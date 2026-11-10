import sqlite3
from contextlib import contextmanager

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

DATABASE_PATH = "books.db"

app = FastAPI()


class BookCreate(BaseModel):
    title: str
    author: str
    year: int = Field(gt=0)


@contextmanager
def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    try:
        with connection:
            yield connection
    finally:
        connection.close()


def init_db():
    # Crie a tabela books usando CREATE TABLE IF NOT EXISTS.
    pass


init_db()


@app.get("/books")
def list_books():
    # Consulte todos os livros no banco e retorne uma lista de dicionários.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # Consulte o livro pelo id; lance HTTPException(404) se não existir.
    pass


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    # Insira o livro e retorne o registro criado, incluindo o id gerado.
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookCreate):
    # Atualize o livro sem alterar o id; lance HTTPException(404) se não existir.
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    # Remova o livro; lance HTTPException(404) se não existir.
    pass