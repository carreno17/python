import os
#copiar un fichero en otro
llamando_import = os.path.dirname(__file__)
fichero = open(f"{llamando_import}/texto_nuevo.txt")
copiar_fichero = fichero.read()

try:
    import_funcion = os.path.dirname(__file__)
    fichero_2 = open(f"{llamando_import}/texto_nuevo-copy.txt", "x")
    fichero_2.write(copiar_fichero)
    
    fichero_2 = open(f"{llamando_import}/texto_nuevo-copy.txt")
    print(fichero_2.read())
except:
    print('Este fichero ya existe')