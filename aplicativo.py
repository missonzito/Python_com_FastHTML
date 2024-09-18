from fasthtml.common import fast_app, serve
from componentes import gerar_titulo, gerar_formulario

app, routes = fast_app()

@routes("/")
def homepage():
    formulario = gerar_formulario()
    return formulario 

@routes("/Blog")
def homepage():
    return gerar_titulo("Blog", "Blog com artigos para você aprender Python")

serve()