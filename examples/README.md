# Exemplos

Exemplos de como criar e usar Skills, manifestos e contexto.

## AGENTS.example.md

Exemplo de como instruir um agente.

```yaml
# Seu arquivo de contexto
skills:
  - sertaodigital-core
  - legislagd

task: |
  Você está trabalhando em um novo feature para LegislaGD.
  Carregue as Skills listadas acima antes de começar.
```

Veja [AGENTS.example.md](AGENTS.example.md).

## knowledge.example.yaml

Exemplo de como estruturar um knowledge.yaml.

Veja [knowledge.example.yaml](knowledge.example.yaml).

## product.example.yaml

Exemplo de como criar um manifesto de produto.

Veja [product.example.yaml](product.example.yaml).

## Criar Seu Próprio Exemplo

Se você quer contribuir com exemplos:

1. Crie arquivo `[seu-exemplo].md` ou `[seu-exemplo].yaml`
2. Documente com comentários
3. Adicione descrição neste README
4. Abra PR

---

Leia a documentação correspondente para entender cada exemplo:
- Manifestos: [docs/SDKA.md](../docs/SDKA.md)
- Skills: [docs/SKILL_ARCHITECTURE.md](../docs/SKILL_ARCHITECTURE.md)
- Agentes: [AGENTS.md](../AGENTS.md)
