from app.database import SessionLocal
from app.models import Departamentos, Cargo

def popular_banco():
    db = SessionLocal() #abrir sessão
    try: 
        # Se já tm dados, não inserir de novo
        if db.query(Departamentos).count() > 0:
            print('Banco já preenchido. Pulando...')
            return

        db.add_all([
            Departamentos(nome='Tecnologia da Informação', sigla='TI'),
            Departamentos(nome='Recursos Humanos', sigla='RH'),
            Departamentos(nome='Financeiro', sigla='FIN'),
            Departamentos(nome='Comercial', sigla='COM')
        ])

        db.add_all([
            Cargo(titulo='Desenvolvedor', nivel='Júnio', salario_min=4000, salario_max=8000000),
            Cargo(titulo='Desenvolvedor', nivel='Pleno', salario_min=6000, salario_max=8000000),
            Cargo(titulo='Designer', nivel='Júnio', salario_min=2500, salario_max=900000),
            Cargo(titulo='Analista de RH', nivel='Pleno', salario_min=56600, salario_max=60000),
            ])

        db.commit()
        print('Banco preenchido co sucesso')

    except Exception as e:
        db.rollback()
        print(f'Erro {e}')
    finally:
        db.close() 
if __name__=='__main__':
    popular_banco()