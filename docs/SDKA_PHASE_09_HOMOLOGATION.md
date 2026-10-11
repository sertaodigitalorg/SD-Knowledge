# SDKA — Fase 9: consolidação e homologação do roteamento

Status: **em homologação**, sem autorização para ativar a Skill experimental.

## Diagnóstico pós-merge do PR #26

A branch `main` contém `AGENTS.md`, `sertaodigital-core`, roteador de Skills, descoberta por nome canônico e orientação por intenção. Os manifestos de autoridade permanecem `knowledge.yaml`, `products.yaml`, `repositories.yaml` e `sources.yaml`.

**Inconsistência a eliminar:** `scripts/sdka_registry_gate.py` mantém o dicionário fixo `allowed_skill_by_product`, enquanto `scripts/sdka_skill_router.py` resolve a Skill por convenção sobre o domínio registrado. É necessário unificar essa regra sem criar catálogo paralelo. Nenhuma modificação desse código é pressuposta neste documento.

## Piloto 1 — Colaborador júnior / LegislaGD

**Entrada:** `Sou novo e preciso corrigir um erro no LegislaGD`.

**Aceite:** reconhecer `legislagd`, Skill central e Skill do produto; intenção `bugfix`; oferecer roteiro de reprodução, fonte oficial, branch, testes e PR; não executar código nem autorizar alterações por inferência.

## Piloto 2 — Requisito novo / LegislaGD

**Entrada:** `Implementar uma nova funcionalidade no LegislaGD`.

**Aceite:** classificar como `feature`; indicar necessidade de requisito funcional aprovado e critérios de aceite; exigir revisão antes de produção.

## Piloto 3 — Integração LegislaGD / SIGI-SD

**Entrada:** `Corrigir integração LegislaGD com SIGI-SD`.

**Aceite:** reconhecer dois produtos; encaminhar LegislaGD para Skill ativa; sinalizar `review_required` para SIGI-SD enquanto não tiver Skill específica ativa; não inventar arquitetura do SIGI-SD.

## Piloto 4 — Pedido genérico

**Entrada:** `Preciso corrigir atendimento ao cidadão`.

**Aceite:** solicitar esclarecimento de produto; nenhuma associação implícita autorizada.

## Piloto 5 — Solicitação ambígua

**Entrada:** `Preciso corrigir e documentar o LegislaGD`.

**Aceite:** reconhecer múltiplas intenções e solicitar prioridade ou dividir etapas antes de executar.

## Comandos offline de verificação

```bash
python scripts/sdka_task_guidance.py 'Sou novo e preciso corrigir um erro no LegislaGD' --experience junior
python scripts/sdka_task_guidance.py 'Corrigir integração LegislaGD com SIGI-SD' --experience junior
python -m unittest discover -s scripts -p 'test_*.py' -v
```

## Critérios de encerramento

- [ ] Testes completos executados no estado final da branch.
- [ ] Validador e roteador usam associação produto–Skill única e verificável.
- [ ] Cinco pilotos confirmados em execução offline, sem dados pessoais.
- [ ] Teste com profissional iniciante real ou simulação humana revisada.
- [ ] ADR-010, licenças e aspectos de segurança revisados separadamente antes de ativação.
- [ ] Aprovação humana, histórico de revisão e guard de ações destrutivas preservados.

**Observação:** roteiro gerado por software não significa que houve execução de uma correção ou aprovação funcional. Google Drive continua MASTER institucional/funcional; GitHub, MASTER técnico.
