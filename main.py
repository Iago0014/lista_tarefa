
from datetime import datetime
from flask import Flask, render_template, request
import base_dados 

num = 0

bDados = base_dados

app = Flask(__name__)

#Rota de abrir pagina 
@app.route('/')
def abrePg():
    return render_template('criar_tarefa.html', listaT = bDados.mostrar())

#Rota para inserir daddos.
@app.route('/inserir', methods=['POST'])
def inserir_tarefa():
    tarefa = request.form['taref']
    dataCr = datetime.now()
    dataRe = datetime.now()
    statusLis = False
    bDados.inserir_dados(tarefa, dataCr, dataRe, statusLis)
    return render_template('tarefas.html', listaT = bDados.mostrar())

#Rota para excluir alguma tarefa.
@app.route('/exclui', methods=['POST'])
def deleta():
    num = request.form['numID']
    bDados.excluir(num)
    return render_template('tarefas.html', listaT = bDados.mostrar())

#Rota para marcar alguma tarefa realizada.
@app.route('/realizada', methods=['POST'])
def realizar_tarefa():
    valor = request.form['idList']
    bDados.editar(valor)
    return render_template('tarefas.html', listaT = bDados.mostrar())


app.run(debug=True)