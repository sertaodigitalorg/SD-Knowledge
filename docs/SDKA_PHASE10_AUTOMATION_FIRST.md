# SDKA — Fase 10: ordem de implantação e validação

**Decisão operacional:** primeiro concluir toda a implantação automatizada; apenas depois iniciar avaliação prática com colaboradores.

## Sequência obrigatória

1. **Implementação técnica:** roteamento de Skills, reconhecimento de produtos, classificação de tarefas, orientações de segurança e documentação de fontes, com LegislaGD e Observatório Mandacaru prioritários.
2. **Automação completa:** CI de contratos, testes de roteamento, cobertura de cenários negativos, preservação dos manifestos oficiais, verificação de dependências e testes de segurança.
3. **Verificação de implantação:** registrar versão/commit, relatório reproduzível dos testes, itens pendentes e riscos. Nenhuma alegação de implantação em produto ou ambiente real sem evidência.
4. **Revisão e PR:** aprovação humana obrigatória de código e requisitos de proteção da `main`. Isto é governança de mudança, não avaliação de usuário.
5. **Homologação prática posterior:** somente após a implantação, conduzir sessões com colaboradores e fichas de avaliação. Reprovações geram issues e PRs corretivos.

## Critérios para fechar a fase automatizada

- [ ] Todos os casos A–D do `scripts/test_phase10_simulation.py` executados com sucesso no CI.
- [ ] Suite de engenharia e todos os checks exigidos no último commit aprovados.
- [ ] Evidências dos testes disponíveis no GitHub Actions, sem dados sensíveis.
- [ ] Fluxo de onboarding e documentação técnica/funcional coerentes com os manifestos MASTER.
- [ ] Registro de limites: nenhuma Skill experimental ativada sem revisão e autorização.
- [ ] PR aprovado e integrado conforme regras institucionais.

**Importante:** o encerramento da fase automatizada não significa que o piloto humano ocorreu. A ficha `docs/templates/SDKA_PHASE10_PILOT_RECORD.md` e a Sessão B permanecem como materiais para a etapa posterior; não preencher notas simuladas nem exigir participação humana agora.
