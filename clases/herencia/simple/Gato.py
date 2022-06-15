from animales import Animales

class Cat(Animales):

    print('Constructur de clase hija ')
    def __init__(self, nombre = None, numero_chip = None, genero = None, 
                fecha_nacimeinto = None, estado = ""):
        super().__init__(nombre, numero_chip, genero, fecha_nacimeinto)
        self.estado = estado
   
    def __del__(self):
        print('Destructur de clase hija ')

    def __str__(self):
        print('Escalar')

    def saltar():
        print('Saltar')
    
    def detalles(self):#Acá estoy aplicando polimofirmos
        super().detalles()
        print("Estado: {}".format(self.estado))
        print("***************************************")
    