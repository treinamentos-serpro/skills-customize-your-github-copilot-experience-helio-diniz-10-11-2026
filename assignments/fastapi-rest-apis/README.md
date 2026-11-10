# 📘 Tarefa: Construindo APIs REST com FastAPI

## 🎯 Objective

Aprenda a criar uma API REST com o framework FastAPI, definindo endpoints para consultar, criar, atualizar e remover recursos, com validação automática de dados usando Pydantic.

## 📝 Tasks

### 🛠️ Criar Endpoints de Consulta

#### Descrição
Crie uma aplicação FastAPI que gerencia uma lista de livros armazenada em memória. Copie o [starter-code.py](starter-code.py) para um arquivo `main.py`, instale as dependências com `pip install fastapi uvicorn` e implemente os endpoints `GET` para listar todos os livros e para buscar um livro pelo seu `id`.

Execute a aplicação com `uvicorn main:app --reload` e acesse `http://127.0.0.1:8000/docs` para testar os endpoints pela documentação interativa do FastAPI.

#### Requisitos
O programa concluído deve:

- Usar a instância `app = FastAPI()` já presente no starter code
- Implementar `GET /books`, retornando a lista de livros
- Implementar `GET /books/{book_id}`, retornando o livro com o `id` informado
- Retornar status `404` com a mensagem `"Livro não encontrado"` quando o `id` não existir

Exemplo de resposta:

```json
GET /books/1

{
  "id": 1,
  "title": "Dom Casmurro",
  "author": "Machado de Assis",
  "year": 1899
}
```


### 🛠️ Cadastrar Livros com Validação

#### Descrição
Adicione um endpoint para cadastrar novos livros. Os dados recebidos devem ser validados por um modelo Pydantic, e o FastAPI deve rejeitar automaticamente requisições inválidas.

#### Requisitos
O programa concluído deve:

- Usar o modelo `BookCreate` (já definido no starter code) com os campos `title`, `author` e `year`
- Implementar `POST /books`, que recebe um `BookCreate`, gera um `id` novo (um número maior que o maior `id` existente), adiciona o livro à lista e retorna o livro criado
- Retornar status `201` ao cadastrar um livro com sucesso
- Garantir que o `year` seja maior que `0`, mantendo a restrição definida no modelo com `Field(gt=0)`
- Verificar que uma requisição sem o campo `title` ou com `year` em formato inválido recebe status `422`

Exemplo de entrada:

```json
POST /books

{
  "title": "Memórias Póstumas de Brás Cubas",
  "author": "Machado de Assis",
  "year": 1881
}
```


### 🛠️ Atualizar e Remover Livros

#### Descrição
Complete o CRUD da API adicionando os endpoints para atualizar e remover livros. Os métodos HTTP e os status codes devem seguir o padrão REST.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /books/{book_id}`, que recebe um `BookCreate` e substitui os dados do livro com o `id` informado, retornando o livro atualizado com status `200`
- Implementar `DELETE /books/{book_id}`, que remove o livro da lista e retorna status `204` (sem conteúdo no corpo da resposta)
- Retornar status `404` nas duas operações quando o `id` não existir
- Manter o `id` do livro inalterado após uma atualização
