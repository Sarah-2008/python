from app.database import engine, Base
from app import models # importar para registrar os modelos na base

# create_all: cria as tabelas que não existem ainda
# Se a tabela já existe: ela não apaga, não muda nada

Base.metadata.create_all(bind=engine)
print('Tabelas ciadas')