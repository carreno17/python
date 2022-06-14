import os

funcion_fichero = os.path.dirname(__file__)
fichero = open(f"{funcion_fichero}/texto2.txt")

#El .read se usa leer todo lo que tiene el fichero
#print(fichero.read())

#fichero.close()


"""#con for podemos leer linea por linea el fichero
for linea in fichero:
    print(linea)"""

"""#Para eleer un fichero por indices 

print(fichero.read(10)) #Me lee todo desde el 0 hasta el indice 10
"""
"""#.readline me muestra linea por linea dependiendo si por ejemplo hago un solo print
#me mostrará solo la linea 1 si hago dos print me mostrará la dos linea 1 y dos

print(fichero.readline())"""

#El .readlines me va a mostrar todas las linea en una lista

print(fichero.readlines())