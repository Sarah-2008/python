class Cargo(Base):
    __tablename__ = 'cargos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    nivel = Column(String(20), nullable=False)
    salario_min = Column(Float, nullable=False)
    salario_max = Column(Float, nullable=False)
    ativo = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Cargo {self.titulo} nivel={self.nivel}>"


# Popular cargos (se ainda não tiver dados)
if db.query(Cargo).count() == 0:
    db.add_all([
        Cargo(titulo='Desenvolvedor', nivel='Junior', salario_min=2500, salario_max=4000),
        Cargo(titulo='Desenvolvedor', nivel='Pleno', salario_min=4000, salario_max=7000),
        Cargo(titulo='Designer', nivel='Junior', salario_min=2200, salario_max=3500),
        Cargo(titulo='Analista RH', nivel='Pleno', salario_min=3500, salario_max=6000),
    ])

    db.commit()

print('Cargos inseridos!')


# 1. Listar todos os cargos ordenados por titulo
todos = db.query(Cargo).order_by(Cargo.titulo).all()

print(f"\nTotal: {len(todos)} cargos cadastrados:")

for c in todos:
    print(f"  {c.titulo} ({c.nivel}) - R$ {c.salario_min} a R$ {c.salario_max}")


# 2. Filtrar só cargos Junior
juniors = db.query(Cargo).filter(Cargo.nivel == 'Junior').all()

print(f"\nCargos Junior: {len(juniors)}")


# 3. Buscar um cargo específico pelo titulo
designer = db.query(Cargo).filter(Cargo.titulo == 'Designer').first()

if designer:
    print(f"Designer encontrado: faixa R$ {designer.salario_min} - R$ {designer.salario_max}")