import csv
from collections import Counter
archivo = open("/home/alumno/Documentos/bgg_db_1806-1.csv","r") 
csvreader= csv.reader(archivo,delimiter =',')

encabezado = next(csvreader)
lista_cartas_menos_de_3 = list(filter(lambda columna: int(columna[4]) < 3 and "Card Game" in columna[17], csvreader))
print("juegos de cartas con menos de 3 jugadores")
for l in lista_cartas_menos_de_3:
    print(l[3])
archivo.close()
#falta mas votados