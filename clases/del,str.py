#__del__ es un metodo para borrar un objeto, conocido como el destructor
# self.__class__.__name__ se utiliza para saber el nombre de la calse
class Deportes:
    
    def __init__(self, tipo, nombre, reglas):
        self.tipo =  str(tipo)
        self.nombre = str(nombre)
        self.reglas = str(reglas)      

    def __del__ (self):
        print('Se elemino un objeto de la clase: {}'
            .format(self.__class__.__name__))
    """
    #El str es una función para imprimir los resultados, podemos dejarlo con
    str o colocarle un nombre
    def __str__(self):
        return "Tipo: {}, Nombre: {},  Reglas: {}".format(self.tipo,  self.nombre , self.reglas )
    """
    #Esto es agregarle metodos a una clase para que imprima resultados
    #con otro nombe, si le coloco otro nombre debo llamar la funcion
    def detalles (self):
        print("Tipo: {}".format(self.tipo))
        print("Nombre: {}".format(self.nombre)) 
        print("Reglas: {}".format(self.reglas)) 


objecto_1 = Deportes('Artes marciales', 'Karate', 'Solo se puede con dos juegadores')

objecto_1.detalles()

objecto_2 = Deportes('Futbol', 'futbol sala', 'Solo se puede 10 jugadores')

objecto_2.detalles()

