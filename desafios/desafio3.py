nota = int(input("Ingresá una nota (-1 para finalizar)"))

lista_de_notas = []

while nota != -1:
    lista_de_notas.append(nota)
    nota = int(input("Ingresá una nota (-1 para finalizar)"))

total = 0
for indice in range(len(lista_de_notas)):
    total += lista_de_notas[indice]
promedio = total//len(lista_de_notas)
print(promedio)


cant = 0
for indice in range(len(lista_de_notas)):
    if promedio < lista_de_notas[indice]:
        cant += 1
print( f"Los alumnos que obtuvieron nota menor que el promedio: {promedio} son:")
print(cant)
