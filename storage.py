"""
Módulo responsável por ler e gravar os dados dos alunos
em um arquivo JSON (banco de dados simples em arquivo).
"""

import json
import os

ARQUIVO_DADOS = "alunos.json"


def carregar_alunos():
    """Lê o arquivo alunos.json e devolve uma lista de alunos (dicionários)."""
    if not os.path.exists(ARQUIVO_DADOS):
        return []

    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def salvar_alunos(alunos):
    """Grava a lista de alunos no arquivo alunos.json."""
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, indent=4, ensure_ascii=False)


def proxima_matricula(alunos):
    """Gera um número de matrícula sequencial simples."""
    if not alunos:
        return 1
    return max(aluno["matricula"] for aluno in alunos) + 1