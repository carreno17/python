import os

respuesta = input('¿Desea eliminar un archivo? [Si/No]: ')
if respuesta == 'si' or respuesta =='SI' or respuesta == 'Si':
    try:
        importar = os.path.dirname(__file__)
        remover = str(input('Ingresa el archivo: '))
        os.remove(remover)
        print('Proceso exitoso')
    except:
        print('El archivos que deseas eliminar no existe')
