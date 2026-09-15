"""
Funcionalidade: Excluir aluno.
Responsável: Aluno 4.
Branch: exclusao
"""

from storage import carregar_alunos, salvar_alunos


def excluir_aluno():
    print("\n--- EXCLUSÃO DE ALUNO ---")
    alunos = carregar_alunos()

    try:
        matricula = int(input("Digite a matrícula do aluno a excluir: ").strip())
    except ValueError:
        print("Erro: matrícula deve ser um número inteiro.\n")
        return

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            confirmacao = input(
                f"Confirma a exclusão de '{aluno['nome']}' (matrícula {matricula})? [s/n]: "
            ).strip().lower()

            if confirmacao == "s":
                alunos.remove(aluno)
                salvar_alunos(alunos)
                print("Aluno excluído com sucesso!\n")
            else:
                print("Exclusão cancelada.\n")
            return

    print("Aluno não encontrado.\n")
