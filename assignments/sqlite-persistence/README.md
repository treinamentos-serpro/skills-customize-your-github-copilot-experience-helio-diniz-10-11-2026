# 📘 Assignment: Persistência de Dados com SQLite

## 🎯 Objective

Aprenda a persistir dados de uma API FastAPI em um banco SQLite, substituindo o armazenamento temporário em memória por operações SQL. Você praticará criação de tabelas, consultas parametrizadas e operações CRUD.

## 📝 Tasks

### 🛠️ Inicializar o Banco de Dados

#### Descrição
Copie o [starter-code.py](starter-code.py) para um arquivo `main.py` dentro da pasta da atividade. Implemente `init_db()` para criar o banco `books.db` e a tabela `books`, e garanta que a função seja executada quando a aplicação iniciar.

Instale as dependências da API com `pip install fastapi uvicorn` e execute a aplicação com `uvicorn main:app --reload`. O SQLite faz parte da biblioteca padrão do Python, então não é necessário instalar uma dependência para o banco.

#### Requisitos
O programa concluído deve:

- Criar a tabela `books` com `id` como chave primária autoincrementada
- Criar os campos `title` e `author` como texto obrigatório e `year` como número inteiro obrigatório
- Rejeitar anos menores ou iguais a zero usando uma restrição `CHECK`
- Criar a tabela sem erro mesmo quando ela já existir


### 🛠️ Consultar Livros no Banco

#### Descrição
Implemente os endpoints de consulta para ler os registros de `books.db`. Use o helper `get_connection()` fornecido e converta cada linha retornada em um dicionário para que o FastAPI possa serializar a resposta. O helper fecha a conexão e confirma ou desfaz a transação ao sair do bloco `with`.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books`, retornando todos os livros; uma tabela vazia deve retornar uma lista vazia
- Implementar `GET /books/{book_id}`, retornando o livro com o identificador informado
- Retornar status `404` com a mensagem `Livro não encontrado` quando o identificador não existir
- Fechar as conexões ao terminar cada operação


### 🛠️ Tornar o CRUD Persistente

#### Descrição
Implemente cadastro, atualização e remoção usando SQL. Teste os endpoints pela documentação interativa em `http://127.0.0.1:8000/docs` e reinicie a aplicação para confirmar que os dados cadastrados continuam no banco.

#### Requisitos
O programa concluído deve:

- Implementar `POST /books`, validando os campos com o modelo `BookCreate` e retornando o livro criado com status `201`
- Gerar o `id` usando o autoincremento do SQLite, sem calcular o próximo identificador manualmente
- Implementar `PUT /books/{book_id}`, atualizando os campos sem alterar o `id`
- Implementar `DELETE /books/{book_id}`, removendo o registro e retornando status `204` sem corpo
- Retornar status `404` ao tentar atualizar ou remover um livro inexistente
- Usar parâmetros SQL (`?`) nas consultas que recebem dados, sem concatenar valores diretamente no comando SQL