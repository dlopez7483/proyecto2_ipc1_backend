class comentarios:
 def __init__(self,cancion,comentario,usuario):
     self.cancion=cancion
     self.comentario=comentario
     self.usuario=usuario
   
 
 def getcancion(self):
     return self.cancion   
 
 def getcomentario(self):
     return self.comentario
 
 def getusuario(self):
     return self.usuario
 
 def setcancion(self,cancion):
     self.cancion=cancion
 
 def setcomentario(self,comentario):
     self.comentario=comentario
 
 def setusuario(self,usuario):
     self.usuario=usuario