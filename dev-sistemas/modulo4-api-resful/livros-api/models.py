
from sqlalchemy import Column, Integer, String, Boolean, DateTime, text
from database import Base


class Livro(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    titulo = Column(String(200), nullable=False)
    autor = Column(String(150), nullable=False)

    ano_publicacao = Column(Integer, nullable=True)

    disponivel = Column(
        Boolean,
        nullable=False,
        default=True,
        server_default=text("1")
    )

    criado_em = Column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP")
    )
