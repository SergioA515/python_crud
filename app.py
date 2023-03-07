""" 
    - CRUD basico con Flask
"""
#Importación de paquetes necesarios que nos brinda Flask para su entorno Web
from flask import Flask, render_template, request, redirect, url_for, flash
from db_config import mysql,app
from flask_mysqldb import MySQL
from flask import Flask
#Se inicializa la estructira y se definen los modulos necesarios ya importados


# conexión de mysql 
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'crud_example'
# mysql = MySQL(app)
# llave secreta que ayuda a compartir datos en una sesion

#comenzamos a definir las rutas de nuestra aplicación web
@app.route('/')
def Main_index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM user')
    data = cur.fetchall()
    return render_template('index.html', users = data)

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
        flash('Success') 
        return redirect(url_for('Main_index'))

@app.route('/updateUser/<id>', methods=['POST'])
def update_user(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE user
            SET fullname_user = %s, phone_user = %s, email_user = %s, password_user = %s
            WHERE id_user = %s
        """, (fullname, phone, email, password, id))
        flash('Contacto Actualizado')
        mysql.connection.commit()
        return redirect(url_for('app.Main_index'))

@app.route('/getUser/<id>', methods=['POST', 'GET'])
def get_user(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM user WHERE id_user = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edicion_usuario.html', users = data[0])

@app.route('/deleteUser')
def delete_user():
    return "<h1>Eliminar un Usuario</h1>"

port = 3306
if __name__=='__main__':
    app.run(port, debug=True)
