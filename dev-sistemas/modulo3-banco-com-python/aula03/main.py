from app.database import engine, Base, SessionLocal
from app import models # importar para registrar os modelos na Base
from app.seed import popular_banco
from app.crud import criar_funcionario, listar_funcionarios, buscar_funcionarios, atualizar_funcionario, criar_departamento, listar_departamentos, buscar_departamento, atualizar_departamento, desativar_departamento 

# create_all: cria as tabelas que não existem ainda
# Se a tabela já existe: não apaga, não muda nada
Base.metadata.create_all(bind=engine)
popular_banco()
# 1 CREATE
db = SessionLocal()
try:
    novo = criar_funcionario(db, 'Pedro Alves', 'pedro@empresa.com', 3200.0)
    print(f'Criado: {novo}')

# 2 READ
    todos = listar_funcionarios(db)
    print(f'Total: {len(todos)} funcionarios')
    for funcionario in todos:
        print(f'{funcionario.nome} - R${funcionario.salario}')

    um = buscar_funcionarios(db, 1)
    if um: 
        print(f'\nFuncionário 1: {um.nome}')

# UPDATE


    # ==========================================================
    # DEPARTAMENTO
    # ==========================================================

    # 1 CREATE
    novo_departamento = criar_departamento(
        db,
        'Logística',
        'LOG'
    )
    print(f'\nDepartamento criado: {novo_departamento}')

    # 2 READ
    departamentos = listar_departamentos(db)
    print(f'Total: {len(departamentos)} departamentos')

    for departamento in departamentos:
        print(
            f'{departamento.nome} - '
            f'{departamento.sigla}'
        )

    departamento = buscar_departamento(
        db,
        novo_departamento.id
    )

    if departamento:
        print(
            f'\nDepartamento encontrado: '
            f'{departamento.nome}'
        )

    # 3 UPDATE
    departamento_atualizado = atualizar_departamento(
        db,
        novo_departamento.id,
        nome='Logística e Transportes',
        sigla='LOGT'
    )

    print(
        f'\nDepartamento atualizado: '
        f'{departamento_atualizado.nome} - '
        f'{departamento_atualizado.sigla}'
    )

    # 4 DESATIVAR
    departamento_desativado = desativar_departamento(
        db,
        novo_departamento.id
    )

    print(
        f'\nDepartamento desativado: '
        f'{departamento_desativado.nome}'
    )


finally:
    db.close()