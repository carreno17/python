from animales import Animales

class Dog(Animales):
    
    print('Constructur de clase hija ')
    def __init__( self, nombre = None, numero_chip = None, genero = None, 
                fecha_nacimeinto = None, domicilio=''):
        super().__init__(nombre, numero_chip, genero, fecha_nacimeinto)
        self.domicilio= domicilio
    def __del__(self):
        print('Destructur de clase hija ')

    def __str__(self):
        print('Limpiar')
    
    def detalles(self):
        super().detalles()
        print("Domicilio: {}".format(self.domicilio))
        print("***************************************")
    



