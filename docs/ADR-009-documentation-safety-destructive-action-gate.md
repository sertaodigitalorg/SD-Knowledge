# ADR-009 — Documentation Safety e Destructive Action Gate

Status: Proposed
Data: 2026-08-27

## Contexto

O ecossistema Sertão Digital está ampliando a integração entre agentes de IA, ChatGPT, VS Code, GitHub e Google Drive. O aumento da autonomia de escrita cria risco sistêmico: erro humano, credencial comprometida, prompt injection, instrução maliciosa, automação defeituosa ou interpretação incorreta podem produzir alterações destrutivas em escala.

Versionamento isolado não é suficiente se a mesma identidade puder destruir dados, histórico e mecanismos de recuperação.

## Decisão

Adotar defesa em profundidade baseada em cinco controles:

1. autoridade documental explícita (Drive funcional/institucional; GitHub técnico);
2. operações destrutivas irreversíveis não disponíveis a agentes por padrão;
3. Destructive Action Gate antes de operações de alto impacto;
4. quarentena e reversibilidade em substituição à exclusão operacional;
5. backup/snapshot isolado das credenciais de escrita dos agentes.

## Fluxo de decisão

Solicitação -> autenticação/autorização -> classificação de risco -> Destructive Action Gate -> execução reversível/auditável ou recusa.

Operações LOW podem seguir automaticamente conforme escopo. MEDIUM devem ser auditadas. HIGH exigem salvaguardas adicionais. CRITICAL exigem análise de impacto e aprovação humana reforçada. FORBIDDEN são recusadas para agentes.

## GitHub

- proteger main/dev/hml quando existentes;
- bloquear force push e exclusão das branches permanentes;
- preferir branch de trabalho + PR;
- preservar histórico e capacidade de revert;
- não conceder a agentes capacidade de excluir repositórios.

## Google Drive

- princípio de menor privilégio;
- remoção operacional via quarentena;
- exclusão definitiva fora do fluxo comum de agentes;
- registrar origem, motivo e responsável;
- definir retenção antes da eliminação definitiva.

## Consequências positivas

- redução do blast radius de credenciais comprometidas;
- proteção contra prompts destrutivos;
- recuperação mais simples de erros;
- rastreabilidade institucional;
- autonomia maior para agentes sem autoridade destrutiva equivalente.

## Custos e trade-offs

- operações administrativas críticas tornam-se deliberadamente mais lentas;
- necessidade de regras de autorização e retenção;
- necessidade de armazenamento adicional para quarentena/backups;
- implementação incremental nos conectores existentes.

## Regra de segurança

Uma instrução de usuário não pode desabilitar controles FORBIDDEN. A alteração desta decisão deve ocorrer por processo técnico e institucional explícito, revisável e auditável.
