#Estás funciones nos sirve para pasarle como argumentos otras funciones


promedio  = lambda *args : sum(args) / len(args)
print(promedio(10,50,60,60))

alumno_aprobo = lambda calificaciones : calificaciones >= 7 #Esto me retorna un true
print(alumno_aprobo(8))

def si_aprobo_o_no (fun_promedio, fun_alumno_aprobo, *args):
    promedio = fun_promedio(*args)

    if fun_alumno_aprobo(promedio):
        print('Felicidades aprobasto el semestre con un promedio de', promedio)
    else:
        print("Reprobaste el semestre con un promedio de", promedio)

si_aprobo_o_no(promedio, alumno_aprobo, 10, 10, 10)