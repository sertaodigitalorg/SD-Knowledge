# Tools

Ferramentas para validação, exportação e manutenção da SDKA.

## Validação

Scripts e ferramentas para validar conhecimento.

### Como Usar

```bash
# Validação YAML
yamllint *.yaml

# Validação JSON
python -m json.tool arquivo.json

# Validação contra Schemas
python scripts/validate_schemas.py

# Detecção de Secrets
detect-secrets scan
```

## Exportação de Contexto

Ferramentas para compilar contexto para IA.

### export-context

Gera Markdown portátil de contexto.

```bash
./export-context.py --skill legislagd --output contexto.md
```

*Ainda não implementado — Fase 2*

## Manutenção

Scripts auxiliares de manutenção.

- Link validation
- Cross-reference checking
- Dependency analysis
- Impact analysis (futuro)

## Implementação

A maioria das ferramentas está em:

- GitHub Actions workflows (`.github/workflows/`)
- Python scripts (futuros)
- Documentação (docs/)

---

Mais informações em [docs/NEXT_STEPS.md](../docs/NEXT_STEPS.md) — Fase 2.
