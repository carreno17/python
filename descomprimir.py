#descomprimir es igual que desempaquetar
# el _ es para decir que no quiero que se muestrene sos elementos de mi tuple
"""el *lista lo que hace es guardarme los elementos que no le asigne una variable
 me los meta en una lista""" 
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10 )
uno, dos, tres , cuatro, cinco, *lista = numeros
print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)
print(lista)
"""Uso el _ para no mostra los números del 5 al 8, pero si me muesta los dos
utimos números"""
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10 )
uno, dos, tres , cuatro, cinco, *_, nueve, diez = numeros
print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)
print(nueve)
print(diez)

"""Uso el _ para no mostra los números del 5 al 8, y tambien el _ para indicar
que no se me muestre mi segunda varible es decir el 2"""
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10 )
uno, _, tres , cuatro, cinco, *_, nueve, diez = numeros
print(uno)
print(tres)
print(cuatro)
print(cinco)
print(nueve)
print(diez)

