
import os
#"a" se usa para agregar más cosas a un fichero
#"w" se usa para cambiar todo lo de ese fichero y que quede solo lo que tu
#acabas de agregar
#"x" es para crear un fichero en caso de que no exista

"""#Utilzando el metodo "a"
#en caso de que no exista el fichero me lo crea
llamando_import = os.path.dirname(__file__)
anadir_fichero = input('Ingresa lo que deseas añadir al fichero: ')
fichero = open(f"{llamando_import}/texto_a.txt", "a")
fichero.write(anadir_fichero)

#Vuelvo a llamar el fichero pero sin la a
fichero = open(f"{llamando_import}/texto_a.txt")
print(fichero.read())
"""
"""#Utilizando el metodo  "W
#si el fichero no existe lo va crear y guarda lo que se escribe
llamando_import = os.path.dirname(__file__)
anadir_fichero = input('Ingresa lo que desea agregar al fichero: ')
fichero = open(f"{llamando_import}/texto_w.txt", "w")
fichero.write(anadir_fichero + "\n")

#Vuelvo a llamar el fichero pero sin la a
fichero = open(f"{llamando_import}/texto_w.txt")
print(fichero.read())
"""

"""#Utilizando el metodo "x"
#Si el fichero existe dará error
try:
    llamando_import = os.path.dirname(__file__)
    anadir_fichero = input('Ingresa lo que desea agregar al fichero: ')
    fichero = open(f"{llamando_import}/texto_x.txt", "x")
    fichero.write(anadir_fichero + "\n")

    #Vuelvo a llamar el fichero pero sin la a
    fichero = open(f"{llamando_import}/texto_x.txt")
    print(fichero.read())
except: 
    print('El fichero ya existe, lo lamento')
"""