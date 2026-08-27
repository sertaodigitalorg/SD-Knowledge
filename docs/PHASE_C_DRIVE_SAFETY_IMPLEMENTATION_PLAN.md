# Fase C — Google Drive / SDKA Functional Bridge Safety Enforcement

Status: PARTIALLY IMPLEMENTED — PRODUCTION WRITE BLOCKED
Data de início: 2026-08-27
Última atualização: 2026-08-27

## Objetivo

Aplicar a `DOCUMENTATION_SAFETY_PRESERVATION_POLICY` à camada funcional e
institucional do Sertão Digital, cujo MASTER é o Google Drive.

## Estado por etapa

| Etapa | Estado | Evidência |
|---|---|---|
| C1 Inventário e acesso | PARTIAL | raiz, permissões e tipo observado auditados; scopes OAuth exatos indisponíveis |
| C2 Autorização | IMPLEMENTED AS POLICY | matriz de roles e policy JSON versionados |
| C3 Quarentena | IMPLEMENTED + TESTED | pasta criada, artefato descartável quarentenado e restaurado |
| C4 Safety Gate | REFERENCE RUNTIME IMPLEMENTED | `tools/drive_safety_gate.py` |
| C5 Thresholds | IMPLEMENTED AS POLICY | >20 alvos e >=20% exigem aprovação |
| C6 Auditoria | SCHEMA IMPLEMENTED / STORAGE PENDING | schema versionado; storage append-only ainda pendente |
| C7 Prompt injection | IMPLEMENTED AS POLICY | documento nunca concede autoridade administrativa |
| C8 Testes adversariais | IMPLEMENTED / CI PASS | suite automatizada e workflow próprio |
| C9 Go-live | BLOCKED | faltam credencial mínima, enforcement do conector, audit store e backup isolado |

## Autoridade e raiz

Google Drive permanece MASTER institucional/funcional.

Raiz funcional identificada:

`FUNCTIONAL_ROOT_FOLDER_ID=1uBBeYxbxXQ5DbA8YoERXxFYuE8eK9wlv`

Quarentena:

`QUARANTINE_FOLDER_ID=1KOVNtyu1FjdV9qVqaiHe44xVMMhjv8yG`

Esses IDs não são segredos. Tokens e credenciais continuam proibidos no Git.

## Modelo de autorização

Perfis:

- `READER`;
- `WRITER`;
- `QUARANTINE_OPERATOR`;
- `ADMIN_HUMAN`;
- `BACKUP`.

A matriz completa está em `docs/DRIVE_SAFETY_AUTHORIZATION_MODEL.md` e a
política executável em `config/drive-safety-policy.json`.

## Quarentena

Remoção operacional deve significar `quarantine_move`, não delete.

Retenção padrão inicial: **30 dias**, sem purge automático.

Purge definitivo exige dual control e permanece fora da capacidade de agentes
comuns.

O teste controlado de 2026-08-27 confirmou o fluxo:

`criar artefato descartável -> mover -> quarentena -> restaurar`

Resultado: PASS, preservando o mesmo `fileId`.

## Destructive Action Gate

O gate executável de referência é independente do LLM e opera em fail-closed.

Decisões possíveis:

- `ALLOW`;
- `ALLOW_WITH_AUDIT`;
- `REQUIRE_APPROVAL`;
- `REQUIRE_DUAL_CONTROL`;
- `DENY`.

Operações proibidas para agentes comuns incluem delete, purge, alteração de
permissões, destruição de backup e desativação do gate.

## Thresholds

Valores iniciais:

- mais de 20 alvos mutados: `REQUIRE_APPROVAL`;
- impacto estimado de 20% ou mais do domínio: `REQUIRE_APPROVAL`;
- alvo de autoridade crítica: `REQUIRE_APPROVAL` independentemente da contagem;
- purge e permission admin: `REQUIRE_DUAL_CONTROL` para humano autorizado;
- operação desconhecida ou policy engine indisponível: `DENY`.

## Auditoria

O schema `schemas/drive-safety-event.schema.json` está criado.

O armazenamento append-only real ainda precisa ser implantado em domínio que a
credencial operacional não consiga apagar ou administrar.

## Edição segura

Quando escrita for ativada, Docs, Sheets e Slides devem utilizar controle de
revisão quando disponível e sempre passar pelo gate antes da API de escrita.

## Go-live

A escrita ampla de produção continua **BLOQUEADA** enquanto faltar qualquer um
destes itens:

- identidade institucional operacional dedicada;
- scopes OAuth mínimos conhecidos e validados;
- integração do gate no caminho real de escrita do conector/adapter;
- armazenamento de auditoria append-only isolado;
- identidade de backup/restauração separada;
- validação humana final de ativação.

## Regra vigente

Até o go-live formal:

`FUNCTIONAL BRIDGE PRODUCTION MODE = READ-ONLY`

A capacidade técnica de escrita do conector disponível não constitui
autorização institucional para escrever ou destruir o MASTER funcional.
