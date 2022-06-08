#Son funciones que resiben a otras
""" Fun_A es la funcion principal (Decorador)
fun_b es la funcion a decorar
fun_c es la funcion decorada"""

"""
def fun_a(fun_b):

    def fun_c():
        fun_b()
        print('Funcion decorada')

    return fun_c    

@fun_a
def saluda():
    print('Está es mi función a decorar')

saluda()"""

#Otra forma más complicada de un decorador

def fun_a(fun_b):

    def fun_c(*args, **kwargs):
        resultado = fun_b(*args, **kwargs)
        print('Funcion decorada')

        return(resultado)

    return fun_c
    

@fun_a
def suma(n1, n2):
    return n1+n2  
resultado = suma(10,20)
print(resultado)