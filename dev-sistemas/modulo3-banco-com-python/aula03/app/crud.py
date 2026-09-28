from sqlalchemy.orm import Session 
from app.models import Funcionario, Departamento 
 
def criar_funcionario(db: Session, nome: str, email: str, salario: float): 
    # 1 Verificar se o email já existe 
    existe = db.query(Funcionario).filter( 
        Funcionario.email == email 
    ).first() 
 
    if existe: 
        raise ValueError(f'E-mail {email} já cadastrado') 
 
    # 2 Criar o objeto 
    novo = Funcionario(nome=nome, email=email, salario=salario) 
 
    # 3 Salvar no banco 
    db.add(novo) 
    db.commit() 
    db.refresh(novo)  # busca o id pelo banco 
    return novo 
 
# READ - Buscar funcionarios com cadastro ativo 
def listar_funcionarios(db: Session, apenas_ativos: bool=True): 
    query = db.query(Funcionario) 
    if apenas_ativos: 
        query = query.filter(Funcionario.ativo == True) 
        return query.order_by(Funcionario.nome).all() 
 
# READ - Buscar funcionarios pelo id 
def buscar_funcionarios(db: Session, funcionarios_id: int): 
    return db.query(Funcionario).filter( 
        Funcionario.id == funcionarios_id 
    ).first()  # Retorna None se não encontrar 
 
# UPDATE -  
def atualizar_funcionario( 
        de: Session, funcionario_id: int,  
        nome: str = None, salario: float = None 
): 
    func = buscar_funcionarios(db, funcionario_id) 
 
    if not func: 
        raise ValueError(f'Funcionário {funcionario_id} não encontrado') 
 
# atualizar só os campos que foram enviados 
    if nome is not None: 
        func.nome = nome 
    if salario is not None: 
        func.salario = salario 
 
    db.commit()         # confirma a alteração no banco 
    db.refresh(func)    #sincronizar 
    return func 


# ==========================================================
# DEPARTAMENTO
# ==========================================================

# CREATE - Criar departamento
def criar_departamento(db: Session, nome: str, sigla: str):
    existe = db.query(Departamento).filter(
        Departamento.sigla == sigla
    ).first()

    if existe:
        raise ValueError(f'Sigla {sigla} já cadastrada')

    novo = Departamento(
        nome=nome,
        sigla=sigla
    )

    db.add(novo)
    db.commit()
    db.refresh(novo)

    return novo


# READ - Listar departamentos
def listar_departamentos(db: Session, apenas_ativos: bool=True):
    query = db.query(Departamento)

    if apenas_ativos:
        query = query.filter(Departamento.ativo == True)

    return query.order_by(Departamento.nome).all()


# READ - Buscar departamento pelo id
def buscar_departamento(db: Session, departamento_id: int):
    return db.query(Departamento).filter(
        Departamento.id == departamento_id
    ).first()


# UPDATE - Atualizar departamento
def atualizar_departamento(
        db: Session,
        departamento_id: int,
        nome: str = None,
        sigla: str = None
):
    departamento = buscar_departamento(db, departamento_id)

    if not departamento:
        raise ValueError(
            f'Departamento {departamento_id} não encontrado'
        )

    if nome is not None:
        departamento.nome = nome

    if sigla is not None:
        departamento.sigla = sigla

    db.commit()
    db.refresh(departamento)

    return departamento


# DELETE - Desativar departamento
def desativar_departamento(db: Session, departamento_id: int):
    departamento = buscar_departamento(db, departamento_id)

    if not departamento:
        raise ValueError(
            f'Departamento {departamento_id} não encontrado'
        )

    departamento.ativo = False

    db.commit()
    db.refresh(departamento)

    return departamento