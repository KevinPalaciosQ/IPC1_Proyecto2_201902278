##Librerias Importadas
from webbrowser import get
from flask import Flask,jsonify, request
from flask_cors import CORS
import json

#Importaciones de Clases 
from Usuario import Usuario
#Lista de Usuarios
Usuarios = []
Usuarios.append(Usuario('a13','Kevin','Usuario_Usac','123456','25','Ingenieria sistemas','201902278'))
Usuarios.append(Usuario('a12','Dylan','Usuario_Usac1','123456','25','Ingenieria sistemas','201902279'))
#Creación del Entorno de Flask
app= Flask(__name__)
CORS(app)##para que llegue la informacion de forma segura
#METODO GET
#Método Utilizado para leer datos
#Mostrar un Mensaje en Pantalla
@app.route('/', methods =["GET"])
def Inicio():
    return('<h1>Hola Mundo</h1>')
#Mostrar Usuarios
@app.route('/user',methods=["GET"])
def MostarUsuarios():
    global Usuarios
    Users=[]
    for user in Usuarios:
        objeto={
            "id_user": user.getid_user(),
            "user_display_name": user.getuser_display_name(),
            "user_nickname": user.getuser_nickname(),
            "user_password": user.getuser_password(),
            "user_age": user.getuser_age(),
            "user_career": user.getuser_career(),
            "user_carnet": user.getuser_carnet()
        }
        Users.append(objeto)
    return(jsonify(Users) )
#MOSTRAR UN USUARIO EN ESPECIFICO
@app.route('/user/<string:user>',methods=["GET"])
def MostrarUsuario(user):
    global Usuarios
    for i in range(len(Usuarios)):
        if Usuarios[i].getuser_display_name() == user:
            objeto= {
            "id_user": Usuarios[i].getid_user(),
            "user_display_name": Usuarios[i].getuser_display_name(),
            "user_nickname": Usuarios[i].getuser_nickname(),
            "user_password": Usuarios[i].getuser_password(),
            "user_age": Usuarios[i].getuser_age(),
            "user_career": Usuarios[i].getuser_career(),
            "user_carnet": Usuarios[i].getuser_carnet()
            }
            return(jsonify(objeto))
    return(jsonify({
        "Mensaje":"No se encontró el Usuario "
    }))

#METODO POST
@app.route('/user/crear',methods=["POST"])
def AgregarUser():
    global Usuarios
    iduser = request.json["id_user"]
    nombre = request.json["user_display_name"]
    nick =   request.json["user_nickname"]
    password = request.json["user_password"]
    age = request.json["user_age"]
    career = request.json["user_career"]
    carnet = request.json["user_carnet"]
    Usuarios.append(Usuario(iduser,nombre,nick,password,age,career,carnet))
    return(jsonify({
        "Mensaje":"Se agregó el usuario correctamente"
    }))

#VALIDAR USUARIO 
#METODO POST
@app.route('/user/verificar',methods=["POST"])
def VerificarUser():
    global Usuarios
    nick =   request.json["user_nickname"]
    for i in range(len(Usuarios)):
        if nick == Usuarios[i].getuser_nickname():
            return(jsonify({
        "Mensaje":"Bienvenido Usuario"
    })) 
    return(jsonify({
        "Mensaje":"Intruso"
    }))
@app.route('/user/verificar1',methods=["POST"])
def VerificarUser2():
    global Usuarios
    nick =   request.json["user_nickname"]
    password = request.json["user_password"]
    for i in range(len(Usuarios)):
        if nick == Usuarios[i].getuser_nickname() and password==Usuarios[i].getuser_password():
            objeto= {
            "id_user": Usuarios[i].getid_user(),
            "user_display_name": Usuarios[i].getuser_display_name(),
            "user_nickname": Usuarios[i].getuser_nickname(),
            "user_password": Usuarios[i].getuser_password(),
            "user_age": Usuarios[i].getuser_age(),
            "user_career": Usuarios[i].getuser_career(),
            "user_carnet": Usuarios[i].getuser_carnet()
            }
            return(jsonify(objeto)) 
    return(jsonify({
        "Mensaje":"El Usuario No Existe"
    }))

#Levantar la API
if __name__ == "__main__":
    app.run(host ="localhost", port=3000, debug= True )##para que se ejecute

