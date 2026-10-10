# ADR-010 (PROPOSTO): Engenharia por agentes e adaptadores de descoberta controlada na SDKA

**Data:** 2026-10-09  
**Status:** proposed — pendente de decisão/revisão técnica  
**Issue:** #25

## Contexto

A SDKA já governa conhecimento e interpretação por Skills, com Technical Decision Gate, fonte de verdade por domínio e Functional Bridge read-only. Os projetos API Anything e Replica Skill podem inspirar novas capacidades, mas incorporá-los diretamente ao Core poderia elevar riscos de segurança, manutenção e dependência de fornecedores.

## Alternativas

1. **Fork/copiar integralmente os projetos** — rejeição proposta: acoplamento elevado e necessidade de auditoria extensiva.
2. **Integrar chamadas externas diretamente ao SDKA Core** — rejeição proposta: quebra de separação entre conhecimento e execução.
3. **Skill metodológica neutra + adaptadores opcionais isolados** — recomendação sujeita a aprovação.

## Decisão proposta (não aprovada)

Documentar inicialmente um workflow neutro de reconhecimento, avaliação de lacunas e validação. Qualquer descoberta/execução de operações web ocorrerá em adaptadores futuros isolados, com permissões explícitas por fonte, allowlist de hosts e métodos, logs redigidos e padrão read-only/dry-run. `sources.yaml` continuará como registro de autoridade; o contrato de operação apenas o referencia.

## Consequências esperadas

**Benefícios:** reutilização entre produtos, evidências auditáveis, adaptação a diferentes agentes e menor acoplamento.

**Custos/riscos:** manutenção de adaptadores, mudanças de endpoints, políticas de terceiros, LGPD, SSRF e vazamento de credenciais. Necessários revisão de licenças, testes de segurança, limitação de taxa, isolamento de rede e aprovação operacional.

## Verificações obrigatórias antes de aprovação

- [ ] Revisar códigos e licenças dos projetos externos em commits fixados.
- [ ] Validar `AGENTS.md`, `docs/SDKA.md`, `docs/SOURCE_OF_TRUTH.md`, ADRs e schemas atuais.
- [ ] Demonstrar ausência de duplicação com Functional Bridge e Skills existentes.
- [ ] Definir política de autorização por fonte, redaction, retenção e auditoria.
- [ ] Aprovar contrato de operações e definir runtime isolado.
- [ ] Validar interoperabilidade de agentes.
- [ ] Realizar piloto em dados autorizados e documentar resultados.

## Impacto cruzado

- **GitHub:** documentação técnica, Skills e futuro código de adaptadores somente após aprovação.
- **Drive:** nenhuma mudança funcional presumida nesta fase; abrir handoff se futuro piloto modificar processos ou requisitos.
- **Produtos:** sem alteração operacional nesta proposta.
