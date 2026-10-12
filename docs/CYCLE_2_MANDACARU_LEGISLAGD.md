# Ciclo 2 — Observatório Mandacaru e LegislaGD

**Data:** 12/10/2026  
**Linha de base:** SDKA Core 1.0 integrada à `main` (`11248eee42852196ab4a6905c75e594c31da5368`).  
**Estado:** ciclo iniciado; triagem estática, não homologação operacional.

## Princípios e fronteiras

- Trabalho **Automation First**; inspeção de código e testes antes de avaliação humana prática.
- SDKA mantém Skills e governança transversais. Cada repositório mantém seus códigos, decisões e issues; não duplicar fontes MASTER.
- Sem deploy, merge automático, ativação de Skills experimentais ou alegação de teste executado sem evidência.
- Mudanças técnicas devem ser realizadas em PRs específicos de cada produto; fluxo de aprovação de cada repositório permanece obrigatório.

## Trilha A — Observatório Mandacaru

**Base consultada:** `sertaodigitalorg/ObservatorioMandacaru/docs/AUDITORIA-2026-10.md`, `docs/roadmap.md` e Skill `observatorio-mandacaru` da SDKA.

**Estado documentado:** MVP em evolução, Symfony/Angular/PostgreSQL; instituições, projetos, indicadores, conteúdo editorial, permissões e APIs. A infraestrutura declara Meilisearch, **sem integração funcional comprovada**. IA, MCP, Qdrant, ingestão e proveniência estruturada não estão implementados segundo a auditoria.

**Primeiro incremento, dentro da Fase 0 do roadmap:**
1. Inventariar testes existentes e verificar execução local/CI sem tocar produção.
2. Auditar configurações, segredos e autorização dos endpoints, registrando somente achados saneados.
3. Verificar busca textual ponta a ponta e delimitar integração atual versus arquitetura alvo.
4. Abrir issues por defeito reproduzível e PRs pequenos com testes e documentação.

**Não iniciar agora:** novas entidades de Pessoa/Knowledge Source, taxonomia abrangente, MCP, IA ou integrações do roadmap sem decisão aprovada.

## Trilha B — LegislaGD

**Base consultada:** `sertaodigitalorg/LegislaGD/docs/inventario-repositorios.md`, `docs/roadmap/fase-0-diagnostico.md` e Skill `legislagd`.

**Estado documentado:** plataforma agregadora de SAPL-SD, PortalModelo-SD, e-Cidade-SD, SIGI-SD, identidade Keycloak Legislativo e Plenário Digital. O inventário histórico de 02/08/2026 explicita inspeções profundas ainda pendentes. Documentos de arquitetura não comprovam, por si, integração funcional dos componentes.

**Primeiro incremento, dentro da Fase 0 do roadmap:**
1. Atualizar inventário dos repositórios componentes: branches, upstream, dependências, licenças, CI, testes e contratos de API.
2. Revisar proteção de branches e CI de `LegislaGD` sem alterar a política de merge.
3. Classificar evidências de SSO, integrações e Plenário Digital por `implementado/parcial/planejado/não verificado`.
4. Registrar riscos e abrir issues/PRs por módulo e impacto, sem mudança estrutural ou deploy.

**Não iniciar agora:** refatoração dos forks upstream, migrações de dados, novas integrações entre Poderes ou alterações de hardware sem gate técnico.

## Orquestração e rastreabilidade

| Etapa | Observatório Mandacaru | LegislaGD |
| --- | --- | --- |
| 1 | Auditoria de testes, configuração e segurança | Inventário atualizado de módulos, upstream e CI |
| 2 | Busca e fluxo de publicação com evidências | SSO, contratos e Plenário Digital com evidências |
| 3 | Issues e correções controladas | Issues e correções por componente |
| 4 | Revisão humana e homologação do incremento | Revisão humana e homologação do incremento |

### Critério de aceite do início do ciclo

- [x] Conferir os dois repositórios e suas Skills ativas.
- [x] Registrar escopo inicial baseado nos documentos versionados.
- [ ] Abrir e executar auditorias técnicas próprias dos dois produtos.
- [ ] Publicar matriz de achados verificáveis (SHA, caminho, evidência, impacto).
- [ ] Criar issues de correção sustentadas por testes e logs expurgados.
- [ ] Homologar os incrementos depois dos gates de CI e revisão.

**Este plano não substitui os roadmaps próprios dos produtos nem declara a execução de testes.**
