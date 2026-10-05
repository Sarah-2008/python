from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Genero(Base):
    __tablename__ = "generos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String, unique=True, nullable=False)


class Autor(Base):
    __tablename__ = "autores"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    nacionalidade: Mapped[str | None] = mapped_column(String, nullable=True)


class Livro(Base):
    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    titulo: Mapped[str] = mapped_column(String, nullable=False)
    ano_publicacao: Mapped[int] = mapped_column(Integer)
    disponivel: Mapped[bool] = mapped_column(Boolean, default=True)

    genero_id: Mapped[int] = mapped_column(
        ForeignKey("generos.id")
    )

    autor_id: Mapped[int] = mapped_column(
        ForeignKey("autores.id")
    )