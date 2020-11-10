from flask import Flask, jsonify, request
from flask_cors import CORS
from usuarios import usuarios
from canciones import canciones
from comentarios import comentarios
app = Flask(__name__)
CORS(app)
U =[]
C=[]
C2=[]
C3=[]
coment=[]
contador_songs=0
U.append(usuarios("Usuario","Maestro","admin","admin"))
@app.route("/", methods=["GET"])
def rutaInicial():
  #print("Ahh")
  return("inicio")

@app.route("/usuarios/", methods=["GET"])
def rutaotra():
  #print("Ahh")
  global U
  Datos=[]
  for usw in U:
   Dato={
     'nombre': usw.getnombre(),
     'apellido': usw.getapellido(),
     'user': usw.getuser(),
     'contraseña': usw.getcontraseña()
     }
   Datos.append(Dato)
  res = jsonify(Datos)
  return(res) 




@app.route("/canciones/", methods=["GET"])
def rutapostcanciones():
  #print("Ahh")
 global C,C2
 Datos2=[]
 for c in C:
   Dato2={
   'id': c.getid(),  
   'nombre': c.getnombre(),
   'artista': c.getartista(),
   'album': c.getalbum(),
   'imagen': c.getimagen(),
   'fecha': c.getfecha(),
   'linkspotify': c.getlinkspotify(),
   'linkyoutube': c.getlinkyoutube()
   }
   Datos2.append(Dato2)
 res = jsonify(Datos2)
 return(res)  
 
@app.route("/canciones/<string:song>/", methods=["GET"])
def rutapostcanciones3(song):
  #print("Ahh")
 global C,C2
 for c in C2:
   if c.getnombre()== song: 
     a = c.getid()
     a2 = c.getnombre()
     a3 = c.getartista()
     a4 = c.getfecha()
     a5 = c.getimagen()
     a6 = c.getalbum()
     a7 = c.getlinkspotify()
     a8 = c.getlinkyoutube()
     dato={
     'id': a,
     'nombre':a2,
     'artista':a3,
     'fecha':a4,
     'imagen':a5,
     'album':a6,
     'linkspotify':a7,
     'linkyoutube':a8
     }
     res = jsonify(dato)
 return(res)  

@app.route("/canciones/<int:song>/", methods=["POST"])
def rutapostcancionesggg(song):
  #print("Ahh")
 global C,C2
 for c in C:
   if c.getid() == song:
     nuevo = canciones(c.getid(),c.getnombre(),c.getartista(),c.getalbum(),c.getimagen(),c.getfecha(),c.getlinkspotify(),c.getlinkyoutube())
     C2.append(nuevo)
     dato={
     'message':'agregado '
     }
     break
 response = jsonify(dato)
 return(response)            

@app.route("/canciones/3<int:song>/", methods=["POST"])
def rutapostcancionesjjj(song):
  #print("Ahh")
 global C2,C3
 for c in C2:
   if c.getid() == song:
     nuevo = canciones(c.getid(),c.getnombre(),c.getartista(),c.getalbum(),c.getimagen(),c.getfecha(),c.getlinkspotify(),c.getlinkyoutube())
     C3.append(nuevo)
     dato={
     'message':'agregado a playlist '
     }
     break
 response = jsonify(dato)
 return(response)  

@app.route("/canciones/3<string:song>/", methods=["GET"])
def rutapostcancioness3(song):
  #print("Ahh")
 global C,C2,C3
 for c in C3:
   if c.getnombre()== song: 
     a = c.getid()
     a2 = c.getnombre()
     a3 = c.getartista()
     a4 = c.getfecha()
     a5 = c.getimagen()
     a6 = c.getalbum()
     a7 = c.getlinkspotify()
     a8 = c.getlinkyoutube()
     dato={
     'id': a,
     'nombre':a2,
     'artista':a3,
     'fecha':a4,
     'imagen':a5,
     'album':a6,
     'linkspotify':a7,
     'linkyoutube':a8
     }
     res = jsonify(dato)
 return(res) 

    
 

@app.route("/usuarios/<string:user>/", methods=["GET"])
def obtenerusuario(user):
 global U
 Datos=[]
 for usw in U:
   if usw.getuser() == user:
     Dato={
     'nombre': usw.getnombre(),
     'apellido': usw.getapellido(),
     'user': usw.getuser(),
     'contraseña': usw.getcontraseña()
     }
     break
 return  jsonify(Dato)     
  
         
 

@app.route("/canciones/<int:song>/", methods=["GET"])
def obtenercancionagregada(song):
  global C2
  Datos=[]
  for c2 in C2:
   if c2.getid() == song:
         Dato={
         'nombre': c2.getnombre(),
         'artista': c2.getartista(),
         'album': c2.getalbum(),
         'imagen': c2.getimagen(),
         'fecha': c2.getfecha(),
         'linkspotify': c2.getlinkspotify(),
         'linkyoutube': c2.getlinkyoutube()
         }
         Datos.append(Dato)
         break
  res = jsonify(Datos)
  return(res)   
  
@app.route("/canciones/2<int:song>/", methods=["GET"])
def obtenercancionagregadas2(song):
  global C2,C
  Datos=[]
  a=0
  a2=""
  a3=""
  a5=""
  a6=""
  a7=""
  a8=""
  for c2 in C:
   if c2.getid() == song:
         a = c2.getid()
         a2= c2.getnombre()
         a3 = c2.getartista()
         a4= c2.getalbum()
         a5 = c2.getfecha()
         a6 = c2.getimagen()
         a7 = c2.getlinkspotify()
         a8 = c2.getlinkyoutube()
         break
  Dato ={
  'id':a,
  'nombre':a2,
  'artista':a3,
  'album':a4,
  'fecha':a5,
  'imagen':a6,
  'linkspotify':a7,
  'linkyoutube':a8
 }      
  
  res = jsonify(Dato)
  return(res)  

@app.route("/usuarios/<string:user>/", methods=["PUT"]) 
def modificar_usuario(user):
  #print("Ahh")
  global U
  
  for i in range(len(U)):
   if user == U[i].getuser():
     U[i].setnombre(request.json['nombre'])
     U[i].setapellido(request.json['apellido'])
     U[i].setuser(request.json['user'])
     U[i].setcontraseña(request.json['contraseña'])
     dato ={
     'message' :'actualizado'
     }
     response = jsonify(dato)
     return(response)
    



@app.route("/usuarios/", methods=["POST"])
def Agregarusuario():
 global U
 variable = True
 nombre = request.json['nombre']
 apellido = request.json['apellido']
 usuario = request.json['user']
 contraseña = request.json['contraseña']
 for i in range(len(U)):
   if U[i].getuser()==usuario:
     variable= False
     break
   else:
     variable=True   
 if variable:
   nuevo = usuarios(nombre,apellido,usuario,contraseña)
   U.append(nuevo)
   Dato ={
     'message':'usuario agregado'
   }
 else:
   Dato ={
     'message':'nel'
   }
 response= jsonify(Dato)
 return(response)

 
 
@app.route("/comentarios/", methods=["POST"])
def Agregarcoment():
 global coment
 cancion = request.json['cancion']
 comentario = request.json['comentario']
 usuario = request.json['usuario']
 nuevo = comentarios(cancion,comentario,usuario)
 coment.append(nuevo)
 return jsonify({'message':'comentario agregado'})

@app.route("/comentarios/", methods=["GET"])
def vercoment():
 global coment
 Data2=[]
 for comentario  in coment:
   Dato2={
   'comentario': comentario.getcomentario(),
   'cancion': comentario.getcancion(),
   'usuario': comentario.getusuario()
   }
   Data2.append(Dato2)
 res = jsonify(Data2)
 return(res)
 


 


 

@app.route("/canciones/", methods=["POST"])
def Agregarcancione():
 global C, contador_songs
 id2 = contador_songs
 nombre2 = request.json['nombre']
 artista2 = request.json['artista']
 album2 = request.json['album']
 imagen2 = request.json['imagen']
 fecha2 = request.json['fecha']
 linkspotify2 =request.json['linkspotify']
 linkyoutube2 = request.json['linkyoutube']
 new = canciones(id2,nombre2,artista2,album2,imagen2,fecha2,linkspotify2,linkyoutube2)
 C.append(new) 
 contador_songs+=1
 Dato ={
 'message':'agregada'
 }
 response = jsonify(Dato)
 return(response)

 
@app.route("/login/", methods=["POST"])
def acceso():
  global U
  username = request.json['user']
  password = request.json['contraseña']
  for usuario in U:
      if usuario.getuser()==username and usuario.getcontraseña()==password:
        Dato ={
         'message': 'acceso',
         'user': usuario.getuser()
         }
        break
      else:
        Dato={
          'message':'Nelprro',
          'user': ''
          }
  response = jsonify(Dato)
  return(response)

@app.route("/usuarios/<string:usuario>/", methods=["DELETE"])
def eliminar(usuario):
  global U
  for i in range(len(U)):
   if usuario == U[i].getuser():
     del U[i]
     break
  return jsonify({'message':'Se elimino el usuario'})

@app.route("/canciones/<string:song>/", methods=["DELETE"])
def eliminar2(song):
  global C
  for i in range(len(C)):
   if song == C[i].getnombre():
     del C[i]
     break
  return jsonify({'message':'Se elimino la cancion'})

if __name__=="_main_":
 app.run(threaded=True,host="0.0.0.0",port=5000,debug=True)



