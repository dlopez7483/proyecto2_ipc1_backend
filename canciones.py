class canciones:
 def __init__(self,id,nombre,artista,album,imagen,fecha,linkspotify,linkyoutube):
     self.nombre=nombre
     self.artista=artista
     self.album=album
     self.imagen=imagen
     self.fecha=fecha
     self.linkspotify=linkspotify
     self.linkyoutube=linkyoutube
     self.id=id

 def getid(self):
     return self.id 


 def getnombre(self):
     return self.nombre 

 def getartista(self):
     return self.artista
 
 def getalbum(self):
     return self.album
 
 def getimagen(self):
     return self.imagen
 
 def getfecha(self):
     return self.fecha

 def getlinkspotify(self):
     return self.linkspotify
  
 def getlinkyoutube(self):
     return self.linkyoutube

 def setnombre(self,nombre):
   self.nombre=nombre     

 def setartista(self,artista):
     self.artista=artista
 
 def setid(self,id):
     self.id=id

 def setalbum(self,album):
     self.album=album

 def setimagen(self,imagen):
     self.imagen=imagen

 def setfecha(self,fecha):
     self.fecha=fecha
 
 def setlinkspotify(self,linkspotify):
     self.linkspotify=linkspotify 

 def setlinkyoutube(self,linkyoutube):
     self.linkyoutube=linkyoutube