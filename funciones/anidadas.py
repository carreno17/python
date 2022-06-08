
def operaciones (cantidad, balance, tipo='deposito'):

    def deposito(cantidad, balance):
        return cantidad + balance
    

    def retiro(cantidad, balance):
        if balance >= cantidad:
            return balance - cantidad
        else:
            None
   # print(deposito(10,20)) Puedo hacerlo de está forma o factorizar mas
   #  print(retiro(10,50)) está funcion
   

    if tipo =='deposito' or tipo=='Deposito' :
        return deposito(cantidad, balance)
    elif tipo == 'retiro':
        return retiro(cantidad, balance)

resultado = operaciones(10, 5 , tipo="Deposito")
print(resultado)

#Las funciones las podemos guardar en variables
"""Cuando guardarmos una función en una variable al imprimir está variable
tenemos que pasarle los parametros de la funcion
"""
guardar_funcion = operaciones
print(guardar_funcion(10, 50, tipo='deposito'))