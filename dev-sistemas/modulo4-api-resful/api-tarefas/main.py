
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from auth import usuario_logado

app = FastAPI()

tarefas = []
proximo_id = 1


class Tarefa(BaseModel):
    titulo: str
    descricao: str = ""
    concluida: bool = False


class TarefaAtualizacao(BaseModel):
    titulo: str | None = None
    descricao: str | None = None
    concluida: bool | None = None


# PUBLICO: qualquer pessoa pode consultar
@app.get("/tarefas")
def listar_tarefas():
    return tarefas


# PROTEGIDO: somente usuário logado pode criar
@app.post("/tarefas", status_code=status.HTTP_201_CREATED)
def criar_tarefa(
    tarefa: Tarefa,
    email: str = Depends(usuario_logado),
):
    global proximo_id

    nova_tarefa = {
        "id": proximo_id,
        **tarefa.model_dump(),
    }

    tarefas.append(nova_tarefa)
    proximo_id += 1

    return nova_tarefa


# PROTEGIDO: qualquer usuário logado pode editar
@app.patch("/tarefas/{id}")
def editar_tarefa(
    id: int,
    atualizacao: TarefaAtualizacao,
    email: str = Depends(usuario_logado),
):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            dados = atualizacao.model_dump(exclude_unset=True)
            tarefa.update(dados)
            return tarefa

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada",
    )


# PROTEGIDO: qualquer usuário logado pode excluir
@app.delete("/tarefas/{id}")
def excluir_tarefa(
    id: int,
    email: str = Depends(usuario_logado),
):
    for indice, tarefa in enumerate(tarefas):
        if tarefa["id"] == id:
            return tarefas.pop(indice)

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada",
    )
