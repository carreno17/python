print ('Esto es una suma')
num=3
num1=7
resultado=num+num1
resultado = str(resultado)
print ('El resultado de la suma es: ' + resultado)


mensaje= 'Hola'
mensaje +=' ' 
mensaje += 'David'
print (mensaje)


bienvenidad = 'Hola'
nombre = ' David'
apellido = ' lozada'
print(bienvenidad + nombre + apellido )

#** es para mutiplicar un número por una potencia;
num1 = 2**3
num2 = 3**3
total = num1+num2
total = str(total)
print('El total de la suma los dos numeros es ' + total)

#.find para busqueda
lista = "Hola David"
busquedad = lista.find("David")
busquedad = str(busquedad)
print('La busquedad es de:' + busquedad)

# comparacion es ==
nombre = 'David'
nombre1= 'David'
nombre2 = 136
resultado = nombre == nombre1
resultado2= nombre == nombre2
resultado = str(resultado)
print('El resultado de esta comparación es: ' + resultado)
print('El resultado de esta compración es: ' + str(resultado2))

# % modulo // division entera
numero1 = 8
numero2= 4
print(numero1 // numero2)

""" Estoy es un comentarío
super
largo
para probrar un sapo"""

#tipos de variable
entera = 2
print(entera, type(entera))
flotante = 17.57
print(flotante, type(flotante))
compleja = 2+6j
print(compleja, type(compleja))
verdadero_falso = 2 == 2
print(verdadero_falso, type(verdadero_falso))

#end y sep
print ('Esto es la prueba de', end=' ')  
print('el end')

print("1", "2", "3","4","5",sep="=")

"""OPERADORES LOGICOS:
 and significa Y
 Ejemplo: if condición and condición
  or significa O
 Ejemplo: if condición or condición
 not significa no
 Ejemplo: if not condición"""

#Colocar varias variables en una linea
nombre, apellido, edad = "David", "Lozada", 19
print(edad)

