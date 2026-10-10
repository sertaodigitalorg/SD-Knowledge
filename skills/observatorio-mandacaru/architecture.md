# Arquitetura — Observatório Mandacaru

## Estado presente verificado no repositório

- Symfony 8.1 e PHP >= 8.4 no backend; API REST e administração Twig.
- Angular 22 no portal público/área autenticada.
- Doctrine ORM/Migrations; PostgreSQL 17 no Compose da raiz.
- Docker Compose, Traefik 3.7.1 e Meilisearch 1.12 declarados.
- Login por sessão, papéis e workflow editorial no backend.
- Busca atualmente combina endpoints públicos no cliente. Meilisearch não tem indexador/Search API funcional verificada.

O Compose em `backend/` é scaffold legado com PostgreSQL 16; o Compose raiz é o ambiente local documentado. Verifique a fonte usada antes de descrever ambiente ou versão.

## Alvos/decisões

- Busca: PostgreSQL → indexador backend → Meilisearch → Search API → Angular.
- Integração sistema↔sistema por REST.
- MCP para IA↔ecossistema é alvo funcional; deve chamar APIs/serviços de domínio, nunca SQL direto.
- Serviços de IA, vector DB, grafo, ETL, Redis/Kestra dedicado e BI não estão implantados no código analisado.
- Nenhuma tecnologia ou fornecedor de IA é selecionado por esta referência.

Decisões existentes podem não ter rationale histórico documentado. Consulte `references/decisions.md`; não crie justificativas retroativas.

## Governança

Mudança arquitetural exige Technical Decision Gate, análise de compatibilidade/segurança e Cross-Layer Impact Check. Registre ADR quando a decisão e seu rationale forem verificáveis. Segredos do Meilisearch não podem ir ao frontend.
