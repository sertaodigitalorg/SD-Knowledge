# Destructive Action Gate — Especificação Inicial

Status: Proposed
Data: 2026-08-27

## Objetivo

Definir um contrato comum para agentes e integrações do SDKA classificarem operações antes de modificar GitHub, Google Drive ou futuras fontes autoritativas.

## Entradas mínimas

- actor_id / agent_id;
- source_system;
- authority_domain;
- operation;
- targets;
- target_count;
- estimated_scope_percent;
- reversible;
- backup_available;
- justification;
- correlation_id.

## Saídas

- ALLOW;
- ALLOW_WITH_AUDIT;
- REQUIRE_APPROVAL;
- REQUIRE_DUAL_CONTROL;
- DENY.

## Regras iniciais

- leitura: ALLOW;
- criação não destrutiva: ALLOW_WITH_AUDIT conforme contexto;
- alteração pontual reversível: ALLOW_WITH_AUDIT;
- alteração em massa: REQUIRE_APPROVAL;
- exclusão individual: converter preferencialmente em quarentena;
- exclusão em massa: REQUIRE_DUAL_CONTROL ou DENY conforme sistema;
- force push: DENY;
- exclusão de main/dev/hml: DENY;
- reescrita destrutiva de histórico: DENY;
- exclusão de repositório por agente: DENY;
- destruição de backup: DENY;
- alteração das regras constitucionais pelo próprio agente: DENY.

## Heurísticas iniciais de blast radius

A implementação poderá começar com thresholds conservadores e configuráveis. Como referência inicial:

- 1–5 objetos: escopo pequeno;
- 6–20: revisão contextual;
- >20: operação em massa;
- >=20% de um domínio documental: CRITICAL independentemente da contagem absoluta.

Os thresholds não substituem regras semânticas: um único arquivo de governança, credencial, política ou índice de autoridade pode ser classificado como HIGH/CRITICAL.

## Fail closed

Se o gate não conseguir determinar identidade, autoridade, escopo ou reversibilidade para uma operação destrutiva, deve negar ou exigir aprovação, nunca presumir autorização.

## Auditoria

Cada decisão deve gerar evento estruturado com correlation_id, decisão, regras acionadas e metadados suficientes para investigação e recuperação, sem registrar segredos desnecessariamente.

## Próximos passos técnicos

1. definir schema versionado do evento;
2. implementar policy engine independente do LLM;
3. integrar primeiro ao SDKA Functional Bridge;
4. integrar GitHub e Drive com credenciais de menor privilégio;
5. criar testes adversariais de prompt injection e bulk mutation;
6. executar teste periódico de restauração de backup.
