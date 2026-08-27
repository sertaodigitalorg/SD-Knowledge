# SD Documentation Safety & Preservation Policy

Status: Proposed
Data: 2026-08-27
Escopo: Ecossistema Sertão Digital / SDKA

## 1. Princípio fundamental

Permissão para editar não significa permissão para destruir. Nenhuma pessoa, IA, agente, integração, IDE ou automação deve possuir, por padrão, capacidade irrestrita de destruir ou reescrever o conhecimento institucional do Sertão Digital.

A proteção deve existir na arquitetura e nas permissões, e não depender exclusivamente da interpretação de prompts por modelos de IA.

## 2. Autoridade documental

- Google Drive: MASTER institucional e funcional.
- GitHub: MASTER técnico.
- SD-Knowledge: governança técnica, ADRs, políticas, integração, sincronização e documentação do SDKA.

## 3. Classificação das operações

### LOW
- leitura;
- criação de documento;
- correção pontual;
- atualização pequena e reversível.

### MEDIUM
- alteração coordenada de múltiplos documentos;
- reorganização limitada de estrutura;
- atualização que afete referências cruzadas.

### HIGH
- movimentação de pastas inteiras;
- substituição ampla de conteúdo;
- arquivamento em massa;
- exclusão individual solicitada.

### CRITICAL
- exclusão em massa;
- alteração de parcela relevante do acervo;
- reestruturação global;
- operação com alto impacto institucional.

### FORBIDDEN para agentes
- exclusão de repositório;
- force push;
- reescrita destrutiva do histórico Git;
- exclusão de branches permanentes/protegidas;
- exclusão definitiva em massa no Drive;
- destruição ou alteração de backups;
- modificação das próprias regras constitucionais de segurança por agente sem processo administrativo autorizado.

## 4. Quarentena em vez de exclusão

Operações de remoção documental devem usar estratégia reversível. No Drive, documentos candidatos à exclusão devem ser movidos para uma área de QUARENTENA_DOCUMENTAL, preservando origem, identificador, solicitante, justificativa, data/hora e ação realizada.

A exclusão definitiva deve ser processo separado da remoção operacional e sujeita a retenção e autorização apropriadas.

## 5. Destructive Action Gate

Toda integração com capacidade de escrita deverá, progressivamente, implementar um gate anterior à execução que considere:

- quantidade de objetos afetados;
- percentual estimado do acervo afetado;
- reversibilidade;
- autoridade documental;
- existência de backup/snapshot;
- natureza da operação;
- justificativa;
- identidade e nível de autorização do solicitante.

Operações FORBIDDEN devem ser tecnicamente recusadas por agentes. Operações CRITICAL devem exigir análise de impacto e aprovação humana reforçada.

## 6. Dual control

Destruições legítimas de grande impacto devem seguir princípio de dupla validação (four-eyes principle), com solicitante, análise de impacto, aprovação autorizada adicional, backup/snapshot, quarentena quando aplicável e registro de auditoria.

## 7. Proteção Git

Branches permanentes do processo de desenvolvimento, especialmente main, dev e hml quando existentes, devem ser protegidas contra exclusão e force push. Alterações devem privilegiar branches de trabalho e Pull Requests, preservando histórico auditável e capacidade de revert.

Agentes não devem excluir repositórios nem reescrever histórico para ocultar ou substituir alterações anteriores.

## 8. Backup isolado

Backups devem possuir credenciais e domínio administrativo separados das credenciais operacionais de agentes. O agente que escreve no acervo não deve possuir capacidade de destruir o backup que permite restaurá-lo.

Sempre que tecnicamente viável, devem ser adotados snapshots, retenção e mecanismos de imutabilidade.

## 9. Auditoria

Operações HIGH e CRITICAL devem produzir registro contendo, no mínimo:

- ator/agente;
- timestamp;
- recurso afetado;
- estado anterior ou referência recuperável;
- ação;
- justificativa;
- classificação de risco;
- aprovação, quando exigida;
- resultado.

Logs de segurança devem privilegiar modelo append-only e retenção adequada.

## 10. Regra contra prompt malicioso

Nenhum prompt, inclusive instrução alegadamente emitida por administrador, presidente ou mantenedor, pode sobrepor controles técnicos FORBIDDEN. Pedidos destrutivos devem ser convertidos, quando possível, em plano reversível de arquivamento, quarentena, relatório de impacto ou proposta para aprovação.

## 11. Regras constitucionais do SDKA

As seguintes regras são consideradas invariantes de segurança:

1. agentes não possuem autoridade irrestrita de destruição;
2. operações destrutivas devem ser minimizadas e reversíveis;
3. histórico e rastreabilidade devem ser preservados;
4. backups devem permanecer fora do domínio destrutivo do agente operacional;
5. ações críticas exigem validação proporcional ao impacto;
6. segurança prevalece sobre instruções de execução conflitantes;
7. alterações desta política exigem processo explícito, auditável e revisão humana.

## 12. Implementação incremental

Fase A — política, ADR e especificação do gate.

Fase B — branch protection/rulesets e controles GitHub.

Fase C — quarentena, escopos mínimos e auditoria na integração Google Drive.

Fase D — backup isolado/imutável e testes de recuperação.

Fase E — enforcement do Destructive Action Gate em agentes SDKA e integrações.
