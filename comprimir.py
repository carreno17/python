#Comprimir es igual que zip
"""El zip sirve para unir elementos de una lista y un tuple, lo hace
juntando el indice 0 de lista con el indice 0 del tuple"""
lista = [1, 2, 3, 4, 5]
tupla = (10, 20, 30, 40, 50)
lista_2 = [100, 200, 300, 400, 500]
tupla_2 = (1000, 2000, 3000, 4000, 5000)
resultado = zip(lista, tupla, lista_2, tupla_2)
resultado = tuple(resultado)
print(resultado)

lista = [1,2,3,4]
dos = lista[-3:]
print(dos)