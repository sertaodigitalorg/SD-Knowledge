# SDKA — Fase 11.2: evidências verificadas por inspeção de árvore Git

**Estado:** levantamento estático inicial; não equivale a teste executado ou homologação.

## Fonte e método

Consulta de árvores Git na branch `main`, seguida de identificação de arquivos de implementação e teste. Commits de referência: SIGI-SD `97a42851dbf1ca46ccd7595585f8e1460bc71a5d`; VEREDAS workspace `ef598eddc42d6e33810d3c1b37bf77f98b2f8039`; VEREDAS-Core `f9205cda0c0ae050ce0eff64595fa96b11151d08`; VEREDAS-Edge `a7508ceb676f6997caacb10d87215d6aa9f9c06f`; VEREDAS-PWA `15a8019da8766220a0bcc701556196b6a098aaa2`.

## Inventário de evidências localizadas

| Produto | Arquivo observado na árvore | O que demonstra | O que ainda não demonstra |
| --- | --- | --- | --- |
| SIGI-SD | `apps/backend-symfony/src/Controller/Admin/Integration/Chatwoot/ChatwootWebhookController.php` | Existe controlador dedicado a webhook | Autenticidade, idempotência e execução segura |
| SIGI-SD | `apps/backend-symfony/src/Command/SyncChatwootConversationsCommand.php` | Existe comando de sincronização | Sucesso de sincronização real |
| SIGI-SD | `apps/backend-symfony/src/Controller/Admin/AttendanceProtocolController.php` | Existe controlador de protocolos | Atendimento funcional em produção |
| VEREDAS-Core | `apps/core-web/src/Api/Controller/SyncController.php` | Existe controlador de sincronização | Reconciliação segura |
| VEREDAS-Core | `apps/core-web/src/Entity/SyncEvent.php` | Existe entidade de evento | Garantia de persistência |
| VEREDAS-Edge | `docs/sincronizacao/contracts/sync-event.schema.json` | Existe contrato de evento documentado | Validação em runtime |
| VEREDAS-PWA | `projects/pwa-shell/src/lib/pwa-shell.spec.ts` | Existe teste unitário versionado | Cobertura de toda a operação offline |

## Contrato mínimo de evidência para próximas análises

Para cada constatação registrar `repository`, `commit`, `path`, `claim`, `verification_level` e `limitations`. Níveis admitidos: `tree_observed`, `content_reviewed`, `test_executed`. A Fase 11.2 começa exclusivamente com `tree_observed` e evoluirá mediante leitura controlada de conteúdo e execução de testes CI.

## Próximos gates

1. Conferir conteúdo dos controladores e contratos listados e registrar resultado de leitura.
2. Executar análise automatizada com fixtures não sensíveis e rejeição de referências inválidas.
3. Validar cada evolução no CI, sem ativar as Skills `sigi-sd` e `veredas` antes de aprovação em PR específico.
4. Preservar a avaliação prática de colaboradores para depois da implantação automatizada.
