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
"""Con el .__dict__ se verifica los atributos del objeto"""
print(objeto1.__dict__)
print(objeto2.__dict__)
print(objeto3.__dict__)
print(objeto4.__dict__)




