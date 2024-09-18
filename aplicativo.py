from fasthtml.common import fast_app, serve
from componentes import gerar_titulo

app, routes = fast_app()

@routes("/")
def homepage():
    return gerar_titulo("Homepage", "Brincando de FastHTML")
@routes("/Blog")
def homepage():
    return gerar_titulo("Blog", "Blog com artigos para você aprender Python")

serve()