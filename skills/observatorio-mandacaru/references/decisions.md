# Observatório Mandacaru — Decision Register

Atualizado em 2026-10-06. Este registro contém apenas escolhas que ainda exigem decisão ou detalhamento; decisões já formalizadas no Drive não são reabertas sem nova evidência.

| ID | Decisão | Estado | Recomendação inicial | Impacto |
|---|---|---|---|---|
| OM-DEC-001 | Provedor de identidade do Mandacaru | PENDENTE | Manter autenticação atual no MVP e preparar OIDC; avaliar Keycloak como alvo sem migração imediata | auth, usuários, deploy, integrações |
| OM-DEC-002 | Estratégia definitiva de busca | PENDENTE | Consolidar busca textual com Meilisearch antes de adicionar busca semântica | backend, frontend, indexação |
| OM-DEC-003 | Vector DB/embeddings | PENDENTE | Não implementar agora; Qdrant é arquitetura recomendada no Drive, mas exige ADR antes da adoção operacional | IA, infra, custo |
| OM-DEC-004 | Modelo territorial | PENDENTE | Definir hierarquia mínima País→UF→Município→Território/área antes de ampliar entidades | domínio, indicadores, mapas |
| OM-DEC-005 | Modelo genérico de relacionamentos | PENDENTE | Projetar após taxonomia mínima; evitar criar relações ad hoc por entidade | domínio, grafo futuro |
| OM-DEC-006 | Pessoas/perfis e competências | PENDENTE | Priorizar como próximo domínio estruturante após território, com LGPD desde o schema | domínio, LGPD, MCP futuro |
| OM-DEC-007 | Knowledge Source / Evidence | PENDENTE | Prioridade alta; criar modelo de proveniência antes de ingestão/IA | governança, auditoria, SDKA |
| OM-DEC-008 | Redis e Kestra dedicados | PENDENTE | Introduzir apenas quando houver job/fila/ETL concreto | infra, operação |
| OM-DEC-009 | BI: Metabase ou Superset | PENDENTE | Adiar até indicadores e modelo analítico estabilizarem | BI, deploy |
| OM-DEC-010 | Camada de grafo | PENDENTE | Não adotar agora; avaliar Apache AGE somente quando consultas relacionais justificarem | dados, operação |
| OM-DEC-011 | Escopo inicial do MCP | PENDENTE | Começar read-only após APIs e autorização estabilizarem; escrita somente em fase posterior | IA, segurança |
| OM-DEC-012 | Planos Free/PRO/Business/Enterprise | PENDENTE FUNCIONAL | Separar da evolução do MVP institucional até definição formal de modelo de oferta | produto, autorização, feature flags |
| OM-DEC-013 | Taxonomia canônica | PENDENTE | Workshop funcional antes de codificação em massa | domínio, busca, BI, IA |
| OM-DEC-014 | Política de dados pessoais/sensíveis e retenção | PENDENTE FUNCIONAL/JURÍDICA | Formalizar antes do cadastro ampliado de pessoas | LGPD, segurança |

## Decisões já aprovadas — não pendentes
- Drive = MASTER institucional/funcional.
- GitHub = MASTER técnico.
- Mandacaru = MASTER de dados estruturados do ecossistema.
- SDKA = camada de conhecimento/contexto.
- REST = integração sistema↔sistema.
- MCP = integração IA↔ecossistema, sem acesso SQL direto.
- Escritas de IA devem ser autorizadas e auditáveis.
- Estado implementado deve ser distinguido de planejado/conceitual.
