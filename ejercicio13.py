from flask import Flask, request, render_template
import mysql.connector
app = Flask(__name__)

hola = "HOLA HIJO DE PUTA: "
@app.route('/', methods=['GET'])
def bienvenida():
    return "AWAWA", 200
@app.route('/saludo/<nombre>', methods=['GET'])
def saludo(nombre):
    return hola + nombre, 200

@app.route('/formulario', methods=['GET'])
def formulario():
    titulo = "ER FORMULARIO"
    return render_template('formulario.html', titulo=titulo)

@app.route('/login', methods=['POST'])
def login():
    nombre = request.form.get('username')
    password = request.form.get('password')
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            port=3190,
            user="root",
            password="secret",
            database="cibera")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE codigo = %s AND clave = %s", (nombre, password))
        resultado = cursor.fetchone()
        if resultado is None:
            return "ACCESO DENEGADO", 403
        else:
            return "HOLA HIJO DE PUTA: "+ nombre, 200
    except:
        return "ERROR DE CONEXION A LA BASE DE DATOS", 500
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexion' in locals() and conexion.is_connected():
            conexion.close()

@app.route('/saludo2', methods=['GET'])
def saludo2():
    nombre = request.args.get('nombre')
    return hola + nombre, 200
app.run(host='0.0.0.0', port=4672)