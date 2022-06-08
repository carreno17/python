""" Las tuplas son iguales que las lista. La diferencia es que se usa
() y en la lista es [], las tuplas no se pueden modificar, solo se pueden 
consultar sus elementos. Dentro de una tupla podemos agregar una lista y 
tambien otra tupla. Las tuplas son mas rapidas que las lista porque no
se pueden modificar"""

tupla = ("Hola", 10, 40.36, True, [1, 4, 5], (9,11,46))
print(tupla)
print(tupla[4][0])
"""Lo que hago es que digo que quiero imprimir el valor de de la tupla
en el indice 4 el cual es una lista, de esta lista quiero imprimer el valor
del indice 0"""
#Creando una sub tupla
sub_tupla = tupla [0:4]
print(sub_tupla)

#Usando Tuplas y lista

cursos = ["Python", "Go", "Php", "Java"] #Esto es una lista []
print(cursos)
#Guardando una lista en un tupla ()
cursos_tupla = tuple(cursos)
print(cursos_tupla)

niveles = ("Basico", "Intermedio", "Avanzado") #Esto es una tupla
print(niveles)
#Guardando una tupla en una lista
niveles_lista = list(niveles)
print(niveles_lista)