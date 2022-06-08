#Metodo split, este sirve para pasar un string a lista



String = "Me gusta Python Mysql"
print(String)
#Convirtiendo el string en una lista, al split puedo pasarle cualquier simbolo
string_lista = String.split()
print(string_lista)

#Metodo join, este sirve para pasar una lista a string
lista = ["Me", "gusta", "Python", "Mysql"]
print(lista)
#Convirtiendo la lista a un string
lista_string = '-'.join(lista)
print(lista_string)


"""Metodo .count, este sirve para ver cuantas veces esta una palabra o numero(string)
en un string"""

metodo = "Hola jose david lozada carreño"
contador_metodo= metodo.count("lozada")
contador_dos = metodo.count('a')
print(contador_metodo)
print(contador_dos)

"""Metodo starwhit(), ester sirve para verificar si un strin es el inicio
 del otro"""

print(metodo.startswith('david')) #esto sera false porque david no esta de primero
print(metodo.startswith('Hola')) #esto sera true porque Hola esta de primero

"""Metodo endwhit(), este sirve para verificar si un strin es el final
 del otro"""

print(metodo.endswith('Hola')) #esto sera false porque Hola no esta de ultimo
print(metodo.endswith('carreño')) #esto sera true porque carreño esta de ultimo

#Para buscar si un valor strin existe en el otro

print("Python" in metodo)#Me da false porque Python no esta en metodo
print('hola' in metodo.lower())