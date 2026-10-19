from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, field_validator


class UsuarioCreate(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    senha: str = Field(..., min_length=8)

    @field_validator("nome", mode="before")
    @classmethod
    def validar_nome(cls, valor):
        if not isinstance(valor, str):
            return valor

        valor = valor.strip()

        if not valor:
            raise ValueError("O nome não pode estar vazio ou conter apenas espaços.")
        if len(valor) < 2:
            raise ValueError("O nome deve ter pelo menos 2 caracteres.")
        if len(valor) > 100:
            raise ValueError("O nome deve ter no máximo 100 caracteres.")
        if any(caractere.isdigit() for caractere in valor):
            raise ValueError("O nome não pode conter números.")

        return valor

    @field_validator("senha")
    @classmethod
    def validar_senha(cls, valor):
        if not any(caractere.isalpha() for caractere in valor):
            raise ValueError("A senha deve conter pelo menos uma letra.")
        if not any(caractere.isdigit() for caractere in valor):
            raise ValueError("A senha deve conter pelo menos um número.")
        return valor


class UsuarioPatch(BaseModel):
    nome: Optional[str] = Field(default=None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None

    @field_validator("nome", mode="before")
    @classmethod
    def validar_nome(cls, valor):
        if valor is None:
            return None
        if not isinstance(valor, str):
            return valor

        valor = valor.strip()

        if not valor:
            raise ValueError("O nome não pode estar vazio ou conter apenas espaços.")
        if len(valor) < 2:
            raise ValueError("O nome deve ter pelo menos 2 caracteres.")
        if len(valor) > 100:
            raise ValueError("O nome deve ter no máximo 100 caracteres.")
        if any(caractere.isdigit() for caractere in valor):
            raise ValueError("O nome não pode conter números.")

        return valor


class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    ativo: bool
    criado_em: datetime

    class Config:
        from_attributes = True


class ErroResponse(BaseModel):
    erro: str
    detalhe: Optional[str] = None
