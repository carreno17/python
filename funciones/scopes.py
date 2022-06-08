#Scopes consiste en el alcanze una variable
"""Esto es una varible global que se puede leer en todo el código
sea en una función, ciclo, condicional"""



lenguaje = 'Python'


def prueba():
    global lenguaje #Con global puedo modificar el valor de la variable
    lenguaje = "Nuevo valor de la variable"
    Pedro = "David" #Es una variable loca porque solo se puede usar dentrol de la funcion
    print(Pedro)

    print(lenguaje)

    def nud ():

    #El nonlocal me sirve par acambiar el valor de una variable loca 
    # # dentro de un funticon, ciclo extera
        nonlocal Pedro
        Pedro= "Jose David Lozada"
    

    print(Pedro)
    
    
    
    
prueba()

print(lenguaje) #Igual me deja leer lenguaje
#print(Pedro) Acá no me deja leer a pedro porque es una varible local