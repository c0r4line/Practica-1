import csv

archivo= open("/home/alumno/Documentos/bgg_db_1806-1.csv","r")
csvreader= csv.reader(archivo,delimiter=',')

lista=[]
for linea in csvreader:
    if((linea[4]<'3')and (linea[17]=="Card Game" ) ):
        lista.append(linea[3].replace("'","").replace("\"",""))

print(lista)