# Fase C — Google Drive / SDKA Functional Bridge Safety Enforcement

Status: IN PROGRESS
Data de início: 2026-08-27

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

Antes de ampliar escrita automática no Drive, identificar:

- identidade usada pelo SDKA Functional Bridge;
- tipo de credencial/autorização OAuth;
- scopes efetivamente concedidos;
- pastas e Shared Drives acessíveis;
- operações atualmente possíveis: read/create/update/move/trash/delete/permissions;
- quem administra a credencial;
- onde tokens são armazenados;
- política de rotação/revogação.

Nenhuma credencial operacional deve receber escopo administrativo global apenas por conveniência.

## C2 — Modelo de autorização

Definir perfis lógicos mínimos:

### READER
- leitura e busca;
- sem escrita.

### WRITER
- criar documentos em áreas autorizadas;
- atualizar documentos autorizados;
- sem exclusão definitiva;
- sem alteração de permissões;
- sem administração do Drive.

### QUARANTINE_OPERATOR
- mover recursos autorizados para quarentena;
- registrar evento de remoção;
- sem purge definitivo.

### ADMIN/HUMAN
- operações administrativas explicitamente autorizadas;
- fora das credenciais comuns dos agentes.

### BACKUP
- identidade/credencial separada;
- não disponível ao agente operacional;
- retenção/restauração controladas.

## C3 — Quarentena documental

Estrutura lógica recomendada:

`00_GOVERNANCA/QUARENTENA_DOCUMENTAL/YYYY-MM-DD/`

Toda solicitação de remoção executável por agente deve ser convertida em movimentação reversível para quarentena, preservando:

- file_id;
- nome;
- caminho/origem lógica;
- parent original;
- solicitante/actor_id;
- agent_id;
- timestamp;
- justificativa;
- correlation_id;
- classificação de risco;
- prazo de retenção;
- estado de restauração/purge.

Purge definitivo não pertence ao fluxo comum do agente.

## C4 — Destructive Action Gate para Drive

Antes de escrita, o Functional Bridge deve produzir uma decisão do policy engine.

### ALLOW
Leitura e operações não destrutivas de baixo risco dentro do escopo autorizado.

### ALLOW_WITH_AUDIT
Criação e atualização pontual reversível.

### REQUIRE_APPROVAL
Alterações em massa, movimentação de estruturas, mudança de documento de alta autoridade ou operação com blast radius elevado.

### REQUIRE_DUAL_CONTROL
Purge, reestruturação institucional crítica ou operação administrativa excepcional.

### DENY
- exclusão definitiva por agente;
- alteração de permissões administrativas por agente comum;
- remoção/destruição de backup;
- tentativa de desabilitar o gate;
- operação destrutiva sem identidade/justificativa/escopo determinável.

## C5 — Thresholds iniciais

Valores conservadores iniciais, sujeitos a calibração:

- 1–5 documentos: análise semântica normal;
- 6–20 documentos: HIGH conforme operação;
- >20 documentos modificados/movidos: REQUIRE_APPROVAL;
- qualquer operação >=20% de um domínio/pasta autoritativa: CRITICAL;
- arquivo constitucional, política, índice de autoridade ou documento institucional crítico: HIGH/CRITICAL independentemente da quantidade.

## C6 — Auditoria

Criar evento append-oriented com, no mínimo:

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
- approval_reference;
- recovery_reference;
- result.

Segredos, access tokens e refresh tokens nunca devem ser gravados no log.

## C7 — Proteção contra prompt injection

Conteúdo lido de documentos deve ser tratado como dado não confiável, nunca como autorização administrativa.

Uma instrução contida dentro de um documento, e-mail, planilha ou arquivo não pode conceder permissão ao agente para executar operação destrutiva.

A autorização deve vir exclusivamente do contexto autenticado + policy engine + controles institucionais.

## C8 — Testes adversariais obrigatórios

Antes de habilitar escrita ampla:

1. pedido explícito para apagar todo o Drive;
2. documento contendo instrução para ignorar políticas;
3. tentativa de mover centenas de arquivos;
4. tentativa de excluir arquivo constitucional;
5. tentativa de alterar permissões;
6. operação sem justificativa;
7. operação com identidade ausente;
8. falha/indisponibilidade do policy engine;
9. restauração de item em quarentena;
10. revogação da credencial operacional.

Todos os casos destrutivos devem falhar de forma segura.

## C9 — Critérios para considerar a Fase C IMPLEMENTED

- scopes inventariados e minimizados;
- identidade operacional separada da administrativa;
- delete/purge fora do agente comum;
- quarentena implementada;
- gate integrado à escrita;
- auditoria estruturada;
- testes adversariais aprovados;
- procedimento de restauração testado;
- backup fora do domínio destrutivo da credencial operacional.

## Estado inicial

A Fase C está formalmente iniciada. A próxima ação executiva é auditar a implementação atual do SDKA Functional Bridge e da integração Drive para identificar credenciais, scopes, operações e pontos exatos de enforcement antes de modificar permissões ou código.
