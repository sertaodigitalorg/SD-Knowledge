# SAPL-SD

Sistema de Acompanhamento de Processo Legislativo - Versão Sertão Digital.

## Informações Rápidas

| Campo | Valor |
|---|---|
| **Nome Completo** | Sistema de Acompanhamento de Processo Legislativo |
| **Acrônimo** | SAPL |
| **Versão SD** | SAPL-SD |
| **Upstream** | <https://github.com/interlegis/sapl> |
| **Manutenção** | Compatibilidade com upstream |
| **Função** | Core de processo legislativo |

## Responsabilidades

- ✅ Gerenciar proposições (PL, emendas, etc)
- ✅ Controlar sessões (plenário, comissões)
- ✅ Registrar votações
- ✅ Manter histórico legislativo
- ✅ Gerenciar parlamentares
- ✅ API pública de consulta

## Integra com

- PortalModelo-SD (publicação)
- SIGI-SD (protocolo ↔ proposição)
- e-Cidade-SD (dados de parlamentar)
- Keycloak (autenticação)

## Tecnologias

- Backend: Python (Django upstream)
- Banco de dados: PostgreSQL
- Frontend: Pode variar (verifique repositório)
- Containerização: Docker

## Repositório

Consulte `repositories.yaml` para a URL canônica e o status validado do repositório.
## Mais Informações

Veja `skills/legislagd/references/domain.md` para conceitos legislativos.
