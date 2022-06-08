#La herencia es que un clase tome los atributos o metodos de otra 
class Animales: #clase padre

    def dormir(self):
        print('El animal duerme')
    

    def comer(self):
        print('El animal come')

class tamaño(Animales): #clase hija que asi vez herada la clase animales, es decir sus metodos, atributos

    def grande (self):
        print('El animal es grande')


    def pequeño(self):
        print('El animal es pequeño')

class perro(tamaño, Animales): #Hereda los atributos, metodos de las dos clases
    
    def __init__(self, nombre):
        self.nombre = nombre 
        
    
    def comer(self):
        super().comer() #Acá llamo todos los metodos que tenga por nombre comer
        #De cualquier clase
        print(f"{self.nombre} come")


#creo un objeto en la class perro
objeto = perro("Doby")
 
#El objeto puede heredad todos los atributos, metodos de las otra clases
objeto.dormir()
objeto.comer()
objeto.grande()
objeto.pequeño()
