#Puedo declara un condiccion en una linea si solo tiene un else
calificacion = int(input("Ingrese su calificación:"))
color = "Verde" if calificacion >= 10 else"Rojo"
print(calificacion, color)

#Si tengo dos variables una con un valor falso y una con valor verdadero
#Paython tomara me imprimaíra solo la variable verdadera
nombre = [] #[] es un valor false
apellido = "Lozada" #Es un valor verdadero

resultado = nombre or apellido 
print(resultado)
