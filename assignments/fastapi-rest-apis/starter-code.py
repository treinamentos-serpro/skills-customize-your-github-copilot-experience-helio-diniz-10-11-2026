from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class BookCreate(BaseModel):
    title: str
    author: str
    year: int = Field(gt=0)


books = [
    {"id": 1, "title": "Dom Casmurro", "author": "Machado de Assis", "year": 1899},
    {"id": 2, "title": "O Cortiço", "author": "Aluísio Azevedo", "year": 1890},
]


# Implemente aqui os endpoints GET /books e GET /books/{book_id}

# Implemente aqui o endpoint POST /books

# Implemente aqui os endpoints PUT /books/{book_id} e DELETE /books/{book_id}
