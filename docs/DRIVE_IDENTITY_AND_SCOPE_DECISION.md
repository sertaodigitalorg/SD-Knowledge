# Drive Identity and Scope Decision

Status: REQUIRED BEFORE PRODUCTION WRITE
Data: 2026-08-27

## Contexto

A auditoria da Fase C confirmou que o conector Google Drive atualmente disponível ao agente está autenticado por uma conta pessoal e possui capacidade técnica de escrita. A raiz funcional `33_BASE_DE_CONHECIMENTO_E_SKILLS` está em My Drive (`driveId = null`), e não há Shared Drives acessíveis pela identidade atual.

Essa configuração é inadequada para habilitar escrita institucional de produção do SDKA Functional Bridge.

## Decisão

A escrita institucional do SDKA deve usar uma identidade dedicada e separada das contas pessoais de administradores.

A arquitetura alvo é:

- `SDKA-READER`: leitura/busca no subtree funcional autorizado;
- `SDKA-WRITER`: criação/atualização limitada após Drive Safety Gate;
- `SDKA-QUARANTINE`: move/restauração na `QUARENTENA_DOCUMENTAL`, sem purge;
- `SDKA-BACKUP`: identidade separada, sem uso por agentes operacionais;
- `ADMIN-HUMAN`: administração de permissões, purge excepcional e recuperação.

## Regras de menor privilégio

1. nenhuma identidade operacional deve ser proprietária do acervo;
2. nenhuma identidade operacional deve possuir permissão para administrar compartilhamentos globalmente;
3. delete/purge permanente não deve ser concedido ao agente comum;
4. a raiz autorizada deve ser explicitamente configurada por `FUNCTIONAL_ROOT_FOLDER_ID`;
5. tokens e secrets não devem ser versionados no Git;
6. scopes OAuth devem ser os mínimos necessários para as operações liberadas;
7. toda escrita deve passar pelo Drive Safety Gate;
8. backup/restauração deve usar domínio de credencial separado da escrita operacional.

## Shared Drive

Quando houver Google Workspace compatível, recomenda-se migrar a autoridade funcional para Shared Drive institucional. Isso reduz dependência de propriedade individual e melhora continuidade administrativa.

A migração para Shared Drive deve ocorrer como projeto controlado, com inventário, teste de permissões, validação de links e plano de rollback. Não mover o acervo inteiro automaticamente.

## Scopes

Os scopes OAuth exatos da integração atual não são visíveis pelo conector. Portanto, a política exige validação no Google Cloud / provedor OAuth antes de qualquer go-live.

A seleção de scopes deve privilegiar menor privilégio e evitar escopos globais amplos quando uma operação mais restrita for suficiente.

## Go-live

Enquanto a identidade institucional e os scopes mínimos não estiverem implementados e validados:

`FUNCTIONAL BRIDGE PRODUCTION WRITE = BLOCKED`
