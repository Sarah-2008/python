from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# url do banco - SQlite salva em um arquivo banco.db na pasta do projeto d
DATABASE_URL = 'sqlite:///./banco.db'

# engine: motor de conexão com o banco
engine = create_engine(
    DATABASE_URL,
    connect_args={'check_same_thread': False} # necessario para SQlite
)

# SessionLocal: fabrica de sessões - cada requisição tem a sua propria 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#base: classe base que todos os modelos vao herdar
Base = declarative_base()

#dependencia injetasa nos endpoints via depends(get_db)
#yeld entrega a sessão - endpoint executa - finally fecha a sessão
def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()
