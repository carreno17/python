"""metodo __init__ este nos sirve para que varios objetos que pertenesca a una
misma clase, tengan los atributos"""

class Usuarios:

    #el parametro self se refie al misma funcion
    #Al igual que las funciones, a las clases se le pueden pasar parametro
    #por defaul un ejemplo seria nombre='', apellido=''
    def __init__(self, nombre='', apellido=''):
        self.nombre = nombre #Creando objetos, aca le paso los paramentros
        self.apellido = apellido

objeto1 = Usuarios("David", "Lozada")#ACÁ le estoy pasando los dos parametros que estableci, nombre y apellido
objeto2 = Usuarios("Alfredo", "Alvarez")
objeto3 = Usuarios("Maria", "Duarte")
objeto4 = Usuarios() #acá me va tomar el nombre y apellido por defaul
#Al imprimir todo los objetos tendrán el mismo atributo
print(objeto1.__dict__)
print(objeto2.__dict__)
print(objeto3.__dict__)
print(objeto4.__dict__)




#METODO PARA CLASES
#Para definir un metodo que sea de tipo clase se usa @classmethod""
class Circulo:

    pi= 3.1416 
    @classmethod
    def area(cls, radio): #Cls es igual asi la misma función que sefl en los metodos de objetos
        return cls.pi * (radio ** 2)

print("El area del circulo es:", Circulo.area(10))