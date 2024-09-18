from fasthtml.common import FastHTML, serve

app = FastHTML()

@app.get("/")
def homepage():
    return "<h1>Bem Vindo ao meu site com FastHTML</h1>"

serve()