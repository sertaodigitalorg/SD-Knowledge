# Fase B — GitHub Safety Enforcement — Relatório de Implantação

Status: IMPLEMENTED
Data: 2026-08-27
Repositório: `sertaodigitalorg/SD-Knowledge`

## Objetivo

Transformar a política de preservação documental em controles técnicos efetivos no GitHub, reduzindo o risco de exclusão, force push, alteração destrutiva em massa e merge sem revisão.

## Evidências de implantação

### Workflow

Foi implantado `.github/workflows/destructive-action-guard.yml` pelo PR #3.

O guard atua sobre Pull Requests e bloqueia alterações classificadas como destrutivas conforme thresholds iniciais, incluindo exclusão de arquivos constitucionais/protegidos, exclusões em massa, alterações excessivamente amplas e remoções de grande volume.

O workflow utiliza permissão somente de leitura de conteúdo (`contents: read`).

### Ruleset

Ruleset ativo: `SD - Protected Main`

ID GitHub: `21675435`

Target: branch padrão (`~DEFAULT_BRANCH`), atualmente `main`.

Configuração efetivamente validada via GitHub API:

- enforcement: `active`;
- restrict deletions;
- block non-fast-forward / force push;
- Pull Request obrigatório;
- 1 aprovação obrigatória;
- dismiss stale approvals on push;
- resolução de review threads obrigatória;
- aprovação adicional para mudanças Copilot não atribuídas;
- branch deve estar atualizada antes do merge;
- status check obrigatório: `Destructive Action Guard`;
- bypass list vazia;
- usuário corrente não pode fazer bypass.

## Fluxo operacional resultante

`branch de trabalho -> Pull Request -> revisão -> Destructive Action Guard -> branch atualizada -> merge -> main`

Alteração direta destrutiva da `main` deixa de ser fluxo operacional aceito.

## Limitações conscientes

O `SD-Knowledge` não possui `dev` ou `hml`. Não foram criadas branches artificiais: por ser repositório de conhecimento/governança, o modelo adotado permanece `branch de trabalho -> PR -> main`, com proteção forte da branch padrão.

Code scanning, code quality e coverage não foram tornados obrigatórios nesta fase para evitar dependências de checks ainda não institucionalizados.

## Critério de encerramento

A Fase B é considerada IMPLEMENTED porque existem simultaneamente:

1. política formal;
2. guard automatizado no CI;
3. ruleset ativo;
4. proteção contra exclusão e force push;
5. revisão humana obrigatória;
6. check destrutivo obrigatório;
7. ausência de bypass permanente.

## Próxima fase

Fase C — Google Drive / SDKA Functional Bridge Safety Enforcement.
