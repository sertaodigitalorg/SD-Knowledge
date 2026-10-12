# SDKA — Fase 12: integridade da arquitetura central

**Escopo:** validação automática e exclusivamente offline dos registros oficiais da SDKA, independente do PR #32.

## Implementado

- `scripts/sdka_integrity_audit.py`: verifica arquivos `SKILL.md` dos registros, dependências ativas, hierarquia dos produtos e vínculos aos repositórios registrados.
- `scripts/test_integrity_audit.py`: testes positivos e negativos para dependências, parent products, repositórios e caminhos de Skill.
- CI executa auditoria e testes nos PRs relevantes.

## Executar

```bash
python scripts/sdka_integrity_audit.py --report integrity-report.json
python -m unittest discover -s scripts -p 'test_integrity_audit.py' -v
```

A saída `pass` significa **consistência cadastral local**, não comprovação de disponibilidade de GitHub, Drive ou produtos implantados. `review_required` gera código de saída 1 no CLI; ações de correção continuam sujeitas a PR e revisão.

## Limitações intencionais

Não faz chamadas a redes, não descobre credenciais, não cria issues, não muda manifestos e não ativa Skills. Fontes funcionais permanecem no Drive; fonte técnica no GitHub; MASTER de dados estruturados no Observatório Mandacaru.

## Dependências e próximos passos

O PR #32 registra a conclusão da proveniência estática e pode ser revisado e integrado separadamente. Esta Fase 12 pode ser integrada à `main` de forma independente, obedecendo à proteção de branch e à aprovação humana.

Monitoramento periódico, integração de conectores externos e auditoria semântica de documentação são módulos evolutivos posteriores, não pré-requisitos desta validação central.
