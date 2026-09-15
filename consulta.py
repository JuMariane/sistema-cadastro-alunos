"""
Funcionalidade: Consultar aluno(s).
Responsável: Ágatha (Aluno 2).
Branch: consulta
"""

from storage import carregar_alunos


def listar_todos():
    alunos = carregar_alunos()

    if not alunos:
        print("\nNenhum aluno cadastrado ainda.\n")
        return

    print("\n--- LISTA DE ALUNOS ---")
    for aluno in alunos:
        print(
            f"Matrícula: {aluno['matricula']} | "
            f"Nome: {aluno['nome']} | "
            f"Idade: {aluno['idade']} anos | "
            f"Curso: {aluno['curso']}"
        )
    print("-----------------------")
    print(f"Total: {len(alunos)} aluno(s) cadastrado(s).\n")


def consultar_por_matricula():
    alunos = carregar_alunos()

    try:
        matricula = int(input("\nDigite a matrícula do aluno: ").strip())
    except ValueError:
        print("Erro: matrícula deve ser um número inteiro.\n")
        return

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            print("\n--- ALUNO ENCONTRADO ---")
            print(f"Matrícula: {aluno['matricula']}")
            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Curso: {aluno['curso']}\n")
            return

    print("Aluno não encontrado.\n")


def consultar_aluno():
    print("\n--- CONSULTA DE ALUNOS ---")
    print("1. Listar todos os alunos")
    print("2. Buscar por matrícula")
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        listar_todos()
    elif opcao == "2":
        consultar_por_matricula()
    else:
        print("Opção inválida.\n")


# Aliases para compatibilidade
consultar_alunos = consultar_aluno
buscar_por_matricula = consultar_por_matricula