# Exemplo: AGENTS.md com Contexto

Como usar AGENTS.md em um projeto específico.

---

## Exemplo 1: Trabalhando em LegislaGD

```yaml
# Seu arquivo de inicialização para agentes

environment:
  project: LegislaGD
  domain: legislative-platform
  
skills:
  - sertaodigital-core      # Sempre carregar base
  - legislagd                # Contexto legislativo
  
task:
  type: feature-development
  description: |
    Você está desenvolvendo um novo feature para LegislaGD.
    
    Antes de começar:
    1. Carregue skills listadas acima
    2. Consulte docs/SOURCE_OF_TRUTH.md
    3. Valide decisões contra Google Drive (master)
    4. Respeite arquitetura em skills/legislagd/references/architecture.md
    5. Não invente informações — sempre cite fontes
```

## Exemplo 2: Questão Sobre Organização Sertão Digital

```yaml
environment:
  project: Sertão Digital
  domain: institutional
  
skills:
  - sertaodigital-core      # Contexto completo
  
task:
  type: research
  description: |
    Responda questões sobre a organização, arquitetura ou governança.
    
    Processo:
    1. Carregue sertaodigital-core/SKILL.md
    2. Consulte references/ para tópico específico
    3. Valide contra Google Drive (Acervo Institucional)
    4. Se conflito: aplicar hierarquia em SOURCE_OF_TRUTH.md
    5. Citar fonte sempre
```

## Exemplo 3: Documentação de Novo Produto

```yaml
environment:
  project: Novo Produto SD
  domain: product-documentation
  
skills:
  - sertaodigital-core      # Base institucional
  
task:
  type: documentation
  description: |
    Você está documentando um novo produto/componente.
    
    Checklist:
    1. Crie Skill em skills/[produto]/SKILL.md
    2. Documente domínio em references/
    3. Crie manifestos (product.yaml, repositories.yaml)
    4. Registre em knowledge.yaml
    5. Abra PR com contexto completo
    
  references:
    - docs/SKILL_ARCHITECTURE.md
    - docs/PRODUCT_KNOWLEDGE_STANDARD.md
    - docs/SOURCE_OF_TRUTH.md
```

## Como Usar Este Exemplo

1. Copie a estrutura apropriada para seu contexto
2. Customize `skills` e `task` conforme necessário
3. Passe para o agente antes de começar
4. O agente carregará contexto automáticamente

## Mais Exemplos

Veja outros exemplos:
- [knowledge.example.yaml](knowledge.example.yaml) — Estrutura de índice
- [product.example.yaml](product.example.yaml) — Manifesto de produto
