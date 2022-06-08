#yield es un iterador pereso, que nos permite iterar una condicion
#A medida que lo vayamos pidendo
#range () es utilo para ver los números de tal a tal y de cuanto en cuanto
#Tambien utilizamos la función next
"Programa para ver los números del 0 al 100 de 2"
def pares():
    for numeros in range(0, 10, 2):
        yield numeros
       

generador = pares()
#acá me vale, a medida que vaya llamando nuevamente esta funcion
#Me va iterando el contador hasta llevar en este caso a 20
"""print(next(generador)) 

print(next(generador)) #vale 2

print(next(generador)) # vale 4

print(next(generador)) #vale 6

print(next(generador)) #vale 8

print(next(generador)) #vale 10

"""
#
#Como trabajar con error, al momento de mi función yield llega a 10 me causa
#Un error llamado StopIteration ya que no hay más valores, ese error lo podemos 
while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print('El generador finalizo')
        break
# convertir En un mensaje
