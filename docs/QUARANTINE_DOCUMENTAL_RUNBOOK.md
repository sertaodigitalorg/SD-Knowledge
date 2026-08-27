# Runbook — Quarentena Documental

Status: Proposed
Data: 2026-08-27
Escopo: Google Drive institucional / SDKA

## Objetivo

Substituir exclusão operacional por um fluxo reversível, auditável e controlado.

## Local oficial observado

`33_BASE_DE_CONHECIMENTO_E_SKILLS/00_GOVERNANCA/QUARENTENA_DOCUMENTAL`

ID da pasta:

`1KOVNtyu1FjdV9qVqaiHe44xVMMhjv8yG`

## Regra principal

Agentes não executam purge definitivo. Solicitação de remoção deve ser convertida em quarentena quando a operação for autorizada pelo Drive Safety Gate.

## Pré-condições

Antes de mover qualquer recurso:

1. identificar `actor_id` e `agent_id`;
2. registrar `correlation_id`;
3. obter `resource_id`, nome e parent original;
4. registrar justificativa;
5. classificar risco;
6. avaliar quantidade e blast radius;
7. validar decisão do gate;
8. garantir referência de recuperação.

Se qualquer pré-condição essencial estiver ausente, a operação deve falhar fechada.

## Fluxo de quarentena

`pedido de remoção -> classificação -> gate -> auditoria -> move para quarentena -> confirmação -> retenção`

### LOW/MEDIUM

Somente itens não críticos e dentro dos limites definidos podem avançar automaticamente, quando a política assim permitir.

### HIGH

Exige aprovação humana antes do move.

### CRITICAL

Exige controle reforçado e pode ser negado mesmo sendo tecnicamente reversível.

### FORBIDDEN

Nunca executar.

## Metadados mínimos do evento

Usar `schemas/drive-safety-event.schema.json`.

A referência de recuperação deve permitir reconstruir:

- ID do arquivo;
- parent original;
- data/hora;
- motivo;
- ator/agente;
- decisão do gate;
- aprovação, quando aplicável.

## Restauração

A restauração deve:

1. localizar o evento original;
2. validar `recovery_reference`;
3. confirmar o parent original ainda válido;
4. executar move reversível para a origem;
5. registrar novo evento com `operation=restore` e `result=RESTORED`.

Nunca sobrescrever silenciosamente um recurso existente com o mesmo nome.

## Retenção

Proposta inicial: 30 dias.

O prazo definitivo depende de validação institucional/jurídica na issue #12.

Itens devem permanecer retidos quando houver:

- incidente em investigação;
- auditoria;
- disputa sobre conteúdo;
- obrigação legal/administrativa;
- classificação documental crítica.

## Purge definitivo

Purge é operação CRITICAL e fora do fluxo normal do agente.

Pré-requisitos mínimos:

- retenção vencida;
- ausência de hold/auditoria/incidente;
- justificativa;
- snapshot/backup aplicável;
- duas aprovações ou dual control definido;
- registro permanente do evento.

## Teste seguro

Testes devem usar somente artefato descartável criado especificamente para validação.

É proibido usar documento institucional real como cobaia.

Cenário mínimo:

1. criar artefato de teste;
2. registrar origem;
3. mover para quarentena;
4. confirmar presença;
5. restaurar para origem;
6. confirmar conteúdo/ID;
7. registrar evidências;
8. não executar purge.

## Incidente

Se uma movimentação inesperada for detectada:

- interromper novas operações de escrita;
- preservar logs;
- revogar/limitar credencial quando necessário;
- restaurar somente com referência verificável;
- abrir registro de incidente.

## Issues relacionadas

- #7 restauração e retenção;
- #11 runbook operacional;
- #12 retenção;
- #20 aprovação HIGH/CRITICAL.
