
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class LivroCreate(BaseModel):
    titulo: str = Field(min_length=2, max_length=200)
    autor: str = Field(min_length=2, max_length=150)
    ano_publicacao: int | None = None
    disponivel: bool = True


class LivroUpdate(BaseModel):
    titulo: str | None = Field(default=None, min_length=2, max_length=200)
    autor: str | None = Field(default=None, min_length=2, max_length=150)
    ano_publicacao: int | None = None
    disponivel: bool | None = None


class LivroResponse(BaseModel):
    id: int
    titulo: str
    autor: str
    ano_publicacao: int | None
    disponivel: bool
    criado_em: datetime

    model_config = ConfigDict(from_attributes=True)
