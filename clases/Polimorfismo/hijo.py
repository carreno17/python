"""Esto es polimorfismo, es decir me traigo una función que ya existe en la clase
y la sobresescribo es decir cambiar todo lo que está contiene, pero yo tambien
puedo traerme la el contenido que tiene la función saluda e imprimirlo y 
mostrar los dos PRINT en este caso el cual es EL PADRE NOS SALUDA Y EL
EL HIJO NOS SALUDA"""
from padre import Padre
class Hijo(Padre):

    def saluda(self):
        
        super().saludo()#Acá estoy trayendo la funcion saluda de la clase padre
        print('!El hijo nos saluda!')#Acá estoy utilizando la misma función de
        #Clase padre pero cambio su contenido