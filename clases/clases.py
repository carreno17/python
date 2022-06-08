"""La palabra pass se utiliza para no dejar un bloque vacio, ya que python
No podemos dejar funiones, bubles, condicionales etec 
EJEMPLO:
numeros=2
for der in numeros:
    pass"""
#Creando una clases, se conoce lo que hay dentro de una clase un atributo

class Usuarios:
    nombre = " "
    apellido = ""

Usuarios.nombre = 'David' #Así podemos cambiarle el valor a un atributo
Usuarios.apellido= "Lozada"
print(Usuarios)
print(Usuarios.nombre) #Metodo para buscar el valor de un atributo en una clase
print(Usuarios.apellido) 

objeto = Usuarios() #así se crea un objeto y su atributos se llama de instancia
"""Dijimos que los atributos de clases son solo de clase no de objetos, que pasa 
en este caso:

1. el objeto busca dentro de los atributos del objetos, aver si existe
2. si el atributo no existe, verifica en los atributos de la clase,
si existe lo toma para no dar un error, pero solo funcionará para lectura
3. si no existe el atributo ni en la clase ni el objeto, dará un error

IMPortante:
__dict__ nos permite ver los atributos de un objetos
ejemplo print(objeto.__dict__)
"""
print(objeto.nombre)
print(objeto.__dict__)

#AGREGANDO ATRIBUTOS A A UN OBJETO

objeto.nombre = "Jose" #Estoy creando un atributo dentro del objeto, objeto
objeto.apellido = "Lozada"
print(objeto.nombre)
print(objeto.apellido)
print(objeto.__dict__) #Verifico los atributos del objeto

#Editando valores de los atributos
objeto.apellido = "Martinez" #Edito el valor del atributo apellido
print(objeto.__dict__) #Verifico los atributos del objeto

