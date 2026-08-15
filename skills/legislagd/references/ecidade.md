# e-Cidade-SD

Sistema ERP para Gestão Administrativa Legislativa (e futuramente Executiva).

## Informações Rápidas

| Campo | Valor |
|---|---|
| **Nome Completo** | e-Cidade-SD |
| **Escopo Atual** | Legislativo |
| **Função** | ERP administrativo-financeiro |
| **Upstream** | Software Livre (Brasil) |

## Responsabilidades

- ✅ Gestão de RH
- ✅ Folha de pagamento
- ✅ Gestão administrativo-financeira
- ✅ Patrimônio
- ✅ Compras e licitações (opcional)
- ✅ Contabilidade

## Dados Legislativos Utilizados

- Parlamentares (importação)
- Mandatos (calendário legislativo)
- Afastamentos (licenças, férias)
- Alocação de recursos por gabinete

## Integra com

- SAPL-SD (dados de parlamentar)
- SIGI-SD (dados de staff)
- Keycloak (autenticação)
- Contabilidade integrada

## Tecnologias

- Backend: Verificar repositório
- Banco de dados: PostgreSQL
- Containerização: Docker

## Repositório

Consulte `repositories.yaml` para a URL canônica e o status validado do repositório.
## Importante

- Contém dados sensíveis (folha, patrimonial)
- Acesso restrito via RBAC
- Auditoria completa de transações
- Backup e recuperação críticos
