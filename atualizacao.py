"""
Funcionalidade: Atualizar dados de um aluno.
Responsável (sugestão do enunciado): Aluno 3.
Branch sugerida: atualizacao
"""

from storage import carregar_alunos, salvar_alunos


def atualizar_aluno():
    print("\n--- ATUALIZAÇÃO DE ALUNO ---")
    alunos = carregar_alunos()

    try:
        matricula = int(input("Digite a matrícula do aluno a atualizar: ").strip())
    except ValueError:
        print("Erro: matrícula deve ser um número inteiro.\n")
        return

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            print("Deixe em branco para manter o valor atual.")

            novo_nome = input(f"Nome ({aluno['nome']}): ").strip()
            nova_idade = input(f"Idade ({aluno['idade']}): ").strip()
            novo_curso = input(f"Curso ({aluno['curso']}): ").strip()

            if novo_nome:
                aluno["nome"] = novo_nome
            if nova_idade:
                if nova_idade.isdigit():
                    aluno["idade"] = int(nova_idade)
                else:
                    print("Idade inválida, valor mantido.")
            if novo_curso:
                aluno["curso"] = novo_curso

            salvar_alunos(alunos)
            print("Aluno atualizado com sucesso!\n")
            return

    print("Aluno não encontrado.\n")
