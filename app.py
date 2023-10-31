from flask import Flask, request, render_template, flash, redirect, url_for
import pyodbc
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

server = '127.0.0.1'
database = 'PS_UserData'
username = 'sa'
password = 'Shaiya123@'

def create_connection():
    return pyodbc.connect(f"Driver={{SQL Server}};Server={server};Database={database};UID={username};PWD={password}")

@app.route('/', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        confirmar_senha = request.form['confirmar_senha']
        email = request.form['email']
        ip_cliente = request.remote_addr

        if not nome or not senha or not confirmar_senha or not email:
            flash('Por favor, preencha todos os campos.')
        elif senha != confirmar_senha:
            flash('As senhas não coincidem.')
        else:
            try:
                connection = create_connection()
                cursor = connection.cursor()

                query = f"SELECT * FROM Users_Master WHERE UserID = ? OR Enpassword = ?"
                cursor.execute(query, (nome, email))

                if cursor.fetchone():
                    flash('Usuário ou e-mail já existem no banco de dados.')
                else:
                    query = "SELECT MAX(UserUID) AS MaxUserUID FROM Users_Master"
                    cursor.execute(query)
                    max_user_uid = cursor.fetchone().MaxUserUID
                    next_user_uid = max_user_uid + 1

                    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    ano_atual = datetime.now().year
                    fim = ano_atual + 30

                    query = """INSERT INTO Users_Master (UserUID, UserID, Pw, JoinDate, Admin, AdminLevel, UseQueue, 
                               Status, Leave, LeaveDate, UserType, UserIp, Point, Enpassword, Birth, PwName, Email, UserCargo, ModiIp, ModiDate) 
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
                    cursor.execute(query, (next_user_uid, nome, senha, data_hora, 'False', '0', 'False', '0', '0', fim, 'C', ip_cliente, '0', email, ano_atual, 'PwName', email, 0, ip_cliente, data_hora))
                    connection.commit()

                    flash('Registro concluído com sucesso!')
            except Exception as e:
                flash(f'Erro ao inserir os dados: {str(e)}')
            finally:
                cursor.close()
                connection.close()
                
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
