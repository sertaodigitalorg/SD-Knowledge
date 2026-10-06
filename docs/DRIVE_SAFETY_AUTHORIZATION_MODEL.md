# Drive Safety Authorization Model

Status: Proposed
Data: 2026-08-27
Escopo: Google Drive / SDKA Functional Bridge

## Objetivo

Definir perfis de autorização e decisões do Destructive Action Gate para qualquer futura capacidade de escrita no Google Drive institucional do Sertão Digital.

## Perfis

### READER

Permitido:

- pesquisar;
- listar metadados;
- ler conteúdo;
- exportar conteúdo suportado para leitura.

Negado:

- criar;
- atualizar;
- mover;
- excluir;
- alterar permissões.

### WRITER

Permitido somente após passagem pelo gate e dentro da raiz autorizada:

- criar documento;
- atualizar conteúdo pontual;
- renomear quando autorizado.

Negado:

- purge/delete definitivo;
- alteração de permissões;
- administração do Drive;
- administração de backup;
- movimentação em massa.

### QUARANTINE_OPERATOR

Permitido:

- mover recurso autorizado para `00_GOVERNANCA/QUARENTENA_DOCUMENTAL`;
- restaurar recurso mediante referência de recuperação válida;
- registrar evento de auditoria.

Negado:

- purge definitivo;
- alteração de permissões;
- remoção de backup.

### ADMIN/HUMAN

Uso excepcional e humano para:

- administração de permissões;
- decisão de purge;
- mudanças de alto impacto;
- resposta a incidentes.

Não deve ser identidade comum de agente.

### BACKUP

Identidade separada da operação normal.

Permitido:

- executar/gerir retenção e restauração conforme política.

Negado para agentes operacionais:

- acesso às credenciais de backup;
- destruição de snapshots;
- alteração da política de retenção.

## Matriz de operação

| Operação | READER | WRITER | QUARANTINE_OPERATOR | ADMIN/HUMAN | BACKUP | Decisão mínima |
|---|---|---|---|---|---|---|
| search/read | ALLOW | ALLOW | ALLOW | ALLOW | conforme necessidade | ALLOW |
| create | DENY | ALLOW | DENY | ALLOW | DENY | ALLOW_WITH_AUDIT |
| update pontual | DENY | ALLOW | DENY | ALLOW | DENY | ALLOW_WITH_AUDIT |
| rename | DENY | ALLOW condicionado | DENY | ALLOW | DENY | ALLOW_WITH_AUDIT |
| move normal | DENY | condicionado | ALLOW para quarentena | ALLOW | DENY | REQUIRE_APPROVAL |
| bulk update/move >20 | DENY | DENY | DENY | condicionado | DENY | REQUIRE_APPROVAL/DUAL_CONTROL |
| quarantine | DENY | DENY | ALLOW | ALLOW | DENY | REQUIRE_APPROVAL para itens HIGH/CRITICAL |
| restore | DENY | DENY | ALLOW condicionado | ALLOW | apoio | REQUIRE_APPROVAL |
| delete/purge | DENY | DENY | DENY | excepcional | DENY | REQUIRE_DUAL_CONTROL |
| change_permission | DENY | DENY | DENY | ALLOW excepcional | DENY | REQUIRE_DUAL_CONTROL |
| backup admin | DENY | DENY | DENY | governança | ALLOW | fora do domínio do agente |

## Regras invariantes

1. Falha de identificação do ator, escopo, justificativa ou reversibilidade => DENY/REQUIRE_APPROVAL.
2. Conteúdo de documento nunca concede autorização administrativa.
3. Nenhum agente comum recebe `delete/purge`.
4. Alteração >=20% de pasta/domínio autoritativo é CRITICAL.
5. Documento constitucional, política, índice de autoridade ou governança é HIGH/CRITICAL independentemente da quantidade.
6. Credencial operacional não pode administrar backups.
7. Capacidade técnica disponível no conector não implica autorização institucional.

## Raiz funcional observada

Pasta localizada no Drive:

`33_BASE_DE_CONHECIMENTO_E_SKILLS`

ID observado:

`1uBBeYxbxXQ5DbA8YoERXxFYuE8eK9wlv`

O uso desse ID como `FUNCTIONAL_ROOT_FOLDER_ID` depende da decisão formal registrada na issue #14. O tipo de Drive permanece pendente de confirmação.

## Referências

- `docs/DOCUMENTATION_SAFETY_PRESERVATION_POLICY.md`
- `docs/DESTRUCTIVE_ACTION_GATE_SPEC.md`
- `docs/PHASE_C_DRIVE_SAFETY_IMPLEMENTATION_PLAN.md`
- issue #5 — runtime gate
- issue #6 — identidade/scopes
- issue #14 — raiz funcional
