
import os
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

if not SECRET_KEY:
    raise RuntimeError("Configure SECRET_KEY no arquivo .env")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def criar_token(email: str):
    expiracao = datetime.now(timezone.utc) + timedelta(minutes=30)
    dados = {"sub": email, "exp": expiracao}

    return jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)


def usuario_logado(token: str = Depends(oauth2_scheme)):
    credenciais_invalidas = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido ou expirado",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )
        email = payload.get("sub")

        if not email:
            raise credenciais_invalidas

        return email

    except JWTError:
        raise credenciais_invalidas
