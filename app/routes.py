from app import app
from flask import render_template, redirect, url_for
from flask import request
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd'
)


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

@app.route ('/autenticar', methods=['POST'])
def autenticar ():
    usuario = request.form['usuario']
    senha = request.form['senha']
    cursor = mydb.cursor()
    cursor.execute("SELECT nome FROM cadastro WHERE nome = %s AND senha = %s", (usuario, senha))
    usuario_autenticado = cursor.fetchone()
    cursor.close()
    if usuario_autenticado:
        return redirect(url_for('index', nome=usuario))
    else:
        return render_template('alerta.html', erro="Credenciais inválidas. Tente novamente.")


@app.route('/registrar')
def registrar():
    return render_template('registrar.html')

    
@app.route('/autenticar1', methods=['POST'])
def autenticar1():
    usuario1 = request.form.get('usuario1')
    senha1 = request.form.get('senha1')
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO cadastro (nome, senha) VALUES (%s, %s)", (usuario1, senha1))
    mydb.commit()
    cursor.close()
    return redirect(url_for('registrado', usuario1=usuario1))

@app.route('/registrado')
def registrado():
    cursor = mydb.cursor()
    cursor.execute("SELECT nome FROM cadastro ORDER BY id DESC LIMIT 1")
    usuario1 = cursor.fetchone()
    cursor.close()
    return render_template('registrado.html', usuario1=usuario1)

