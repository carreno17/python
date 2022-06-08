#Docstrting signica documentar algo nosotros podes documentar, se coloca en la primera linea de código
#(modulos, metedos, clases, funciones)
#__doc__ o help(funcion) nos sirve para ver las cosas documentadas

def suma (numero1, numero2):
    """
    la Función suma  dos números
    
    argumentos:
    numero1(int)
    numero2(int)

    Se retorna la suma de dos parametros
    """
    return numero1+numero2

#print(suma.__doc__) metodo 1
print(help(suma)) #metodo 2

""" Tambíen podemos testear funciones apartir de un Docstring en una funicón
"""

def suma (numero1, numero2):
    """
    la Función suma  dos números
    
    argumentos:
    numero1(int)
    numero2(int)

    >>> suma(10, 20)
    30

    >>> suma(10,40)
    50

    Se retorna la suma de dos parametros
    """
    return numero1+numero2
""" Para yo verificar una función si esta funcionando bien coloca la siguente
expresión >>>>>> suma(10,40) y en otra linea el resultado que me deberia dar
50. PARA YO COMPROBAR EL TESTEO DEDO DE IRME A LA TERMINAR Y COLOCAR EL COMANDO
python -m doctest documentar.py, si todo esta bien me imprimira el comentario
de lo contrarío si está mal el resultado me dara un error"""
