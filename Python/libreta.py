from contacto import Contacto
class Libreta():
    def __init__(self):
        self.__coleccion_contactos=[]
        
    @property
    def coleccion_contactos(self) ->list:
        return self.__coleccion_contactos
    
    @coleccion_contactos.setter
    def coleccion_contactos(self,otraColeccion_contactos):
        self.__coleccion_contactos=otraColeccion_contactos;
    
    def añadir_Contacto(self,contacto:Contacto):
        self.coleccion_contactos.append(contacto)
        return print("¡Contacto agregado con exito!") 
    
    def buscar_Contacto(self,nombree:str,apellido:str):
        if len(self.coleccion_contactos)==0:
            return print("la lista de contactos esta vacia")
        else:
            for corredor in self.__coleccion_contactos:
                corredor: Contacto
                if corredor.nombre == nombree and corredor.apellido==apellido:
                    return corredor
                
    def lista_de_Contacto(self):
        contador=1
        for corredor in self.__coleccion_contactos:
            corredor:Contacto
            print("Contacto:",contador)
            print("Nombre:",corredor.nombre)
            print("Apellido:",corredor.apellido)
            print("Celular:",corredor.celular)
            print("Gmail:",corredor.gmail)
            print("--------------------")
            contador+=1
            
    