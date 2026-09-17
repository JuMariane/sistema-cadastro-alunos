# Sistema de Cadastro de Alunos

## Nome do Projeto
**Sistema de Cadastro de Alunos**

---

## Integrantes do Grupo e Divisão de Funcionalidades
O projeto foi desenvolvido em dupla, dividindo as 4 funcionalidades do sistema igualmente entre as duas integrantes, cada uma trabalhando em suas respectivas branches:

- **Julia Mariane dos Santos**
  - **Cadastro de Alunos** (branch: `cadastro`) — Responsável pela criação do formulário de entrada, validações de campos e geração automática de matrícula.
  - **Atualização de Dados** (branch: `atualizacao`) — Responsável pela busca por matrícula e edição dinâmica dos dados do aluno.

- **Ágatha Rodrigues de Souza Oliveira**
  - **Consulta de Alunos** (branch: `consulta`) — Responsável pela listagem completa de alunos cadastrados e busca individual por matrícula.
  - **Exclusão de Alunos** (branch: `exclusao`) — Responsável pela exclusão de registros com solicitação prévia de confirmação.

---

## Descrição do Sistema
Sistema interativo via terminal (CLI) desenvolvido em Python para gerenciar o ciclo completo de cadastro de alunos. Os dados são persistidos localmente em formato JSON (`alunos.json`), garantindo integridade e facilidade de manipulação.

### Funcionalidades:
1. **Cadastrar Aluno**: Permite registrar nome, idade e curso, atribuindo um identificador sequencial único (matrícula).
2. **Consultar Aluno**: Disponibiliza visualização formatada de todos os alunos ou busca direta pelo número da matrícula.
3. **Atualizar Aluno**: Permite editar seletivamente o nome, idade ou curso de um aluno já existente mantendo os dados não alterados.
4. **Excluir Aluno**: Remove com segurança o registro de um aluno após confirmação do usuário (`s/n`).

---

## Estrutura de Branches e Fluxo Git
- `main`: Branch principal e estável do projeto.
- `cadastro`: Desenvolvimento da funcionalidade de inclusão de alunos.
- `consulta`: Desenvolvimento da funcionalidade de listagem e busca.
- `atualizacao`: Desenvolvimento da funcionalidade de edição de registros.
- `exclusao`: Desenvolvimento da funcionalidade de remoção de registros.

---

## Tecnologias Utilizadas
- **Python 3**: Linguagem base do sistema.
- **Módulo `json`**: Persistência de dados em arquivo estruturado.
- **Git & GitHub**: Controle de versão distribuído, branches, pull requests, colaboração com forks e tags de release.

---

## Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/JuMariane/sistema-cadastro-alunos.git
   cd sistema-cadastro-alunos
   ```

2. **Execute o sistema:**
   ```bash
   python main.py
   ```

3. **Utilize o menu no terminal para navegar:**
   ```text
   ========================================
      SISTEMA DE CADASTRO DE ALUNOS
   ========================================
   1. Cadastrar aluno
   2. Consultar aluno
   3. Atualizar aluno
   4. Excluir aluno
   0. Sair
   ========================================
   ```
