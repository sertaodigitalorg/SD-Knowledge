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
