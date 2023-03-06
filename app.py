""" 
    - CRUD basico con Flask
"""
#Importación de paquetes necesarios que nos brinda Flask para su entorno Web
from flask import Flask, render_template, request
#import config.db_config as db
from flask_mysqldb import MySQL
from flask import Flask
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'crud_example'
mysql = MySQL(app)
#Se inicializa la estructira y se definen los modulos necesarios ya importados
app = Flask(__name__)
mysql = MySQL(app)

#comenzamos a defiir las rutas de nuestra aplicación web
@app.route('/')
def main_index():
    return render_template('index.html')

@app.route('/createUser', methods=['POST'])
def create_user():
    if request.method == 'POST':
        fullname= request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user (fullname_user, phone_user, email_user, password_user) VALUES (%s, %s, %s, %s)",(fullname, phone, email, password))
        mysql.connection.commit()
        return 'Done'

@app.route('/getUser')
def get_user():
    return "<h1>Formulario para Obtener un Usuario</h1>"

@app.route('/updateUser')
def update_user():
    return "<h1>Formulario para Actualizar un Usuario</h1>"

@app.route('/deleteUser')
def delete_user():
    return "<h1>Eliminar un Usuario</h1>"

port = 3306
if __name__=='__main__':
    app.run(port, debug=True)
