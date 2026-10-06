# Skill: observatorio-mandacaru

## Metadados
- **Name:** observatorio-mandacaru
- **Type:** product-context
- **Status:** active
- **Produto:** Observatório Mandacaru
- **Dependência:** sertaodigital-core

## Propósito
Fornecer o contexto funcional e técnico necessário para trabalhar no Observatório Mandacaru sem confundir estado implementado, arquitetura alvo e hipótese futura.

## Autoridade
- Google Drive: MASTER institucional, estratégico e funcional.
- GitHub: MASTER técnico, código, APIs, deploy e ADRs.
- Observatório Mandacaru: MASTER dos dados estruturados do ecossistema.
- SD-Knowledge: catálogo, contexto e distribuição de conhecimento.
- GPT_SOURCE e exports: derivados.

## Estado atual verificado
O produto possui MVP técnico em evolução no repositório `sertaodigitalorg/ObservatorioMandacaru`, com backend Symfony, frontend Angular, PostgreSQL, Docker/Traefik, autenticação, usuários/papéis, instituições, projetos, indicadores, posts, tags, histórico/auditoria, APIs e workflow editorial. Meilisearch existe na infraestrutura; sua cobertura funcional deve ser verificada no código antes de tratá-lo como busca consolidada.

## Arquitetura alvo aprovada
A documentação funcional/arquitetural aprova REST para sistema↔sistema e MCP para IA↔ecossistema. O MCP deve operar sobre APIs/serviços de domínio, nunca por acesso SQL direto. Governança/higiene do conhecimento, Qdrant, Redis/Kestra dedicados, BI, integrações externas e planos avançados são roadmap até haver evidência técnica.

## Regra de status
Use sempre: IMPLEMENTADO, EM IMPLEMENTAÇÃO, PLANEJADO, CONCEITUAL ou DESCONTINUADO. Código e testes são evidência do estado técnico; documentação de roadmap não é evidência de implementação.

## Domínio
Núcleo já implementado: Instituição, Projeto, Indicador, Post, Tag, User e CadastroHistorico.

Expansão planejada: pessoas/perfis, territórios, competências, tecnologias, oportunidades, fontes/evidências, programas/políticas, relacionamentos, governança de fontes e perfis SDKA.

## Workflow editorial
Preservar a separação entre versão pública e alteração em análise. Fluxo de referência: RASCUNHO → ENVIADO PARA ANÁLISE → REVISÃO → PUBLICADO ou DEVOLVIDO → CORREÇÃO.

## IA e conhecimento
IA não é fonte de verdade. Respostas e escritas assistidas devem ser rastreáveis à fonte, respeitar autorização, classificação de dados e auditoria. Não selecionar LLM, embeddings, vector DB ou grafo sem decisão técnica versionada quando a escolha ainda estiver aberta.

## Decisões pendentes
Consulte `references/decisions.md`. Itens pendentes não devem ser implementados como padrão definitivo antes da decisão.

## Antes de alterar o produto
1. Ler `SD-Knowledge/AGENTS.md`.
2. Ler `skills/sertaodigital-core/SKILL.md` e esta Skill.
3. Ler a documentação do repositório do Mandacaru.
4. Auditar código/testes para confirmar o estado.
5. Aplicar Cross-Layer Impact Check.
6. Para decisão arquitetural relevante, usar Technical Decision Gate e ADR.
7. Nunca expor secrets ou promover roadmap a implementado.
