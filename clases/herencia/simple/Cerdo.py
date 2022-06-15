from animales import Animales

class Pig(Animales):

    print('Constructur de clase hija ')
    def __init__(self, nombre = None, numero_chip = None, genero = None, 
                fecha_nacimeinto = None, granja=''):
        super().__init__(nombre, numero_chip, genero, fecha_nacimeinto)
        self.granja= granja
    def __del__(self):
        print('Destructur de clase hija ')

    def __str__(self):
        print('Tomar le sol')

    def entorno(self):
        print('Investigar el entorno')
    
    def detalles(self):
        super().detalles()
        print("Granja: {}".format(self.granja))
        print("***************************************")
    