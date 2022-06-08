#Podemos retornarn de una funcion otra funcion
def retorno ():

    def mensaje():
        print('Esto es un mensaje del retorno de la función retorno')
    
    return mensaje

resultado = retorno()
resultado()