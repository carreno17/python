#* El asterisco nos sirve para encerrar equis cantidad de valores en una tupla
#sum lo que nos hace es sumar todos los valores una lista u tupla
#len nos dice cuantos elementos hay en una lista o tupla
from ast import arg


def promedio_notas(notas):
    return sum(notas) / len(notas)

resultado = promedio_notas([10, 50, 60])
print(resultado)
"""Sin el * tenemos que pasar los valores dentrol de una lista o tupla
porque solo podemos imprimir un argumento"""

""" En cambio con el * nos convierte varios argumentos en una lista o tupla.
Cuando usamos el *es recomendable llamar la variable *args
"""
def promedio_notas(*args):
    return sum(args) / len(args)

resultado = promedio_notas(10, 50, 60)
print(resultado)

#** nos encerriera los termino en un diccionario, se usa **Kwargs para nombrar
#por la comunidad de python

def combinacion (*args, **kwargs):
    print(args)
    print(kwargs)

combinacion(10,50,80,curso="python", edad=19)