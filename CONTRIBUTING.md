# Contribuindo

Obrigado por considerar contribuir para a SDKA! Este documento fornece diretrizes para contribuir.

## Como Contribuir

### 1. Identificar o Problema ou Recurso

Comece abrindo uma issue descrevendo:
- O que você quer melhorar ou corrigir
- Contexto e motivação
- Impacto esperado

### 2. Criar uma Branch

```bash
git checkout -b feature/descricao
# ou
git checkout -b fix/descricao
git checkout -b docs/descricao
```

**Convenção de branches:**
- `feature/*` — nova funcionalidade
- `fix/*` — correção de bug
- `docs/*` — melhorias de documentação
- `chore/*` — manutenção

### 3. Fazer Mudanças

- Siga os padrões de documentação existentes
- Valide YAML e JSON
- Atualize referências relacionadas
- Adicione comentários para mudanças complexas

### 4. Commits

Use Conventional Commits:

```
feat: descrever nova funcionalidade
fix: descrever correção
docs: descrever mudança de documentação
chore: descrever manutenção
refactor: descrever refatoração
```

Exemplos:
```
feat: adicionar skill VEREDAS
fix: corrigir referência em knowledge.yaml
docs: atualizar SDKA.md com nova seção
```

### 5. Push e Pull Request

```bash
git push origin feature/descricao
```

No Pull Request, forneça:
- **Objetivo**: O que mudou e por quê
- **Tipo**: feature, fix, docs, chore
- **Skill afetada**: Se aplicável
- **Produto afetado**: Se aplicável
- **Fontes consultadas**: Referências utilizadas
- **Impacto funcional**: Como isso afeta os usuários finais
- **Impacto técnico**: Como isso afeta a arquitetura
- **Documentação atualizada**: Sim/não e quais documentos
- **Segurança**: Nenhuma secret exposta
- **Checklist**: Revisão de padrões

### 6. Revisão e Merge

Um mantenedor revisará sua contribuição e conversará sobre qualquer mudança necessária.

## Padrões de Documentação

- Use Markdown para toda documentação
- Adicione metadados YAML quando apropriado
- Mantenha links relativos para referências internas
- Use código e exemplos onde apropriado

## Arquivos Obrigatórios

Certos arquivos não devem ser alterados sem discussão:

- `AGENTS.md` — bootstrap central
- `VERSION` — siga semver
- `CHANGELOG.md` — siga Keep a Changelog
- `docs/SOURCE_OF_TRUTH.md` — hierarquia de fontes

## Perguntas?

Consulte:
- [README.md](README.md) para visão geral
- [docs/SDKA.md](docs/SDKA.md) para arquitetura
- [docs/SOURCE_OF_TRUTH.md](docs/SOURCE_OF_TRUTH.md) para hierarquia de fontes

Obrigado por contribuir!
