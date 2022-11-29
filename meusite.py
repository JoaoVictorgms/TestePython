from selectors import EpollSelector
from flask import Flask,render_template, request
app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    variavel ='Adivinhe o numero'
    if request.method == 'GET':
        return render_template("index.html",variavel = variavel)
    else:
         numero = 0
         palpite = int(request.form.get("nome"))
    if numero == palpite:
        return '<h1> Resultado voce ganhou</h1>'
    else:
        return '<h1>Perdeu</h1>'

@app.route('/<string:nome>')
def error(nome):
    variavel =  f'Página ({nome}) Não existe'
    return render_template("error.html",variavel = variavel)
