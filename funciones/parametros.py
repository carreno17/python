"""A las funciones podemos pasarles parametros ya sea dandole a una 
ya sea creando una variable constante es decir que su valor no cambiara.
Pero cuando le damos el valor tiene que estár ubicada a la derecha """
def area_triangulo (radio, pi=3.14):
    return pi * (radio ** 2)

resultado = area_triangulo(10)#Solo le pasamos el radio porque pi ya esta definida
print(resultado)

#Tambien podemos darle valores de diferente forma colocando el nombre de la variable
resultado = area_triangulo(pi=30114, radio=10)
print(resultado)