# Changelog

Todas as mudanças notáveis neste projeto são documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Fixed

- validated repository registry
- removed unverified technical assumptions
- clarified normative vs illustrative content
- hardened technical decision governance
- improved source-of-truth consistency

## [1.0.0] - 2026-08-15

### Added

- Estrutura inicial SDKA (Arquitetura de Conhecimento e Skills)
- Skill `sertaodigital-core` — contexto institucional e arquitetural
- Skill `legislagd` — contexto funcional da plataforma legislativa
- Manifestos de conhecimento (knowledge.yaml, sources.yaml, products.yaml, repositories.yaml)
- Documentação arquitetural completa (docs/)
- JSON Schemas para validação de manifestos
- GitHub Actions workflows para CI/CD
- Validação automática (YAML, JSON, Markdown)
- Guia de contribuição (CONTRIBUTING.md)
- Código de conduta (CODE_OF_CONDUCT.md)
- Procedimento de segurança (SECURITY.md)
- Template de Pull Request
- Estrutura de Issues templates
- Diretório de exemplos

### Planned

- Integração com IDs reais do Google Drive
- Skills adicionais (SIGI-SD, VEREDAS, Plataforma360, etc)
- Ferramenta de exportação de contexto para IA
- Validação automática de referências
- Sincronização controlada com Google Drive
- Registry de Skills global

---

## Como Versionar

- **Major**: Mudanças estruturais na SDKA, quebra de compatibilidade
- **Minor**: Novas Skills, novos produtos registrados, extensões
- **Patch**: Correções, atualizações de documentação, melhorias

Siga [Semantic Versioning](https://semver.org/).
