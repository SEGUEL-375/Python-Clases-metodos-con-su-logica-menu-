class Contacto() :
    def __init__(self,nombre:str,apellido:str,celular:int,gmail:str):
        self.__nombre=nombre
        self.__celular=celular
        self.__gmail=gmail
        self.__apellido=apellido
        
        
    @property
    def nombre(self) ->str:
        return self.__nombre;
    
    @nombre.setter
    def nombre(self,otroNombre):
        self.__nombre=otroNombre;
        
    @property
    def apellido(self) ->str:
        return self.__apellido;
    
    @apellido.setter
    def apellido(self,otroApellido):
        self.__apellido=otroApellido;    
    
    @property
    def celular(self) ->int:
        return self.__celular;
    
    @celular.setter
    def celular(self,otroCelular):
        self.__celular=otroCelular;
    
    @property
    def gmail(self) ->str:
        return self.__gmail;
    
    @gmail.setter
    def gmail(self,otroGmail):
        self.__gmail=otroGmail;

    def __str__(self):
            return "nombre: {} apellido: {} email: {}".format(self.nombre,self.__apellido,self.__gmail)    
    
    def __int__(self):
            return "celular: {}".format(self.celular)
            