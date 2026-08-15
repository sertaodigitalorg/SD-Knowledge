# Skills

Camada de interpretação e conhecimento de domínios do Sertão Digital.

## O que é uma Skill?

Uma Skill encapsula:

- **Contexto de domínio** — conceitos, vocabulário, padrões
- **Regras de interpretação** — como agentes devem entender referências
- **Dependências** — outras Skills e fontes necessárias
- **Workflows** — processos padrão para mudanças

## Skills Disponíveis

### sertaodigital-core

**Contexto:** Institucional e Arquitetural  
**Status:** ✅ Active  
**Propósito:** Base de conhecimento para todo ecossistema Sertão Digital

Fornece contexto sobre:
- Organização e governança
- Princípios de software livre
- Arquitetura técnica
- Documentação e fontes

**Quando usar:** Sempre — é a base para todas as outras Skills.

[Ler SKILL.md](sertaodigital-core/SKILL.md)

### legislagd

**Contexto:** Plataforma Legislativa  
**Status:** ✅ Active  
**Propósito:** Contexto específico da plataforma LegislaGD

Fornece contexto sobre:
- Processo legislativo
- Arquitetura de LegislaGD
- Integração de componentes (SAPL-SD, SIGI-SD, etc)
- Identidade centralizada (Keycloak)
- Workflows de desenvolvimento

**Quando usar:** Ao trabalhar em LegislaGD ou componentes relacionados.

[Ler SKILL.md](legislagd/SKILL.md)

## Estrutura de uma Skill

```
[skill-name]/
├── SKILL.md              # Especificação principal
├── references/           # Conteúdo de domínio
│   ├── topic1.md
│   ├── topic2.md
│   └── ...
├── manifests/            # Registros estruturados (YAML)
│   ├── product.yaml
│   ├── repositories.yaml
│   └── sources.yaml
└── workflows/            # Processos padrão
    ├── process1.md
    ├── process2.md
    └── ...
```

## Como Usar uma Skill

### Para Agentes de IA

1. Identifique a Skill relevante para sua tarefa
2. Carregue `[skill-name]/SKILL.md` para especificação
3. Consulte `references/` para tópicos específicos
4. Respeite hierarquia em `docs/SOURCE_OF_TRUTH.md`
5. Use manifestos para contexto estruturado

Exemplo:
```
Trabalhando em LegislaGD? → Carregue legislagd/SKILL.md
Questão sobre organização? → Consulte sertaodigital-core/SKILL.md
```

### Para Desenvolvedores

1. Leia a Skill relevante para seu domínio
2. Conheça os conceitos em `references/`
3. Siga os workflows em `workflows/`
4. Consulte os manifestos para informações estruturadas
5. Respeite as dependências documentadas

### Para Documentadores

1. Identifique a qual Skill sua documentação pertence
2. Adicione em `references/` com tópico bem definido
3. Link para outras referências quando apropriado
4. Mantenha coerência com SKILL.md

## Criar uma Nova Skill

Veja [docs/SKILL_ARCHITECTURE.md](../docs/SKILL_ARCHITECTURE.md) para instruções completas.

Resumo:

1. Verificar necessidade (qual domínio?)
2. Criar estrutura de diretórios
3. Escrever SKILL.md
4. Documentar em references/
5. Criar manifestos
6. Registrar em knowledge.yaml
7. Abrir PR

## Manutenção

Skills devem ser revisadas:

- [ ] Conteúdo ainda está correto?
- [ ] Há conflitos com outras Skills?
- [ ] Dependências mudaram?
- [ ] Nova documentação disponível?
- [ ] Atualizar VERSION quando necessário

## Dependências Entre Skills

```
sertaodigital-core (Base)
    ↓
    └→ legislagd (Plataforma Legislativa)
    └→ [Outras Skills de produto]
```

Toda Skill (exceto sertaodigital-core) depende de contexto base.

## Convenção de Nomenclatura

- Skill names em kebab-case: `meu-skill`, `novo-produto-sd`
- Referências em snake_case: `topic_name.md`
- Manifestos em snake_case: `product.yaml`, `repositories.yaml`

## Mais Informações

- [Especificação SDKA](../docs/SDKA.md)
- [Arquitetura de Skills](../docs/SKILL_ARCHITECTURE.md)
- [Source of Truth](../docs/SOURCE_OF_TRUTH.md)
