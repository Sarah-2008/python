
from fastapi import FastAPI

from database import Base, engine
from router import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Livros API",
    description="API de cadastro de livros com SQLite",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def inicio():
    return {"mensagem": "API de Livros funcionando!"}
