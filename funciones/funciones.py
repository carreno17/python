#def para crear una funcion
""" El return se usa para un resultado en una variable, si no queremos
mostrarla en pantalla"""
def suma (numero_1, numero_2):
    return numero_1+numero_2, "Esto es un tercer parametro"

numero_1 = int(input('Ingrese el primer número:'))
numero_2= int(input('Ingrese el segundo número:'))

resultado = suma(numero_1, numero_2)
print(resultado)

"""Al return le podemos pasar un terce o mas parametros y el resultado sera
una tupla entre el resultado de la suma de los dos numeros y el tercer termino"""

#Podemos divir ese tercer termino de los  primeros, asignandole una variable al 3
resultado, tercer_termino = suma(numero_1, numero_2)
print(resultado)
print(tercer_termino)
