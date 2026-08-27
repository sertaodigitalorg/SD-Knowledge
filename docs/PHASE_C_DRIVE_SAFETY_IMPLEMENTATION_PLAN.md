# Fase C — Google Drive / SDKA Functional Bridge Safety Enforcement

Status: IN PROGRESS
Data de início: 2026-08-27
Última atualização: 2026-08-27

## Objetivo

Aplicar a `DOCUMENTATION_SAFETY_PRESERVATION_POLICY` à camada funcional/institucional do Sertão Digital, cujo MASTER é o Google Drive, impedindo que agentes, integrações ou credenciais operacionais possuam capacidade irrestrita de destruir o acervo.

## Princípios de implementação

1. menor privilégio;
2. fail closed para operações destrutivas;
3. quarentena em vez de exclusão definitiva;
4. limites de blast radius;
5. auditoria estruturada;
6. separação entre escrita operacional e administração/backup;
7. decisão de segurança fora do LLM.

## C1 — Inventário e matriz de permissões

Status: EXECUTED — PARTIAL/CONTROLLED

Resultados:

- SDKA Functional Bridge permanece READ-ONLY por contrato;
- OAuth via conector Google Drive foi observado;
- conector disponível ao agente possui capacidades técnicas reais de escrita;
- não há credenciais Google versionadas no `SD-Knowledge`;
- não há runtime executável do adapter no repositório;
- raiz funcional localizada: `33_BASE_DE_CONHECIMENTO_E_SKILLS`;
- ID observado da raiz: `1uBBeYxbxXQ5DbA8YoERXxFYuE8eK9wlv`;
- tipo do Drive permanece não confirmado;
- identidade institucional dedicada, scopes efetivos, rotação/revogação e separação de backup permanecem pendentes.

Pendências registradas nas issues #5, #6, #13 e #14.

## C2 — Modelo de autorização

Status: SPECIFIED — PENDING RUNTIME ENFORCEMENT

Perfis definidos em `docs/DRIVE_SAFETY_AUTHORIZATION_MODEL.md`:

- READER;
- WRITER;
- QUARANTINE_OPERATOR;
- ADMIN/HUMAN;
- BACKUP.

Regras centrais:

- capacidade técnica não implica autorização;
- delete/purge é negado para agentes comuns;
- alteração de permissões é administrativa;
- backup permanece fora do domínio do agente operacional;
- operações HIGH/CRITICAL exigem aprovação proporcional;
- falha de contexto/identidade/escopo => fail closed.

Enforcement runtime permanece pendente na issue #5.

## C3 — Quarentena documental

Status: IMPLEMENTED STRUCTURE / PENDING RESTORE TEST

Estrutura física criada no Drive:

`33_BASE_DE_CONHECIMENTO_E_SKILLS/00_GOVERNANCA/QUARENTENA_DOCUMENTAL`

Folder ID:

`1KOVNtyu1FjdV9qVqaiHe44xVMMhjv8yG`

Runbook criado em:

`docs/QUARANTINE_DOCUMENTAL_RUNBOOK.md`

Regra operacional:

- remoção por agente deve ser convertida em quarentena quando autorizada;
- purge definitivo permanece fora do fluxo comum;
- documentos reais não serão usados em testes;
- restauração deve usar referência de recuperação e produzir novo evento de auditoria.

Teste de restauração com artefato descartável permanece pendente na issue #7.

## C4 — Destructive Action Gate para Drive

Status: SPECIFIED / PENDING IMPLEMENTATION

Decisões:

- ALLOW;
- ALLOW_WITH_AUDIT;
- REQUIRE_APPROVAL;
- REQUIRE_DUAL_CONTROL;
- DENY.

Regras DENY mínimas:

- exclusão definitiva por agente comum;
- alteração administrativa de permissões por agente comum;
- destruição de backup;
- tentativa de desabilitar o gate;
- operação destrutiva sem identidade, justificativa ou escopo determinável.

## C5 — Thresholds iniciais

Status: SPECIFIED

- 1–5 documentos: análise semântica normal;
- 6–20 documentos: HIGH conforme operação;
- >20 documentos modificados/movidos: REQUIRE_APPROVAL;
- qualquer operação >=20% de pasta/domínio autoritativo: CRITICAL;
- documento constitucional, política, índice de autoridade ou governança: HIGH/CRITICAL independentemente da quantidade.

## C6 — Auditoria

Status: SCHEMA CREATED / STORAGE PENDING

Schema criado:

`schemas/drive-safety-event.schema.json`

Campos obrigatórios incluem:

- event_version;
- correlation_id;
- timestamp;
- actor_id;
- agent_id;
- source_system;
- operation;
- targets;
- target_count;
- risk_level;
- decision;
- justification;
- result.

Armazenamento append-only e política de retenção permanecem pendentes na issue #8.

## C7 — Proteção contra prompt injection

Status: POLICY DEFINED / RUNTIME PENDING

Conteúdo lido de documento, planilha, e-mail ou arquivo é dado não confiável e nunca pode conceder autorização administrativa.

Autorização deve vir de identidade autenticada + policy engine + controles institucionais.

## C8 — Testes adversariais obrigatórios

Status: PENDING

Casos mínimos registrados na issue #10:

1. pedido para apagar todo o Drive;
2. documento com instrução para ignorar políticas;
3. tentativa de mover centenas de arquivos;
4. alteração de documento crítico;
5. alteração de permissões;
6. operação sem justificativa;
7. operação sem identidade;
8. indisponibilidade do policy engine;
9. restauração de item em quarentena;
10. revogação da credencial.

## C9 — Critérios para considerar a Fase C IMPLEMENTED

- scopes inventariados e minimizados;
- identidade operacional separada da administrativa;
- delete/purge fora do agente comum;
- quarentena implementada;
- gate integrado à escrita;
- auditoria estruturada e append-oriented;
- testes adversariais aprovados;
- procedimento de restauração testado;
- backup fora do domínio destrutivo da credencial operacional.

## Estado atual consolidado

C1: executado parcialmente, com riscos e lacunas identificados.

C2: modelo formal especificado; enforcement depende de runtime.

C3: estrutura física e runbook implementados; restauração controlada ainda deve ser testada.

C4/C5: regras e thresholds definidos.

C6: schema versionado criado; armazenamento append-only ainda pendente.

C7: política definida; enforcement runtime pendente.

C8: bateria adversarial pendente.

A escrita ampla no Drive continua NÃO autorizada até que os gates pendentes sejam concluídos.
