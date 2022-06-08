"""#Para calcular el promedio de un alumno
print ('Sistema para calcular el promedio de un alumno')
nombre = input('Para comenzar, ¿Cual es tú nombre?')
matematica =  int(input(nombre +' ¿Cual es tu calificación de matematica?'))
quimica =  int (input(nombre + ' Cual es tu calificación de quimica?'))
biologia = int(input(nombre +' Cual es tu calificación de biologia?'))
promedio = (matematica + quimica + biologia) / 3
if promedio >=6 :
    print('Felicidades '+ nombre + ' aprobaste con un promedio de: ', promedio)
else:
    print(nombre+' Lo siento Reprobaste')

#SENTENCIAS MULTIPLES
#CONDICIONALES, .LOWER ES PARA QUE PUEDA LEER CUALQUIER PALABRA ESCRITA EN MAYUSCULA Y MINUSCULA

print('------------------------------------------')
print('!!Convertidor!!')
print('------------------------------------------')
print('Menu de opciones')
print('Presione 1 para convertir de numero a letras')
print('Presione 2 para convertir de palabras a numeros')

opcion = int(input('¿Cual es tú opción deseada?'))

if opcion == 1:
    numero = int(input('¿Cual es el número que deseas convertir?'))
    if numero ==1:
        print('El número es "Uno"')
    elif numero ==2:
        print('El número es "Dos"')
    elif numero ==3:
        print('El número es "Tres"')
    elif numero ==4:
        print('El número es "Cuatro"')
    elif numero ==5:
        print('El número es "Cinco"')
    else:
         print('ERRO: este programa solo convierte hasta el número 5')
elif opcion ==2:
     palabra = str(input('¿Cual es el palabra que deseas convertir a numero?'))
     palabra = palabra.lower()
     if palabra == 'uno':
         print('El número es "1"')
     elif palabra =='dos':
         print('El número es "2"')
     elif palabra == 'tres':
         print('El número es "3"')
     elif palabra =='cuatro':
            print('El número es "4"')
     elif palabra == 'cinco':
         print('El número es "5"')
     else:
        print('Este programa solo convierte palabras hasta el numero 5')

else:
    print('Opción Invalidad')

print('Fin.')"""



"""#Programa para determinar si un numero entero es par o inpar
print('----------------------------------------------------')
print('Programa para detemianar si un entero es par o inpar')
print('----------------------------------------------------')

numero = int(input('Ingrese un número entero:'))

if numero % 2  == 0:
             print('El número', numero, "es par")
else:
    print ('El número', numero, 'es impar')
#Programa para dertimnar el número mayor
print('----------------------------------------------------')
print('Programa para detemianar si un entero es par o inpar')
print('----------------------------------------------------')    
     
num1 = int(input('Ingrese el primer número entero:'))
num2 = int(input('Ingrese el segundo número entero:'))
num3 = int(input('Ingrese el tercero número entero:'))
if num1 != num2 and num1 != num3 and num2 != num3:
    if num1 > num2 and num1 > num3:
        print('El número', num1, "es el mayor de los tres")
    else:
        if num2 > num3:
            print('El número', num2,'es el mayor de los tres')
else:
    print('No pueden haber números iguales')"""

"""#CALCULADORA CON OPERADORES LÓGICOS
print('********************************')
print('* MENU de opciones')
print('********************************')
print('1. Suma')
print('2. Resta')
print('3. Multiplicación')
print('4. División')
print('5. División entera')
print('6. Exponente')
print('7. Modulo o resto \n')
numero = int(input('¿Ingresa la opcion que deseas? '))
if numero == 1:
    numero =int(input('Ingrese el primer número:'))
    numero += int(input('Ingrese el segundo número:'))
    print('La suma de los dos números es: ',numero)

elif numero == 2:
    numero =int(input('Ingrese el primer número:'))
    numero -= int(input('Ingrese el segundo número:'))
    print('La resta de los dos números es: ',numero)

elif numero == 3:
    numero =int(input('Ingrese el primer número:'))
    numero *= int(input('Ingrese el segundo número:'))
    print('La multiplicación de los dos números es:',numero)

elif numero == 4:
    numero =float(input('Ingrese el primer número:'))
    numero /= float(input('Ingrese el segundo número:'))
    print('La división de los dos números es:',round (numero,2))
    
elif numero == 5:
    numero =int(input('Ingrese el primer número:'))
    numero //= int(input('Ingrese el segundo número:'))
    print('La división parte entera de los dos números es:',numero)

elif numero == 6:
    numero =int(input('Ingrese el número:'))
    numero **= int(input('Ingrese el exponente:'))
    print('El resultado es:',numero)
    
elif numero == 7:
    numero =int(input('Ingrese el primer número:'))
    numero %= int(input('Ingrese el segundo número:'))
    print('El modulo  de los dos números es:',numero)
    
else:
    print('Esa opción no existe, intentanlo de nuevo')

#Serie figonachi
num_uno, num_dos = 0, 1
while num_dos <= 1597:
    print(num_uno, num_dos, end=" ")
    num_uno= num_uno+num_dos
    num_dos= num_dos+num_uno

#Ejercio calculando los a�os de vacaciones que se le debe otorgar a un trabajor
print('-----------------------------------------------')
print('Sistema de control de empleados de RAPPID!')
print('-----------------------------------------------')
nombre = input('Ingrese su nombre: ')
clave_departamento = int(input('Ingrese la clave del departamento: '))


if clave_departamento == 1 or clave_departamento == 2 or clave_departamento == 3:
    a�os = float(input('Ingrese los a�os en la compa�ia: '))
    if clave_departamento == 1:
        if a�os == 1:
            print('Departamento de atenci�n al cliente:', nombre +' tienes derecho 6 d�as de vacaciones')
        elif a�os >= 2 and a�os<=6:
            print('Departamento de atenci�n al cliente:', nombre +' tienes derecho 14 d�as de vacaciones')
        elif a�os >=7:
            print('Departamento de atenci�n al cliente:', nombre +' tienes derecho 20 d�as de vacaciones')
        else:
            print(nombre, 'a�n no tienes derechos a vacaciones')
    
    elif clave_departamento == 2:
        if a�os == 1:
            print('Departamento de logistica:', nombre +' tienes derecho 7 d�as de vacaciones')
        elif a�os >= 2 and a�os<=6:
            print('Departamento de logistica:', nombre +' tienes derecho 15 d�as de vacaciones')
        elif a�os >=7:
            print('Departamento de logistica:', nombre +' tienes derecho 22 d�as de vacaciones')
        else:
            print(nombre, 'a�n no tienes derechos a vacaciones')

    elif clave_departamento == 3:
        if a�os == 1:
            print('Departamento de gerencia:', nombre +' tienes derecho 10 d�as de vacaciones')
        elif a�os >= 2 and a�os<=6:
            print('Departamento de gerencia:', nombre +' tienes derecho 20 d�as de vacaciones')
        elif a�os >=7:
            print('Departamento de gerencia:', nombre +' tienes derecho 30 d�as de vacaciones')
        else:
            print(nombre, 'a�n no tienes derechos a vacaciones')

else:
    print('Clave de Departamento no existe, intentalo nuevamente')
print('fin')

"""
    

