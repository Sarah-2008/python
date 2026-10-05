from app.database import engine, SessionLocal, Base
from app.models import Genero, Autor, Livro


# Criar as tabelas
Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso!")


# Criar sessão
db = SessionLocal()


# Gêneros
genero1 = Genero(nome="Ficção")
genero2 = Genero(nome="Romance")
genero3 = Genero(nome="Fantasia")

db.add(genero1)
db.add(genero2)
db.add(genero3)

db.commit()

print("Gêneros inseridos com sucesso!")


# Autores
autor1 = Autor(
    nome="Machado de Assis",
    nacionalidade="Brasileiro"
)

autor2 = Autor(
    nome="J. K. Rowling",
    nacionalidade="Britânica"
)

autor3 = Autor(
    nome="George Orwell",
    nacionalidade="Britânico"
)

db.add(autor1)
db.add(autor2)
db.add(autor3)

db.commit()

print("Autores inseridos com sucesso!")


# Livros
livro1 = Livro(
    titulo="Dom Casmurro",
    ano_publicacao=1899,
    disponivel=True,
    genero_id=genero2.id,
    autor_id=autor1.id
)

livro2 = Livro(
    titulo="Memórias Póstumas de Brás Cubas",
    ano_publicacao=1881,
    disponivel=True,
    genero_id=genero1.id,
    autor_id=autor1.id
)

livro3 = Livro(
    titulo="Harry Potter e a Pedra Filosofal",
    ano_publicacao=1997,
    disponivel=True,
    genero_id=genero3.id,
    autor_id=autor2.id
)

livro4 = Livro(
    titulo="1984",
    ano_publicacao=1949,
    disponivel=False,
    genero_id=genero1.id,
    autor_id=autor3.id
)

livro5 = Livro(
    titulo="A Revolução dos Bichos",
    ano_publicacao=1945,
    disponivel=True,
    genero_id=genero1.id,
    autor_id=autor3.id
)

db.add(livro1)
db.add(livro2)
db.add(livro3)
db.add(livro4)
db.add(livro5)

db.commit()

print("Livros inseridos com sucesso!")

print("Banco de dados populado com sucesso!")


# Fechar conexão
db.close()