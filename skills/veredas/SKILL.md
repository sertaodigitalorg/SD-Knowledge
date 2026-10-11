# Skill: veredas — contexto inicial (não ativado)

## Metadados
- **Name:** veredas
- **Type:** product-context
- **Status:** inactive
- **Produto:** VEREDAS
- **Dependência prevista:** sertaodigital-core
- **Registro do produto:** `products.yaml → products.veredas`

## Propósito
Preparar a orientação institucional inicial do produto **VEREDAS** (mobilidade pública inteligente para transporte escolar e saúde) sem assumir características ou funcionalidades ainda não verificadas no código.

## Fontes de autoridade
1. `AGENTS.md` e `skills/sertaodigital-core/SKILL.md`.
2. `products.yaml`, `repositories.yaml` e `knowledge.yaml` para estado cadastral.
3. Documentação funcional aprovada no Drive para requisitos e processos.
4. Repositório `sertaodigitalorg/VEREDAS` para evidência técnica, após confirmação dos artefatos.

## Protocolo de descoberta e evolução
1. Validar repositório, branch de referência, documentação e testes existentes.
2. Classificar informações em **verificado**, **declarado no catálogo**, **proposto** ou **pendente de confirmação**.
3. Produzir inventário de módulos, integrações, fluxos e lacunas somente com evidências citáveis.
4. Abrir issue/ADR/PR segundo política vigente; executar Cross-Layer Impact Check quando aplicável.
5. Propor ativação em `knowledge.yaml` apenas após revisão de responsáveis e documentação mínima.

## Restrições
- Esta Skill **não está ativa** e não poderá ser carregada como autoridade de produto pelo roteador atual.
- Não inferir implementação a partir da descrição do catálogo ou do roadmap.
- Não acessar dados de cidadãos, estudantes, pacientes ou credenciais sem autorização e necessidade demonstrada.
- Não executar mudanças em produção, deploy ou integrações externas.

## Próxima ação
Auditar o repositório e a documentação aprovada do produto para elaborar a primeira versão técnica verificável desta Skill.

## Evidência técnica inicial (README do repositório, não teste de execução)

O workspace documenta três componentes em repositórios/submódulos independentes: `VEREDAS-Core` (Symfony, Angular administrativo, PostgreSQL, Redis, MQTT), `VEREDAS-Edge` (API local, MQTT, SQLite) e `VEREDAS-PWA` (Angular/PWA para aluno, motorista, monitor e paciente). A documentação declara priorização `edge-first` e fallback para o Core e manutenção dos componentes por submódulos Git. Isso descreve a arquitetura documentada; **não** comprova fluxos offline, sincronização, PNATE ou integração SETE em produção.

**Próxima revisão:** conferir `docs/arquitetura-geral.md`, `docs/cenarios-teste.md`, Core/Edge/PWA e evidências de sincronização offline, segurança, RFID e transporte escolar/saúde antes de afirmar cobertura de requisitos.

## Auditoria documental complementar — VEREDAS

Fontes lidas: `sertaodigitalorg/VEREDAS/docs/arquitetura-geral.md` e `docs/cenarios-teste.md`.

**Documentado:** o Core detém o cadastro mestre e governança; Edge recebe carga operacional e deve persistir eventos localmente; PWA possui perfis operacionais. A documentação descreve sincronização posterior e roteiros de teste de educação, saúde, gestão de rotas e páginas públicas.

**Critérios antes da ativação:** verificar código e testes para persistência SQLite, reconciliação sem duplicidade, transições offline/online, segurança e segregação de dados; executar cenários de educação/saúde em ambiente controlado. O documento de cenários é um roteiro, não resultado de testes.
