#!/usr/bin/env python3
"""Classificacao conservadora de intencao e roteiro orientado SDKA, offline."""
import argparse
import json
from sdka_skill_discovery import discover, normalize

SIGNALS = {
    "bugfix": ("corrigir", "correcao", "erro", "bug", "falha", "defeito"),
    "feature": ("implementar", "criar funcionalidade", "nova funcionalidade", "desenvolver funcionalidade"),
    "documentation": ("documentar", "documentacao", "atualizar documento", "readme"),
    "architecture": ("arquitetura", "adr", "refatoracao arquitetural"),
    "learning": ("aprender", "estudar", "entender", "conhecer", "sou novo"),
    "testing": ("testar", "teste", "testes", "validar"),
}
STEPS = {
    "bugfix": ["Reproduzir e registrar o defeito sem expor dados", "Localizar codigo e testes com a Skill do produto", "Criar correcao minima em branch permitida", "Executar testes e registrar evidencia em PR"],
    "feature": ["Verificar requisito e MASTER funcional", "Definir criterio de aceite e impactos", "Implementar em branch permitida", "Testar, documentar e abrir PR"],
    "documentation": ["Verificar MASTER do dominio antes de editar", "Atualizar somente a camada autorizada", "Revisar links e consistencia", "Solicitar revisao da alteracao"],
    "architecture": ["Ler ADRs e decisoes existentes", "Mapear impactos tecnicos e funcionais", "Propor ADR/issue antes de consolidar", "Solicitar revisao de arquitetura"],
    "learning": ["Carregar AGENTS.md e Skill central", "Ler a Skill do produto e sua documentacao", "Executar exercicio sem alterar producao", "Solicitar revisao do entendimento"],
    "testing": ["Identificar comportamento esperado na fonte MASTER", "Selecionar testes existentes", "Executar apenas no ambiente autorizado", "Registrar resultados e lacunas"],
}
def classify(request):
    tokens = " " + normalize(request) + " "
    matches = [kind for kind, patterns in SIGNALS.items()
               if any(" " + normalize(pattern) + " " in tokens for pattern in patterns)]
    if not matches:
        return "unspecified"
    if len(matches) > 1:
        # Learning context does not override a concrete work request.
        concrete = [item for item in matches if item != "learning"]
        if len(concrete) == 1:
            return concrete[0]
        return "ambiguous"
    return matches[0]

def guide(request, experience="junior"):
    result = discover(request, experience)
    intent = classify(request)
    result["intent"] = intent
    result["task_steps"] = STEPS.get(intent, ["Confirmar a tarefa, o produto e o resultado esperado antes de executar"])
    result["task_execution_authorized"] = False
    if intent in ("ambiguous", "unspecified") and result["status"] == "ready":
        result["status"] = "clarification_required"
    if result["status"] != "ready":
        result["task_steps"] = ["Confirmar o escopo pendente e as fontes oficiais antes de qualquer alteracao"] + result["task_steps"]
    return result

def main():
    p = argparse.ArgumentParser(description="Orientacao inicial de tarefas SDKA")
    p.add_argument("request")
    p.add_argument("--experience", choices=["junior", "intermediate", "senior"], default="junior")
    a = p.parse_args()
    print(json.dumps(guide(a.request, a.experience), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
