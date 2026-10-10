# Skill: observatorio-mandacaru

## Metadados

| Campo | Valor |
|---|---|
| **Name** | `observatorio-mandacaru` |
| **Type** | product-context |
| **Status** | active |
| **Produto** | Observatório Mandacaru |
| **Subtítulo** | Plataforma de Inteligência Territorial e Ecossistêmica do Sertão Digital |
| **Dependência** | `sertaodigital-core` |

## Propósito e identidade

Contextualizar o produto ativo/em desenvolvimento e orientar alterações sem confundir capacidades implementadas, parciais, planejadas ou conceituais. “Observatório Sertão Digital” é nomenclatura anterior; marca atual: **Observatório Mandacaru**. Não renomeie classes, namespaces ou identificadores internos sem necessidade técnica.

## Autoridade e fonte de verdade

- Google Drive: MASTER institucional, estratégico e funcional.
- GitHub: MASTER técnico, código, APIs, deploy, Skills e ADRs.
- Observatório Mandacaru: MASTER dos dados estruturados do ecossistema, preservando proveniência/referências às fontes originais.
- SD-Knowledge: manifestos, contexto e distribuição de conhecimento.
- GPT_SOURCE e exports: derivados, nunca substituem a fonte MASTER.

Consulte `docs/SOURCE_OF_TRUTH.md`, READ/WRITE/ACCESS e o estado de acesso antes de concluir que uma fonte não existe. Uma cópia técnica de requisitos funcionais não substitui o Drive.

## Estado atual verificado

O repositório `sertaodigitalorg/ObservatorioMandacaru` contém MVP com backend Symfony 8.1/PHP >= 8.4, frontend Angular 22, PostgreSQL 17 no Compose raiz, Traefik e Meilisearch declarado em infraestrutura. Existem autenticação por sessão, papéis, contas, instituições, projetos, indicadores, posts/tags, REST, área de usuário, revisão editorial e histórico parcial.

Busca usa quatro endpoints públicos combinados no Angular; não foi encontrada integração de indexação/Search API com Meilisearch. `CadastroHistorico` cobre parte do fluxo de contribuição/revisão, não toda edição administrativa. Não foram encontrados testes HTTP dos controllers nem implementação de IA/MCP/RAG/vetores/grafo/ETL.

Use os estados da matriz da auditoria do produto: `IMPLEMENTADO`, `PARCIAL`, `PLANEJADO` e `AUSENTE`. Quando apropriado, registre `PROPOSTO/CONCEITUAL`. Código e testes são evidência; roadmap não é.

## Arquitetura, domínio e roadmap

- Arquitetura atual e alvo: [architecture.md](architecture.md).
- Entidades e relações: [domain.md](domain.md).
- Fontes/documentos: [references.md](references.md).
- Decisões pendentes: [references/decisions.md](references/decisions.md).

O núcleo atual é `User`, `Instituicao`, `Projeto`, `Indicador`, `Post`, `Tag` e `CadastroHistorico`. A conta `User` implementa perfis autodeclarados `pessoa`, `instituicao`, `empresa`, `estudante` e `professor`; também armazena formação profissional e nome da empresa nos perfis correspondentes. Esses campos não constituem entidades próprias de Pessoa ou Empresa. Territórios, modelo ampliado de pessoas/competências, evidências/fontes, pesquisas, programas/políticas, tecnologias, oportunidades e relações genéricas permanecem roadmap/conceito até decisão.

## Governança e proveniência

O modelo-alvo deverá rastrear fonte, origem, coleta, responsável, método, atualização, confiabilidade, evidência, validação, curadoria, publicação e revisão. O domínio atual ainda não modela proveniência estruturada. Não criar entidades de governança automaticamente.

## Busca e IA

Meilisearch está na infraestrutura, não na integração funcional confirmada. A arquitetura-alvo de busca é PostgreSQL → indexador backend → Meilisearch → Search API → Angular. Nunca expor `MEILI_MASTER_KEY` ao frontend.

IA não é fonte de verdade nem substitui o dado canônico. Respostas precisam apontar fontes; escritas assistidas exigem autorização e auditoria. REST é o alvo sistema↔sistema e MCP o alvo IA↔ecossistema referenciado funcionalmente; o MCP ainda é futuro, opera por APIs/serviços autorizados e nunca por SQL direto. Não selecionar LLM, embeddings, vector DB ou grafo sem decisão/ADR aplicável.

## Segurança

Não versionar segredos, tokens ou dados pessoais; não reproduzir valores em issues/relatórios. Usar configuração local ignorada ou secret manager e revisar defaults de Compose antes de publicação. A auditoria do produto registrou a remoção do segredo de desenvolvimento do arquivo atual, necessidade de rotação e riscos condicionais nos endpoints públicos e serviços de infraestrutura.

## Regras de mudança

1. Ler `SD-Knowledge/AGENTS.md`, esta Skill, `sertaodigital-core/SKILL.md` e `ObservatorioMandacaru/AGENTS.md`.
2. Ler `ObservatorioMandacaru/docs/` e consultar o código/testes para confirmar estado.
3. Não inventar requisito nem promover roadmap a implementado.
4. Executar Technical Decision Gate para decisões estruturais; documentar ADR sem fabricar rationale histórico.
5. Avaliar Cross-Layer Impact e sincronizar ou gerar Prompt Handoff conforme o acesso à fonte MASTER.
6. Atualizar testes e documentação junto com mudanças funcionais/técnicas.
7. Nunca versionar segredos.
