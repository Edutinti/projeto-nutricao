from flask import Flask, render_template, url_for

"""
-Criar uma pagina para cadastro de alimentos que terei que passar a quantidade de CARB, PROT E GORDURAS e o NOME, e ele calcule o quanto de caloria por porção proporciona
-Criar uma pagina que eu terei que digitar quantas calorias totais eu quero preencher, e com isso eu poderei ir adicionando alimentos ja cadastrados para suprir essa caloria.
-No final de adicionar os alimentos para o total de calorias, calcular e mostrar na tela a % de cada macro.

"""

app = Flask(__name__)

@app.route('/')
def pagina_principal():
    teste = ['1','b','c']

    return render_template('index.html', gg=teste)

@app.route('/cadastro-alimento')
def cadastro_alimento():

    return render_template('cadastroAlimento.html')

@app.route('/calcular')
def calcular():

    return render_template('calcular.html')



app.run(debug=True)