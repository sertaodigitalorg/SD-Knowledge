# SDKA — Fase 13: relatório institucional determinístico

**Status:** módulo offline de apresentação de estado cadastral. Não equivale a auditoria semântica de produtos ou fontes externas.

## Objetivo

Gerar uma visão única e reproduzível da cobertura dos produtos no catálogo da SDKA, consumindo diretamente `products.yaml`, `repositories.yaml` e `knowledge.yaml`. Não criar catálogo paralelo.

## Execução

```bash
python scripts/sdka_governance_report.py --output governance-report.json
python -m unittest discover -s scripts -p 'test_governance_report.py' -v
```

O relatório informa estado cadastral, repositório, Skill de contexto ativa e necessidade de revisão. Componentes vinculados ao LegislaGD herdam seu contexto institucional de produto; não ganham Skills independentes.

## Limites de confiança e segurança

- `implementation_verified: false` para todos os produtos, pois não há inspeção nem execução técnica nesse relatório.
- `external_evidence_verified: false`, `automated_approval: false`. A existência de uma Skill ativa **não** autoriza deployment ou merge.
- SIGI-SD e VEREDAS continuam sem Skill ativa específica. Produtos pendentes de validação não são promovidos.
- Saída apenas local, não coleta dados, não executa chamadas de rede, não cria issues nem altera manifestos.

## Independência dos PRs

Este trabalho é independente dos PRs #32 (proveniência) e #33 (integridade); pode seguir por sua própria revisão, sujeito às proteções da main. A automação periódica e ações de escrita seguem fora do escopo.
