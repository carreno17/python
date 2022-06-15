
from resultado import Resultado

objeto = Resultado(15, 6, 22, 7, 58, 46)

print("Hora: {}".format(objeto.relog()))
print("Fecha: {}".format(objeto.calendario()))
print("Hora/Fecha: {}".format(objeto))

"""El metodo .__mro__ nos ayuda haber si una clase tiene herencias, es decir
si tiene herencia con una clase o varias"""
print(Resultado.__mro__)#Aca vemos que la clase resultado tiene dos herencia,
#de dos clases padre,
