class usuarios:
 def __init__(self,nombre,apellido,user,contraseña):
   self.nombre=nombre
   self.apellido=apellido
   self.user=user
   self.contraseña=contraseña
 
 def getnombre(self):
   return self.nombre   
 
 def getapellido(self):
    return self.apellido
 
 def getcontraseña(self):
    return self.contraseña
 
 def getuser(self):
   return self.user 
 
 def setnombre(self,nombre):
   self.nombre=nombre
 
 def setapellido(self,apellido):
   self.apellido=apellido
 
 def setcontraseña(self,contraseña):
   self.contraseña=contraseña
 
 def setuser(self,user):
   self.user=user


