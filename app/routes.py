from app import app
from flask import render_template, redirect, url_for
from flask import request

lista = []

@app.route('/')
def index_default():
    nome = "usuário"  
    return render_template('index.html', nome=nome)

@app.route('/index/<nome>')
def index(nome):
    return render_template('index.html', nome=nome)

@app.route ('/login')
def login ():
    return render_template('login.html')

@app.route ('/autenticar', methods=['GET'])
def autenticar ():
    usuario = request.args.get('usuario')
    senha = request.args.get('senha')
    return redirect(url_for('index', nome=usuario))



@app.route('/registrar')
def registrar():
    return render_template('registrar.html')

    
@app.route('/autenticar1', methods=['POST'])
def autenticar1():
    usuario1 = request.form.get('usuario1')
    senha1 = request.form.get('senha1')
    return redirect(url_for('registrado', usuario1=usuario1))

@app.route('/registrado')
def registrado ():
    usuario1 = request.args.get('usuario1')
    return render_template('registrado.html', usuario1=usuario1)
