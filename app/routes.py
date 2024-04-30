from app import app
from flask import render_template, redirect, url_for, flash, request
import mysql.connector
import os

mydb = mysql.connector.connect(
    host=os.environ.get('DB_HOST', 'localhost'),
    user=os.environ.get('DB_USER', 'root'),
    port=int(os.environ.get('DB_PORT', 3306)),
    password=os.environ.get('DB_PASSWORD', ''),
    database=os.environ.get('DB_DATABASE', 'bd')
)

@app.route('/')
def index_default():
    nome = "usuário"
    return render_template('index.html', nome=nome)

@app.route('/index/<nome>')
def index(nome):
    return render_template('index.html', nome=nome)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form['usuario']
    senha = request.form['senha']
    cursor = mydb.cursor()
    cursor.execute("SELECT nome FROM cadastro WHERE nome = %s AND senha = %s", (usuario, senha))
    usuarios_autenticados = cursor.fetchall()  # Busca todos os resultados
    cursor.close()  # Fecha o cursor após buscar todos os resultados
    if usuarios_autenticados:
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

@app.route('/deletar')
def deletar():
    return render_template('deletar.html')

@app.route('/deletado', methods=['POST'])
def deletado():
    usuario3 = request.form.get('usuario3')
    senha3 = request.form.get('senha3')
    cursor = mydb.cursor()
    sql = "DELETE FROM cadastro WHERE nome = %s AND senha = %s LIMIT 1"
    values = (usuario3, senha3)
    cursor.execute(sql, values)
    mydb.commit()
    if cursor.rowcount > 0:
        return f"Usuário: {usuario3} deletado com sucesso"
    else:
        flash("Conta inexistente")
        return redirect('/deletar')

@app.route('/atualizar')
def atualizar():
    return render_template('atualizar.html')

@app.route('/verificar', methods=['POST'])
def verificar():
    usuario4 = request.form['usuario4']
    senha4 = request.form['senha4']
    usuario5 = request.form['usuario5']
    senha5 = request.form['senha5']
    
    cursor = mydb.cursor()
    
    # Update the 'nome' and 'senha' columns where nome = usuario4 and senha = senha4
    cursor.execute("UPDATE cadastro SET nome = %s, senha = %s WHERE nome = %s AND senha = %s LIMIT 1", (usuario5, senha5, usuario4, senha4))

    # Commit the changes to the database
    mydb.commit()

    cursor.close()

    return redirect(url_for('atualizado'))

@app.route('/atualizado')
def atualizado():
    return render_template('atualizado.html')
