#Funciones lambdas nos sirve para declara una funcion en una linea
#Dentro de una variable

from ast import arg


funcion_lambdas = lambda n1, n2 : n1+n2
#Estructura lambda (parametros) : <instruciones (cuerpo de funcion)>
print(funcion_lambdas(10, 40))


"Está tambien se pueden realizar de otras formas"
suma_3_numeros = lambda n1, n2, n3 : n1+n2+n3
print(suma_3_numeros(10,20,30))

