# Sistema de Cadastro de Alunos

## Nome do projeto
Sistema de Cadastro de Alunos

## Nome dos integrantes
- Aluno 1 - Cadastro
- Aluno 2 - Consulta
- Aluno 3 - Atualização
- Aluno 4 - Exclusão

*(substitua pelos nomes reais do grupo)*

## Descrição do sistema
Sistema simples de linha de comando (terminal), desenvolvido em Python,
que permite cadastrar, consultar, atualizar e excluir alunos. Os dados
são armazenados em um arquivo local `alunos.json`, funcionando como um
pequeno banco de dados em arquivo.

Funcionalidades:
- **Cadastro**: adiciona um novo aluno (nome, idade, curso) com matrícula
  gerada automaticamente.
- **Consulta**: lista todos os alunos ou busca um aluno por matrícula.
- **Atualização**: edita os dados de um aluno já cadastrado.
- **Exclusão**: remove um aluno do sistema mediante confirmação.

## Tecnologias utilizadas
- Python 3
- Módulo `json` da biblioteca padrão (persistência de dados)
- Git e GitHub (versionamento e colaboração)

## Como executar o projeto
1. Certifique-se de ter o Python 3 instalado (`python3 --version`).
2. Clone o repositório:
   ```
   git clone https://github.com/SEU-USUARIO/sistema-cadastro-alunos.git
   cd sistema-cadastro-alunos
   ```
3. Execute o programa:
   ```
   python3 main.py
   ```
4. Use o menu exibido no terminal para cadastrar, consultar, atualizar
   ou excluir alunos.
