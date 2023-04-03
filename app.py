from flask import Flask, render_template# """ importa classe flasc """

app = Flask("__name__") #""" cria uma instnância dessa classe """

@app.route("/")          #""" cria rotas com o decorator """
def index():
    return render_template("index.html")

@app.route("/")          
def quemsomos():
    return render_template("/quemsomos.html")

@app.route("/")          
def contatos():
    return render_template("/contatos.html")

