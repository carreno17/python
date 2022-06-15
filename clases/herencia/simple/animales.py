
class Animales:

    def __init__(self, nombre, numero_chip, genero, fecha_nacimeinto):
        print('Probando el constructor en la clase padre')
        if (nombre == None or numero_chip == None or genero == None or
            fecha_nacimeinto == None):
                raise ValueError ("Todos los campos son obligatorios")
        self.nombre = nombre
        self.numero_chip = int(numero_chip)
        self.genero = genero
        self.fecha_nacimiento = fecha_nacimeinto
        
    def __del__(self):
        print('Probando el destructor en la clase padre')

    def detalles(self): #el termino __str__ se usa para mostar un objeto dentro de una lista
       print("Nombre: {}".format(self.nombre))
       print("Numero Chip: {}".format(self.numero_chip))  
       print("Genero: {}".format(self.genero))  
       print("Fecha nacimiento: {}".format(self.fecha_nacimiento))  

