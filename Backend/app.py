##Librerias Importadas
from webbrowser import get
from flask import Flask,jsonify, request
from flask_cors import CORS
import json

#Importaciones de Clases 
from Usuario import Usuario
from Libro import Libro

#Lista de Usuarios
Usuarios = []
Usuarios.append(Usuario('a13','Kevin','Usuario_Usac','123456','25','Ingenieria sistemas','201902278'))
Usuarios.append(Usuario('a12','Dylan','Usuario_Usac1','123456','25','Ingenieria sistemas','201902279'))
#Lista de Libros
Libros =[]
Libros.append(Libro('100','don quijote','novela','nose','100','50','50','2021','usac'))
#Creación del Entorno de Flask
app= Flask(__name__)
CORS(app)##para que llegue la informacion de forma segura

#Mostrar un Mensaje en Pantalla
@app.route('/', methods =["GET"])
def Inicio():
    return('<h1>Hola Mundo</h1>')
#METODO PARA MOSTRAR USUARIOS
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
        "Mensaje":"El Usuario no existe "
    }))

#METODO CREAR SIN VALIDACION
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
@app.route('/user/verificar',methods=["POST"])
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


#METODO PARA VERIFICAR SI EL USUARIO EXISTE
def VerificarUsuario(nusuario):
    global Usuarios
    validar = False
    for Usuario in Usuarios:
        if str(nusuario) == str(Usuario.getid_user()):
            validar =True
    return validar
#METODO CREAR USUARIO CON VALIDACION
@app.route('/user/crearval',methods=["POST"])
def AgregarUserVAL():
    global Usuarios
    try:
        iduser = request.json["id_user"]
        nombre = request.json["user_display_name"]
        nick =   request.json["user_nickname"]
        password = request.json["user_password"]
        age = request.json["user_age"]
        career = request.json["user_career"]
        carnet = request.json["user_carnet"]
        if VerificarUsuario(iduser)== False:
            Usuarios.append(Usuario(iduser,nombre,nick,password,age,career,carnet))
            return(jsonify({
                "Mensaje":"Se agregó el usuario correctamente"
            }))
        else:
            return(jsonify({
                "Mensaje":"Por favor cree un nuevo id "
            }))        
    except:
            return(jsonify({
                "Mensaje":"response"
            }))
#METODO PARA MOSTRAR LIBROS
@app.route('/book/show',methods=["GET"])
def MostarLibros():
    global Libros
    books=[]
    for lib in Libros:
        objeto1={
            "id_book": lib.getid_book(),
            "book_title": lib.getbook_title(),
            "book_type": lib.getbook_type(),
            "author": lib.getauthor(),
            "book_count": lib.getbook_count(),
            "book_available": lib.getbook_available(),
            "book_not_available": lib.getbook_not_available(),
            "book_year": lib.getbook_year(),
            "book_editorial": lib.getbook_editorial()
        }
        books.append(objeto1)
    return(jsonify(books) )
#METODO PARA VERIFICAR SI EL LIBRO EXISTE
def VerificarLibro(nlibro):
    global Libros
    validar = False
    for Libro in Libros:
        if str(nlibro) == str(Libro.getid_book()):
            validar =True
    return validar           
#METODO CREAR LIBRO CON VALIDACION
@app.route('/book',methods=["POST"])
def Agregarbook():
    global Libros
    try:
        idbook = request.json["id_book"]
        booktitle = request.json["book_title"]
        tipo =   request.json["book_type"]
        autor = request.json["author"]
        bc = request.json["book_count"]
        ba = request.json["book_available"]
        bna = request.json["book_not_available"]
        by = request.json["book_year"]
        be = request.json["book_editorial"]
        if VerificarLibro(idbook)== False:
            Libros.append(Libro(idbook,booktitle,tipo,autor,bc,ba,bna,by,be))
            return(jsonify({
                "Mensaje":"Se agregó el libro correctamente"
            }))
        else:
            return(jsonify({
                "Mensaje":"Por favor cree un nuevo id "
            }))        
    except:
            return(jsonify({
                "Mensaje":"response"
            }))
#METODO PARA ACTUALIZAR LIBRO 
@app.route('/book/actualizar/<string:buk>', methods=['PUT'])
def Actualizarlibro(buk):
    global Libros
    idbook = request.json["id_book"]
    booktitle = request.json["book_title"]
    tipo =   request.json["book_type"]
    autor = request.json["author"]
    bc = request.json["book_count"]
    ba = request.json["book_available"]
    bna = request.json["book_not_available"]
    by = request.json["book_year"]
    be = request.json["book_editorial"]
    for i in range(len(Libros)):
        if buk ==  Libros[i].getid_book():
            Libros[i].setid_book(idbook)
            Libros[i].setbook_title(booktitle)
            Libros[i].setbook_type(tipo)
            Libros[i].setauthor(autor)
            Libros[i].setbook_count(bc)
            Libros[i].setbook_available(ba)
            Libros[i].setbook_not_available(bna)
            Libros[i].setbook_book_year(by)
            Libros[i].setbook_editorial(be)
            return(jsonify({
                "Mensaje":"Se actualizó con exito"
            }))
    return(jsonify({
        "Mensaje":"No se encontró el usuario"
            }))
#Levantar la AP
#Levantar la API
if __name__ == "__main__":
    app.run(host ="localhost", port=3000, debug= True )##para que se ejecute

