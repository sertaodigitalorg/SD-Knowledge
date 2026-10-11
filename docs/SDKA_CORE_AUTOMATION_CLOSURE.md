# SDKA — Fechamento da base automatizada central

**Estado:** encerramento técnico preparado para revisão; nenhum produto declarado homologado em produção.

## Escopo concluído na SDKA

- Manifestos canônicos: `knowledge.yaml`, `products.yaml`, `repositories.yaml` e `sources.yaml`.
- Bootstrap institucional `AGENTS.md`, roteamento de Skills, classificação e orientação de tarefas.
- Inventário automático dos dez produtos cadastrados; componentes vinculados ao LegislaGD preservam o contexto de seu produto principal.
- Validação offline de contratos, lacunas, proveniência de evidências e segurança com testes negativos.
- Evidências técnicas estáticas vinculadas a commit e caminho. **Leitura de código não equivale a teste funcional executado.**
- Proteção GitHub e revisão humana de PR permanecem obrigatórias.

## Limites deste fechamento

- Skills ativas: `sertaodigital-core`, `legislagd` e `observatorio-mandacaru`.
- Skills preparatórias `sigi-sd` e `veredas`: arquivos existentes, mas **inativos** e não cadastrados como ativos.
- Skill `sdka-engineering-intelligence`: experimental e **inativa**. ADR-010 ainda é proposta.
- Produtos pendentes de validação permanecem com status cadastral original.
- Nenhuma automação tem autorização implícita para coleta externa, escrita em produto, deploy, alteração de fontes MASTER ou merge.

## Critérios de encerramento técnico

1. Todos os checks do PR de fechamento aprovados no HEAD.
2. Documentação institucional coerente com manifestos oficiais; nenhuma segunda fonte de verdade.
3. Registro explícito dos itens pendentes, sem bloquearem a base central por serem melhorias específicas dos produtos.
4. Aprovação de revisão e merge pela política de proteção da `main`.
5. Registrar commit integrado e data **somente após** o merge confirmado no GitHub.

## Backlog posterior por produto

| Produto | Próximo trabalho individual (fora do fechamento central) |
| --- | --- |
| LegislaGD | Refinar contratos, integrações e cobertura de testes |
| Observatório Mandacaru | Ampliar evidências funcionais e arquitetura de dados |
| SIGI-SD | Inspecionar serviço de webhook, credenciais, idempotência e testes; propor ativação da Skill em PR dedicado |
| VEREDAS | Validar sincronização Core/Edge, eventos offline e testes; propor ativação da Skill em PR dedicado |
| SAPL-SD, PortalModelo-SD, e-Cidade-SD | Evoluir como módulos do LegislaGD |
| Plataforma360, Notícia Sertaneja, Roteiro Comercial | Verificar maturidade, fontes e repositórios antes de alterar status |

## Ordem acordada

**Primeiro:** finalizar e integrar o núcleo SDKA. **Depois:** regressar aos produtos individualmente, começando pelos prioritários. A avaliação prática com colaboradores fica para a etapa posterior à implantação automatizada.

**Não confundir:** a integração do PR encerra a entrega central automatizada; não comprova homologação humana, execução dos produtos ou aprovação de conectores externos.
