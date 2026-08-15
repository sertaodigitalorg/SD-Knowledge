# Próximos Passos - Roadmap SDKA

Fases de desenvolvimento e expansão da SDKA.

---

## Status Atual (Fase 1 - Foundation)

✅ Concluído:

- Estrutura base SDKA
- Skill sertaodigital-core
- Skill legislagd
- Manifestos (knowledge.yaml, sources.yaml, etc)
- Schemas JSON
- Documentação técnica
- GitHub Actions workflows básicos
- AGENTS.md bootstrap

---

## Fase 2 - Integração e Expansão (3-4 meses)

### Integrações com Google Drive

- [ ] Integração com API Google Drive
- [ ] Ferramenta de export Markdown automático
- [ ] Sincronização bidirecional controlada
- [ ] Webhook Drive → GitHub para mudanças
- [ ] Validação de IDs de pasta

**Outcome:** Drive sincroniza com GitHub sem overhead manual.

### Skills Adicionais

- [ ] **SIGI-SD Skill** — Atendimento ao cidadão
- [ ] **VEREDAS Skill** — Participação cidadã
- [ ] **Plataforma360 Skill** — Gestão integrada
- [ ] **Tecnologias Compartilhadas Skill** — Docker, Kubernetes, etc
- [ ] **Padrões Arquiteturais Skill** — RBAC, APIs, etc

**Outcome:** Todas as linhas de produtos com Skills definidas.

### Exportação de Contexto

- [ ] Ferramenta `export-context`
- [ ] Gerar Markdown portátil para IA
- [ ] Compilar Skills em contexto unificado
- [ ] Validar referências antes de export
- [ ] Versionamento de exports

**Outcome:** Contexto estruturado pronto para IA consumir.

### Validação Avançada

- [ ] Validação automática de referências cruzadas
- [ ] Detecção de Skills conflitantes
- [ ] Validação de manifesto contra schemas
- [ ] Teste de dependências circulares
- [ ] Relatório de cobertura de documentação

**Outcome:** CI/CD garante integridade de conhecimento.

---

## Fase 3 - Automação e Inteligência (6+ meses)

### Registry Global de Skills

- [ ] Repositório público de Skills
- [ ] Instalação/sincronização de Skills
- [ ] Versioning e compatibilidade
- [ ] Descoberta de Skills
- [ ] Métrica de uso e qualidade

**Outcome:** Comunidade pode compartilhar Skills.

### IA Avançada

- [ ] RAG (Retrieval-Augmented Generation) com SDKA
- [ ] Integração com LLM local
- [ ] Análise automática de impacto entre produtos
- [ ] Sugestões de mudanças arquiteturais
- [ ] Validação automática contra SOURCE_OF_TRUTH

**Outcome:** Agentes fazem decisões mais sofisticadas.

### Integração com Repositórios

- [ ] AGENTS.md em cada repositório de produto
- [ ] Auto-discovery de Skills
- [ ] Link automático de repositório ↔ Skill
- [ ] Alertas de mudanças de compatibilidade

**Outcome:** Cada repositório "sabe" qual Skill o governa.

### Análise de Impacto

- [ ] Ferramenta de análise de impacto cruzado
- [ ] Gráfico de dependências de produtos
- [ ] Simulação de mudança arquitetural
- [ ] Previsão de quebra de compatibilidade
- [ ] Relatórios para decisão

**Outcome:** Decisões técnicas mais informadas.

---

## Fase 4 - Ecossistema (12+ meses)

- [ ] Integração com múltiplos Poderes (Legislativo + Executivo)
- [ ] Federação de identidades entre poderes
- [ ] Sincronização de dados intergovernamental (com consentimento)
- [ ] Skills para cada Poder separadamente
- [ ] Marketplace de Agents
- [ ] Certificação de Skills
- [ ] Padrão aberto de SDKA (ISO/DIN?)

---

## Métricas de Sucesso

### Fase 1 (Foundation)
- ✅ Estrutura em produção
- ✅ 2 Skills ativas
- ✅ CI/CD funcionando
- ✅ Documentação completa

### Fase 2 (Integration)
- 5+ Skills ativas
- Export-context funcionando
- Drive sincronizado
- Validação automática robusta

### Fase 3 (Automation)
- Registry global de Skills
- IA consumindo SDKA efetivamente
- 10+ Skills documentadas
- Análise de impacto automática

### Fase 4 (Ecosystem)
- Múltiplos Poderes integrados
- Comunidade ativa contribuindo Skills
- Padrão amplamente adotado
- Impacto mensurável na velocidade de desenvolvimento

---

## Dependências Externas

Para progredir entre fases:

- [ ] Aprovação institucional para integração Drive
- [ ] Decisão sobre licença (Fase 1 blocka)
- [ ] Recursos de desenvolvimento
- [ ] Infraestrutura para webhooks (Fase 2)
- [ ] LLM para IA avançada (Fase 3)
- [ ] Governança intergovernamental (Fase 4)

---

## Como Contribuir

### Agora (Fase 1)

- [ ] Testar estrutura
- [ ] Reportar erros na documentação
- [ ] Propor novas Skills
- [ ] Sugerir melhorias em AGENTS.md
- [ ] Validar schemas

### Próximo (Fase 2)

- [ ] Desenvolver Skills adicionais
- [ ] Trabalhar em export-context
- [ ] Integração Drive (quando aprovada)
- [ ] Expandir testes

---

**Versão:** 1.0.0  
**Última atualização:** 2026-08-15  
**Status:** Foundation Release → Planning Fase 2
