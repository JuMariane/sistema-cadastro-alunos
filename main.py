"""
Sistema de Cadastro de Alunos
Ponto de entrada do programa - integra as funcionalidades
desenvolvidas em cada branch (cadastro, consulta, atualizacao, exclusao).
"""

# Fork desse projeto criado por Lucas e Tamires

from cadastro import cadastrar_aluno
from consulta import consultar_aluno
from atualizacao import atualizar_aluno
from exclusao import excluir_aluno


# Importa as funções usadas no sistema.

def exibir_menu():
    print("=" * 40)
    print("   SISTEMA DE CADASTRO DE ALUNOS")
    print("=" * 40)
    print("1. Cadastrar aluno")
    print("2. Consultar aluno")
    print("3. Atualizar aluno")
    print("4. Excluir aluno")
    print("0. Sair")
    print("=" * 40)

# Exibe o menu com as opções disponíveis.

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            consultar_aluno()
        elif opcao == "3":
            atualizar_aluno()
        elif opcao == "4":
            excluir_aluno()
        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executa a função escolhida pelo usuário.

if __name__ == "__main__":
    main()