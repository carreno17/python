#Los closures son funtiones añadidas que al momento de retornar, retornan
#variables locales de su de la funcion principal


def name (nombre):
    mensaje =  f"Hola{nombre}" #Puede ser tambien "hola" + nombre
    
    def mensajes():
        print(mensaje)


    return mensajes()

nombre= "David"
resultado = name(nombre)