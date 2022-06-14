

try:
    num1 = float(input('Ingresa el primero número'))
    num2 = float(input('Ingresa el segundo número'))
    resultado = num1 + num2
    print(resultado)

except:
    print('No se pueden ingresar valores de tipo string')


lista = {"a",3,4,5, "a", True, False, (3,4,5,7)}
lista.add((35,5,4))
print('o' in lista)
