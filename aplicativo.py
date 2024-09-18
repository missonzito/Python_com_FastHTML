from fasthtml.common import fast_app, serve, Titled, RedirectResponse
from componentes import gerar_titulo, gerar_formulario, gerar_lista_tarefas

app, routes = fast_app()

lista_tarefas = []

@routes("/")
def homepage():
    formulario = gerar_formulario()
    elemento_lista_tarefas = gerar_lista_tarefas(lista_tarefas)
    return Titled("Lista de Tarefas", formulario, elemento_lista_tarefas)

@routes("/adicionar_tarefa", methods=["post"])
def adicionar_tarefas(tarefa: str):
    if tarefa:
        lista_tarefas.append(tarefa)
    return RedirectResponse(url="/", status_code=303)

@routes("/deletar/{posicao}")
def deletar(posicao: int):
    if len(lista_tarefas) > posicao:
        lista_tarefas.pop(posicao)
    return RedirectResponse(url="/", status_code=303)

@routes("/Blog")
def homepage():
    return gerar_titulo("Blog", "Blog com artigos para você aprender Python")

serve()