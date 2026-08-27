# GitHub Safety Ruleset Runbook

Status: Ready for enforcement
Data: 2026-08-27
Escopo inicial: `sertaodigitalorg/SD-Knowledge`

## Objetivo

Configurar proteção técnica de branches e Pull Requests conforme a `DOCUMENTATION_SAFETY_PRESERVATION_POLICY.md` e o ADR-009.

## Estado identificado em 2026-08-27

- branch padrão: `main`;
- `main` não protegida;
- nenhum repository ruleset ativo;
- branches `dev` e `hml` não existem neste repositório;
- workflows existentes: `Markdown Lint` e `Validate Knowledge`;
- novo check proposto: `Destructive Action Guard`.

## Ruleset obrigatório para `main`

Nome sugerido: `SD-Knowledge - Main Protection`

Target: Branch
Enforcement status: Active

Target branch:

- Include default branch (`~DEFAULT_BRANCH`) ou `main` explicitamente.

Ativar:

1. Restrict deletions
2. Block force pushes
3. Require a pull request before merging
4. Require approvals: 1
5. Dismiss stale pull request approvals when new commits are pushed
6. Require conversation resolution before merging
7. Require status checks to pass
8. Require branches to be up to date before merging, se operacionalmente viável
9. Do not allow bypass para agentes/bots

Status checks recomendados:

- `Destructive Action Guard`
- checks de `Validate Knowledge`
- `Markdown Lint` quando aplicável

## Bypass

Princípio: bypass mínimo.

- não conceder bypass a GitHub Apps, bots, agentes de IA ou tokens operacionais;
- administradores humanos devem usar bypass somente em recuperação/incidente, com justificativa registrada;
- ações normais devem continuar por PR.

## Permissões de agentes

Credenciais usadas por agentes devem preferir conteúdo/PR com menor privilégio e não devem possuir autorização administrativa de repositório.

Operações explicitamente vedadas para agentes:

- exclusão de repositório;
- alteração de rulesets/proteções;
- force push;
- exclusão de branch protegida;
- alteração de configurações de segurança para reduzir enforcement;
- destruição do histórico Git.

## Arquivos constitucionais/protegidos

O workflow `Destructive Action Guard` trata a exclusão dos seguintes arquivos como proibida:

- `AGENTS.md`
- `SECURITY.md`
- `governance.yaml`
- `docs/SOURCE_OF_TRUTH.md`
- `docs/DOCUMENTATION_SAFETY_PRESERVATION_POLICY.md`
- `docs/ADR-009-documentation-safety-destructive-action-gate.md`
- `docs/DESTRUCTIVE_ACTION_GATE_SPEC.md`
- `.github/workflows/destructive-action-guard.yml`

Alterações nesses arquivos continuam possíveis via PR e revisão humana; a exclusão direta é bloqueada pelo check.

## Blast radius inicial

O check falha quando detectar:

- mais de 5 arquivos excluídos;
- mais de 20 arquivos alterados no mesmo PR;
- mais de 1000 linhas removidas;
- exclusão de arquivo constitucional/protegido.

Esses valores são deliberadamente conservadores e podem ser refinados mediante ADR/revisão de governança.

## Ordem de ativação

1. merge do workflow `Destructive Action Guard`;
2. validar execução do check em PR de teste;
3. criar ruleset `SD-Knowledge - Main Protection`;
4. incluir o check como required status check;
5. validar que push direto, force push e delete de `main` estão bloqueados;
6. registrar evidências da ativação.

## Expansão para outros repositórios

Para repositórios com fluxo `dev -> hml -> main`, criar proteção equivalente para as três branches permanentes, respeitando o branch flow específico do produto.

A existência do ruleset não substitui workflows de fluxo de branch já adotados em projetos como LegislaGD; as duas camadas devem operar juntas.
