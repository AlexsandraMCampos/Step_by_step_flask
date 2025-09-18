# EXERCICIO 3-2: Templates com estruturas de controle
# Passe uma lista de nomes para o template e use um for em Jinja para listar todos os nomes em uma <ul>.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask !'

@app.route('/sobre')
def sobre():
    return 'Olá, eu sou aluno do projeto Fábrica de Programadores!'

@app.route('/lista')
def lista():
    alunos = ['Aluno1','Aluno2','Aluno3','Aluno4','Aluno5', 'Aluno6']
    return render_template('ex_3-2.html',lista=alunos)


if __name__ == '__main__':
    app.run(debug=True)