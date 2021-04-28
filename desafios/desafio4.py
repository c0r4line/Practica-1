def ingreso_notas():
    """ Esta función retorna un diccionario con los nombres y notas de estudiantes """
    nombre = input("Ingresa un nombre (<FIN> para finalizar)")
    dicci = {}
    while nombre != "FIN":
        nota = int(input(f'Ingresa la nota de {nombre}'))
        dicci[nombre] = nota 
        nombre = input("Ingresa un nombre (<FIN> para finalizar)")
    return dicci
    

def calculo_promedio(notas):
    """ Esta función calcula el promedio de las notas recibida por parámetro. notas: es un diccionario de forma nombre_estudiante: nota"""
    suma = 0
    for estu in notas:
        suma += notas[estu]
        promedio = 0 if len(notas)==0 else suma/len(notas)
    return promedio
    
notas_de_estudiantes= ingreso_notas()
promedio= calculo_promedio(notas_de_estudiantes)

print(promedio)
    
