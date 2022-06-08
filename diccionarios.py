#Para crea un diccionario utilizamos {} 


diccionario = {}
"""Para agregar un valor al dicionario se usa el nombre de la variable 
 = al nombre del string y su valor, Ejemeplo diccionario["nombre"] = "David" """
diccionario["nombre"] = "David"
diccionario["Apellido"]= "Lozada"
diccionario["Edad"]= 19
print(diccionario)

#Para modificar el valor de que tiene una variable
diccionario["nombre"]= "Jose David"
print(diccionario)
#Tambien podemos pasarle de una vez los valores al diccionario
diccionario_dos = {'Uno': 1, 'Dos': 2, 'Tres': 3}
print(diccionario_dos)


"""Para obtener el varlor de una variable en el diccionario se usa el metodo .get
usamos la variable.get("acá colocamos el nombre de la variable que
deseamos su valor")"""
print(diccionario_dos.get('Dos'))
"""El get le podes pasar un segundo parametro para dar un mensaje para cuando
una variable no existe en el diccionario"""
print(diccionario_dos.get('tres', "Esa variable no existe en el diccionario"))


#ELEMENTOS PARA OBTENER VALORES DEL DICCIONARIO

#keys, se usa para ver el nombre de las llaves
llaves = tuple (diccionario_dos.keys())
print(llaves)

#values, se usa para mostar el valor de llaves
valor_llaves= tuple (diccionario_dos.values())
print(valor_llaves)

#items, se usa para las llaves con su valor
llaves_consu_valor = tuple (diccionario_dos.items())
print(llaves_consu_valor)


#PARA ELIMINAR UNA LLAVE DEL DICCIONARIO
para_eliminar = {'Uno': 1, 2: 2, 'Tres': 3, 'Cuatro': 4, 'Cinco': 5 ,}
print(para_eliminar)
print(len(para_eliminar))
#Eliminando
del para_eliminar['Cinco']#Metodo 1
print(para_eliminar)

para_eliminar.clear()#Para eliminar todas las llaves del diccionario
print(para_eliminar)


