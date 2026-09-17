# Sistema de Cadastro de Alunos

## Nome do projeto
Sistema de Cadastro de Alunos

## Nome dos integrantes
- **Julia Mariane dos Santos** - Cadastro e Atualização (branches: `cadastro`, `atualizacao`)
- **Ágatha Rodrigues de Souza Oliveira** - Consulta e Exclusão (branches: `consulta`, `exclusao`)

## Descrição do sistema
Sistema de linha de comando (terminal), desenvolvido em Python, que permite cadastrar, consultar, atualizar e excluir alunos. Os dados são persistidos em um arquivo local `alunos.json` em formato JSON.

### Funcionalidades:
- **Cadastro**: Adiciona um novo aluno (nome, idade, curso) com matrícula gerada automaticamente.
- **Consulta**: Permite listar todos os alunos ou buscar por número de matrícula.
- **Atualização**: Edita os dados de um aluno cadastrado.
- **Exclusão**: Remove um aluno do sistema mediante confirmação.

## Tecnologias utilizadas
- Python 3
- Módulo `json` (persistência de dados)
- Git e GitHub (versionamento e colaboração)

## Como executar o projeto
1. Certifique-se de ter o Python 3 instalado: `python --version`
2. Clone o repositório: `git clone https://github.com/JuMariane/sistema-cadastro-alunos.git` e depois `cd sistema-cadastro-alunos`
3. Execute o programa: `python main.py`
4. Use o menu exibido no terminal para navegar pelas opções.
