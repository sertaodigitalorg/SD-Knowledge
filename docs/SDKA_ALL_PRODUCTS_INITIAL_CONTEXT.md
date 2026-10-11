# SDKA — Contexto inicial de todos os produtos

**Fonte exclusiva para estado cadastral:** `products.yaml`, `repositories.yaml`, `knowledge.yaml`. O script `scripts/sdka_product_inventory.py` gera inventário atualizado, sem catálogo paralelo.

## Como usar

```bash
python scripts/sdka_product_inventory.py
python -m unittest discover -s scripts -p 'test_product_inventory.py' -v
```

Este documento é uma **orientação inicial**, não atesta implementação, arquitetura em produção ou aprovação funcional. A melhoria será realizada produto por produto, com evidências, ADR quando necessário e PR independente.

| Produto | Base de contexto e primeira melhoria | Skill hoje |
| --- | --- | --- |
| Observatório Mandacaru | Inteligência territorial/ecossistêmica e dados estruturados; validar lacunas documentais e evidências observáveis | `observatorio-mandacaru` ativa |
| LegislaGD | Plataforma legislativa; confirmar arquitetura e fluxos no repositório antes de propor novas funções | `legislagd` ativa |
| SAPL-SD | Componente do processo legislativo; verificar estado do fork, dependências e integração com o LegislaGD | Herda contexto `legislagd`, sem Skill autônoma |
| PortalModelo-SD | Componente do portal institucional; verificar interface, integrações e documentação | Herda contexto `legislagd`, sem Skill autônoma |
| e-Cidade-SD | Componente de gestão administrativa e ERP; verificar contratos e limites de integração | Herda contexto `legislagd`, sem Skill autônoma |
| SIGI-SD | Atendimento ao cidadão e protocolos; iniciar levantamento técnico e proposta de Skill dedicada | Apenas `sertaodigital-core`; Skill específica pendente |
| VEREDAS | Mobilidade pública inteligente, escolar e saúde; iniciar documentação e proposta de Skill dedicada | Apenas `sertaodigital-core`; Skill específica pendente |
| Plataforma360 | Gestão integrada; verificar maturidade funcional e fontes de autoridade antes de ativar qualquer Skill | Produto `pending-validation` |
| Notícia Sertaneja | Portal de notícias; validar repositório e maturidade funcional | Produto `pending-validation`, URL não validada |
| Roteiro Comercial | Plataforma comercial; validar repositório e maturidade funcional | Produto `pending-validation`, URL não validada |

## Regras de evolução por produto

1. Ler `AGENTS.md`, a Skill central e a ficha em `products.yaml`; conferir `repositories.yaml`.
2. Para produto com Skill ativa, aplicar a Skill e registrar somente evidências verificadas.
3. Para produto sem Skill dedicada, usar contexto institucional **sem inventar decisões de implementação**; propor Skill em PR separado.
4. Para produto `pending-validation`, validar identidade, repositório, documentação funcional e responsável antes de alterar status.
5. Não adicionar Skills como `active` apenas por constarem nesta lista. O processo formal continua em `knowledge.yaml` e nas políticas de governança.
6. Avançar iterativamente por prioridade; testes e review antes de atualização da `main`; avaliação prática humana depois da implantação automatizada.

## Ordem sugerida de aprofundamento

Observatório Mandacaru → LegislaGD e componentes → SIGI-SD → VEREDAS → Plataforma360 → Notícia Sertaneja → Roteiro Comercial. A ordem é uma **proposta de planejamento**, não uma alteração de prioridade institucional já aprovada.
