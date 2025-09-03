# EXERCICIO 2-1: HTML básico na resposta
# Modifique sua rota principal para retornar um pequeno HTML com título, parágrafo e um link para outra rota.
# (Usar 'render_template' para renderizar um arquivo .html)
# (Usar 'url_for()' nas anchor tags do script html)


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ex_2-1.html')

@app.route('/sobre')
def sobre():
    return 'Fábrica de Programador'

@app.route('/zezinho')
def zezinho():
    return "Achou a rota"

if __name__ == '__main__': # condição para os arquivos serem executados de maneira independente
    app.run(debug=True)