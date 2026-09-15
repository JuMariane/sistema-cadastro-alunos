"""
Funcionalidade: Cadastrar aluno.
Responsável: Julia Mariane (Aluno 1).
Branch: cadastro
"""

from storage import carregar_alunos, salvar_alunos, proxima_matricula


def cadastrar_aluno():
    print("\n--- CADASTRO DE ALUNO ---")
    nome = input("Nome do aluno: ").strip()

    if not nome:
        print("Erro: o nome não pode ser vazio.\n")
        return

    try:
        idade = int(input("Idade: ").strip())
        if idade <= 0:
            print("Erro: a idade deve ser maior que zero.\n")
            return
    except ValueError:
        print("Erro: idade deve ser um número inteiro.\n")
        return

    curso = input("Curso: ").strip()
    if not curso:
        print("Erro: o curso não pode ser vazio.\n")
        return

    alunos = carregar_alunos()
    matricula = proxima_matricula(alunos)

    novo_aluno = {
        "matricula": matricula,
        "nome": nome,
        "idade": idade,
        "curso": curso,
    }

    alunos.append(novo_aluno)
    salvar_alunos(alunos)

    print(f"Aluno cadastrado com sucesso! Matrícula: {matricula}\n")