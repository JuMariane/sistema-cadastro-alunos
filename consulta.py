"""
Funcionalidade: Consultar alunos.

Responsável: Ágatha.

Branch: consulta-agatha
"""

from storage import carregar_alunos


def consultar_alunos():
    print("\n--- CONSULTA DE ALUNOS ---")

    alunos = carregar_alunos()

    if not alunos:
        print("Nenhum aluno cadastrado.\n")
        return

    for aluno in alunos:
        print(f"Matrícula: {aluno['matricula']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Curso: {aluno['curso']}")
        print("--------------------------")


def buscar_por_matricula():
    alunos = carregar_alunos()

    try:
        matricula = int(input("Digite a matrícula: "))
    except ValueError:
        print("Erro: a matrícula deve ser um número.\n")
        return

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            print("\n--- ALUNO ENCONTRADO ---")
            print(f"Matrícula: {aluno['matricula']}")
            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Curso: {aluno['curso']}")
            return

    print("Aluno não encontrado.\n")