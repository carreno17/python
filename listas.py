
#Creación de una lista [] o tambien list() ejemplo:
lista = ["Python", "Django", "Flask", "Java"]
print(lista[0])
#Modificiando un elemento en de la lista
lista[0] = "Ruby"
print(lista)#
#Creación de sublistas, si es de 0:4 no me va a mosta el elemento 3
sub_lista = lista[0:3]
print(sub_lista)

#Modificar una lista
lista = ["Python", "Php", "Java", "Javascript", "Mysql", "MongoDB"]
#Len es para contar cuantos elemento hay en una lista
print(len(lista))
#Para agregar nuevos elementos a una lista, hay dos formas con += o .append
#con .append, solo puedo agregar un solo elemento, con += mas elementos
lista.append("Go")
lista += "Go", "C#", "C++"
print(lista)
print(len(lista))
"""Para agregar un nuevo elemento a un indece de la lista, en la cual ya hay otro
elmenento, se usa  .insert"""
lista.insert(0, "Ruby")
print(lista)
print(len(lista))
#Para eleminar un elemento de la lista
lista.remove("Ruby") #Esto es para remover mediante el nombre del string
print(lista)
del lista [0] #Esto es para remover mediante el indice del elemento
print(lista)
#Para eleminar todos los elementos de unas lista se usa el .clear o = []
#lista.clear()
lista = []
print(lista)

#Para acomodar una lista con elmentos númericos
lista = [1, 44, 86, 2, 9, 61, 4 , 78]
lista.sort() #.sort es para comodar mi lista de menor a mayor
print(lista)
lista.sort(reverse=True) #remove=true es para comodar una lista de mayor a menor
print(lista)
#Forma para hallar el número mayor y menor de una lista
lista.sort()
print(lista[0]) #mimino
print(lista[-1]) #max
#La forma que se usa mas es usar min y max
print(min(lista))
print(max(lista))

#Forma de verificar si existe un valor en una lista
print(10 in lista) #El resultado sera false porque 10 no existe en la lista
print(44 in lista) #El resultado sera true porque 44 si existe en la lista
#Tambien se puede utilizar el not int que daría el contrarío de los resultados
print(10 not in lista) #El resultado sera true porque 10 no existe en la lista
print(44 not in lista) #El resultado sera false porque 44 si existe en la lista

#Si ese elemento existe en la lista, podemos verificar en que indice esta
print(44 in lista)
print(lista.index(44)) #.index es para ver en que indixe se ubica el elmento

