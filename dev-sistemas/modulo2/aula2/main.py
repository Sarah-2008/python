from http.client import HTTPException

from fastapi import FastAPI
from pydantic import BaseModel, field_validator
from typing import Optional

app = FastAPI(title='API de cadastro - SENAI', version='0.2.0')

# modelo pydantic: define a estrurura e os tipos 
#receber informaççoes 
class Usuario(BaseModel):
    nome: str
    email: str
    cargo: str
    ativo: bool = True #valor padrão
    salario: Optional[float] = None # campo opcional 

    @field_validator('nome')
    @classmethod 
    def validar_nome(cls, v):
        v = v.strip()
        if len(v) < 3:
            raise ValueError('Nome deve ter pelo menos 3 caracteres')
        return v.title()

# modelo resposta: incluir o ID gerado pelo servidor 
class UsuarioResposta(BaseModel):
    id: int
    nome: str
    email: str
    cargo: str
    ativo: bool
    salario: Optional[float] = None

Usuario_db: list[UsuarioResposta] = [
    UsuarioResposta(id=1, nome='Toin jesus', email='toin@gmail.com',
                    cargo='Desing', ativo=True, salario=3800.0),

    UsuarioResposta(id=2, nome='Maros rodrigues', email='maros@gmail.com',
                    cargo='QA', ativo=True, salario=3200.0),

    UsuarioResposta(id=3, nome='Filipe farias', email='filipe@gmail.com',
                    cargo='Dev', ativo=True, salario=4500.0),
]
proximo_id = 4

# GET /usuarios - Lista todos os usuarios
@app.get('/usuarios', response_model=list[UsuarioResposta])
def listar_usuario():
    return Usuario_db

@app.get('/usuario/{usuario_db}', response_model=UsuarioResposta)
def buscar_usuario(usuario_id: int):
    for in Usuario_db:
        if usuario_id == usuario_id:
            return Usuario
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    