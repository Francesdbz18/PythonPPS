from flask import Flask, request, render_template
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
    if nombre == "root" and password == "1234":
        return "HOLA HIJO DE PUTA: "+ nombre, 200
    return "ACCESO DENEGADO", 403

@app.route('/saludo2', methods=['GET'])
def saludo2():
    nombre = request.args.get('nombre')
    return hola + nombre, 200
app.run(host='0.0.0.0', port=4672)