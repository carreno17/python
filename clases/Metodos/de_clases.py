
#METODO PARA CLASES
#Para definir un metodo que sea de tipo clase se usa @classmethod""
class Circulo:

    pi= 3.1416 
    @classmethod
    def area(cls, radio): #Cls es igual asi la misma función que sefl en los metodos de objetos
        return cls.pi * (radio ** 2)

print("El area del circulo es:", Circulo.area(10))