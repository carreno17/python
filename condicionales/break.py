"""break nos firve para finalizar cualquier ciclo cuando se cumpla la condicion
Este nos mostrara lo que está antes del resultado de la condiccion"""

condicion = "Hola mi nombre es Jose David"

for iteracion in condicion:
    if iteracion == "J": 
        break #Llega hasta donde consigua la J de hay para alla no impreme lo demas
        
    print(iteracion)

#continue sirve ignora el resultado de la condicion que escribimos y continua

for iteracion in condicion:
    if iteracion == "J": 
        continue #Ignora la J y sigue
        
    print(iteracion)