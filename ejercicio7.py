nombres= ''''Agustin','Alan','Andrés', 'Ariadna', 'Bautista','CAROLINA','CESAR','David','Diego','Dolores','DYLAN','ELIANA','Emanuel','Fabián','Facundo','Facundo','FEDERICO','FEDERICO','GONZALO','Gregorio','Ignacio','Jonathan','Jonathan','Jorge','JOSE','JUAN','Juan','Juan','Julian','Julieta','LAUTARO','Leonel','LUIS','Luis','Marcos','María','MATEO','Matias','Nicolás','NICOLÁS','Noelia','Pablo','Priscila','TOMAS','Tomás','Ulises','Yanina' '''
notas1='''81,60,72,24,15,91,12,70,29,42,16,3,35,67,10,57,11,69,12,77,13,86,48,65,51,41,87,43,10,87,91,15,44,85,73,37,42,95,18,7,74, 60,9,65,93,63,74'''
notas2='''30,95,28,84,84,43,66,51,4,11,58,10,13,34,96,71,86,37,64,13,8,87,14,14,49,27,55,69,77,59,57,40,96,24,30,73,95,19,47,15,31,39,15,74,33,57,10'''


nombres= nombres.replace("'","")
nombres=nombres.split(',') #separo los str que entran x coma,
notas1=notas1.split(',')
notas2=notas2.split(',')

estudiante_notas= list(zip(nombres,notas1,notas2)) #creo lista de tuplas con ZIP
print('Nombre del estudiante y sus evaluaciones: ')
print(tuple(estudiante_notas))

promedio=[]
suma_notas=[]
for nota1,nota2 in zip(notas1,notas2): #recorro la estructura y voy sumando ambas notas
   suma_notas.append(sum([int (nota1), int (nota2)]))
   for una_nota in suma_notas: #recorro haciendo el promedio de TODOS los estudiantes
       promedio.append(una_nota/2)

nombres_total= list(zip(nombres,suma_notas))
nombres_promedio=list(zip(nombres,promedio))
print('NOMBRE DEL ESTUDIANTE Y LA SUMA DE SUS EVALUACIONES: ',nombres_total)
print('NOMBRE DEL ESTUDIANTE Y SU PROMEDIO: ', nombres_promedio)

notas= {}

for indice in range(len(nombres)):
    notas[nombres[indice]] = int(notas1[indice]) + int(notas2[indice])
total = 0
for alumno in notas:
    total += notas[alumno]
promedio= total / len(notas)

for alumno in notas:
    if promedio > notas[alumno]:
        print (f"Los alumnos que obtuvieron nota menor que el promedio: {promedio} son:")
        print(alumno,notas[alumno])
#suma1=0
#suma2=0
#cant=0
#for a in nombres:
#   cant+=1
#for i in notas1:
#   suma1= suma1 + int (i)
#for x in notas2:
#   suma2= suma2 + int (x)
#total_notas= suma1 + suma2
#prom_total_notas= total_notas / cant
#prom_total_notas= [prom_total_notas]

#print('el promedio de estudiantes es: ', prom_total_notas)
#print('por debajo del promedio se encuentran')

#for nombres in nombres_promedio:
#   if promedio<prom_total_notas:
#      print(nombres)


