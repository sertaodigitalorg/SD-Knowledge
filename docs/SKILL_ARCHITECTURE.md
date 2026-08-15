# Skill Architecture

Como criar, estruturar e manter uma Skill.

---

## O que é uma Skill?

Uma **Skill** é a camada de interpretação que encapsula:

- **Contexto de domínio** — conhecimento específico
- **Regras de interpretação** — como agentes devem entender referências
- **Dependências** — outras Skills e fontes necessárias
- **Workflows** — processos padrão para mudanças

**Exemplo:** `legislagd` Skill fornece contexto sobre a plataforma legislativa.

---

## Estrutura de uma Skill

```
skills/[skill-name]/
├── SKILL.md                 # Especificação principal
├── references/              # Conteúdo de domínio
│   ├── topic1.md
│   ├── topic2.md
│   └── ...
├── manifests/               # Registros estruturados
│   ├── product.yaml         # Info de produto
│   ├── repositories.yaml    # Repositórios relacionados
│   └── sources.yaml         # Fontes/autoridades
└── workflows/               # Processos padrão
    ├── process1.md
    ├── process2.md
    └── ...
```

---

## SKILL.md (Especificação)

Cabeçalho:

```yaml
---
name: skill-name
description: Breve descrição
version: 1.0.0
status: active | inactive | deprecated
type: organizational-context | product-context | domain-context | technical-context
---
```

Seções obrigatórias:

1. **Propósito** — O que a Skill fornece
2. **Escopo** — O que entra e o que não entra
3. **Quando Usar** — Use quando... / Não use quando...
4. **Fontes de Autoridade** — Onde vem a verdade
5. **Hierarquia de Autoridade** — Como resolver conflitos
6. **Dependências** — Outras Skills/fontes necessárias
7. **Como Usar** — Para agentes, desenvolvedores, documentadores

Seções opcionais (conforme relevante):

- Conceitos principais
- Padrões técnicos
- Integração
- Segurança/privacidade
- Versionamento

---

## references/ (Conteúdo)

Documentação de tópicos específicos.

Estrutura:

```
references/
├── concept1.md       # Conceitos principais
├── architecture.md   # Arquitetura (se relevante)
├── integrations.md   # Integrações (se relevante)
├── security.md       # Segurança (se relevante)
└── [other].md        # Tópicos do domínio
```

Cada arquivo:

- Tópico singular e bem definido
- Markdown bem estruturado
- Links para outras referências na Skill
- Acessível para agentes de IA

---

## manifests/ (Estruturado)

Registros legíveis por máquina.

### product.yaml

Se Skill é de produto:

```yaml
name: product-name
version: 1.0.0
status: active | pending | deprecated

product:
  name: Nome do Produto
  description: Descrição
  type: platform | component | infrastructure
  
components:
  - name: Componente 1
    description: O que faz
    repository: URL ou null
    
dependencies:
  required:
    - sertaodigital-core
  conditional:
    domain-name:
      when:
        - situação 1
        - situação 2
```

### repositories.yaml

Repositórios relacionados:

```yaml
repositories:
  repo-key:
    name: Nome do Repositório
    url: https://github.com/...
    status: active | pending-validation | deprecated
    description: O que é
```

### sources.yaml

Fontes de autoridade:

```yaml
sources:
  source-key:
    name: Nome da Fonte
    type: google-drive | github | web | other
    authority: primary | secondary | reference
    status: active | archived
    description: O que contém
```

---

## workflows/ (Processos)

Procedimentos padrão para o domínio.

Exemplos:

- `new-feature.md` — Como adicionar funcionalidade
- `bug-fix.md` — Como corrigir bug
- `integration-change.md` — Como integrar com outro componente
- `architecture-change.md` — Como fazer mudança arquitetural
- `documentation-update.md` — Como atualizar documentação

Cada workflow descreve:

1. **Gatilho** — Quando usar este workflow
2. **Pré-requisitos** — O que é necessário
3. **Passos** — Procedimento passo a passo
4. **Validação** — Como confirmar conclusão
5. **Referências** — Links e recursos

---

## Como Criar uma Nova Skill

### Passo 1: Verificar Necessidade

```
- Existe Skill? Não → Continuar
- Tipo de Skill?
  - Contexto institucional? → Estenda sertaodigital-core
  - Novo produto? → Crie product-context Skill
  - Novo domínio técnico? → Crie domain-context Skill
- Dependências? → Liste Skills necessárias
```

### Passo 2: Estrutura

```bash
mkdir -p skills/[skill-name]/{references,manifests,workflows}
touch skills/[skill-name]/SKILL.md
```

### Passo 3: SKILL.md

Escrever especificação principal com metadados.

### Passo 4: references/

Documentar tópicos de domínio.

### Passo 5: manifests/

Criar product.yaml, repositories.yaml, sources.yaml conforme aplicável.

### Passo 6: workflows/

Documentar processos padrão de trabalho.

### Passo 7: Registrar em knowledge.yaml

```yaml
- name: new-skill
  type: product-context
  status: active
  description: "Descrição"
  location: skills/new-skill/
  depends_on:
    - sertaodigital-core
```

### Passo 8: Pull Request

- Title: `feat: add [skill-name] skill`
- Description: Propósito, escopo, dependências
- Checklist: Validação concluída?

---

## Versionamento de Skills

Semantic Versioning:

- **1.0.0** — Skill inicial, estável
- **1.1.0** — Nova seção de referência adicionada (compatível)
- **1.0.1** — Correção de typo ou esclarecimento
- **2.0.0** — Quebra de compatibilidade (raro)

Atualizar VERSION em SKILL.md.

---

## Manutenção de Skills

### Review Periódico

- [ ] Conteúdo ainda está correto?
- [ ] Há conflitos com outras Skills?
- [ ] Novas dependências surgiram?
- [ ] Há issues relacionadas?

### Quando Atualizar

- [ ] Mudança em fonte de autoridade (Drive)
- [ ] Nova documentação de referência
- [ ] Mudança arquitetural
- [ ] Resolução de conflitos

### Deprecação

Se Skill não é mais usada:

```yaml
status: deprecated
deprecation_reason: "Motivo"
successor_skill: "Nome da Skill substituta, se houver"
```

---

## Dicas

- ✅ Mantenha Skill focada em seu domínio
- ✅ Referencie outras Skills quando apropriado
- ✅ Use manifests para dados estruturados
- ✅ Workflows devem ser acionáveis
- ✅ Links internos/externos claros
- ✅ Valide contra SOURCE_OF_TRUTH.md
- ✅ Mantenha compatibilidade quando possível
- ❌ Não duplique conteúdo entre Skills
- ❌ Não invente informação funcional
- ❌ Não misture conceitos de múltiplos domínios

---

**Versão:** 1.0.0  
**Última atualização:** 2026-08-15
