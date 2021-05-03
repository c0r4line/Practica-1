import PySimpleGUI as sg
from ventana import menu_bandas
from componente import inicio
import csv
import json
import os

def write_json(consulta_generada, filename='bandas.json'):
    """Escribe en el archivo json la info requerida en la consulta"""
    try:
        with open(filename,'w') as json_file:
            print("escribiendo en json")
            json.dump(consulta_generada, json_file, indent=4)
    except FileNotFoundError:
        print("archivo no encontrado")

def start():
    """Lanza la ejecución de la ventana del dataset opcion BANDAS"""
    window = loop()
    window.close()


def loop():
    """Loop de la ventana de Consulta Bandas que capta los eventos al presionar las opciones"""
    window = menu_bandas.build()
    archivo_path= os.path.join(os.getcwd(),'dataset1.csv')

    
    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","-Salir-"):
            break

        if event == "-ESTRELLAS-":
            try:
                archivo = open(archivo_path,"r") 
                print("leyendo csv")
            except FileNotFoundError:
                print("archivo no encontrado")
            csvreader= csv.reader(archivo,delimiter =',')
            encabezado = next(csvreader)
            nombre_album= []
            lista_5_estrellas = list(filter(lambda columna: columna[13] == '5', csvreader))
            for linea in lista_5_estrellas:
                nombre_album.append(linea[2])
            write_json(nombre_album)
            #-----lo que quiero conseguir con esta consulta es imprimir en json la lista resultante..
            #.. de los NOMBRES DE ALBUMES que tienen rating de exactamente 5 puntos----------
            archivo.close()
            

        if event == "-DOSMIL-":
            try:
                archivo = open(archivo_path,"r") 
                print("leyendo csv")
            except FileNotFoundError:
                print("archivo no encontrado")
            csvreader= csv.reader(archivo,delimiter =',')
            encabezado = next(csvreader)
            nombre_banda = []
            lista_2000 = list(filter(lambda columna: columna[3] >= '2000', csvreader))
            for linea in lista_2000:
                nombre_banda.append(linea[1])
            write_json(nombre_banda)
            #-----lo que quiero conseguir con esta consulta es imprimir en json la lista resultante..
            #.. de los NOMBRES DE LAS BANDAS que lanzaron albumes del 2000 en adelante ----------
            archivo.close()
            
        if event == "-ATRAS-":
            window.hide()
            inicio.start()
            break
    return window
