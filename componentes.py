from fasthtml.common import Div, H1, P, Form, Input, Button, Ul, Li, A

def gerar_titulo(titulo, subtitulo):
    return Div(
        H1(titulo),
        P(subtitulo),
        P("Esse componente foi gerado com FastHTML")
    )

def gerar_formulario():
    formulario = Form(
        Input(type="text", name="tarefa", placeholder="insira a tarefa a ser adicionada"),
        Button("Enviar"),
        method="post",
        action="/adicionar_tarefa"
    )
    return formulario

def gerar_lista_tarefas(lista_tarefas):

    itens_lista = [Li(tarefa, " - ", A("Excluir", href=f"/deletar/{i}")) for i, tarefa in enumerate (lista_tarefas)]
    
    lista = Ul(
        *itens_lista
    )
    return lista
