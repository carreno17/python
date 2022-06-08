"""range, siempre comienza en 0 hasta el valor que decidamos 
ejemplo quiero los numeros del 0 al 20, tendría que colocar 21 ya que el último
numero no lo toma"""
"""Le podemos pasar un primer termino que sería de donde queremos que comienze
un segundo termino que seria hasta donde queremos que termine,
y un tercero que seria de cuanto en cuanto queremos que se muestre"""

for numeros in range(1, 21, 2):
    print(numeros)

#enumerate sirve para mostrarnos el indice de una lista y su variable
numeros= [10, 20, 30, 40]
for indice, numeros in enumerate(numeros):
    print(indice, numeros)