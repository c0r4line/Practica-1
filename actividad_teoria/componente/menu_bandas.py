import PySimpleGUI as sg
from ventana import menu_bandas
from componente import inicio
import csv
import json

def write_json(consulta_generada, filename='/home/alumno/Documentos/actividad_teoria/bandas.json'):
    """Escribe en el archivo json la info requerida en la consulta"""
    with open(filename,'w') as json_file:
        json.dump(consulta_generada, json_file, indent=4)

def start():
    """Lanza la ejecución de la ventana del dataset opcion BANDAS"""
    window = loop()
    window.close()


def loop():
    """Loop de la ventana de Consulta Bandas que capta los eventos al presionar las opciones"""
    window = menu_bandas.build()
    archivo_path='/home/alumno/Documentos/actividad_teoria/dataset1.csv'
    
    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","-Salir-"):
            break

        if event == "-estrellas-":
            archivo = open(archivo_path,"r") 
            csvreader= csv.reader(archivo,delimiter =',')
            encabezado = next(csvreader)
            lista_5_estrellas = list(filter(lambda columna: columna[13] == '5', csvreader))
            #for l in lista_5_estrellas:
            #   print(l[1])    //para chequeo
            consulta_5_estrellas = lista_5_estrellas[:]
            write_json(consulta_5_estrellas)
            archivo.close()
            

        if event == "-2000-":
            archivo = open(archivo_path,"r") 
            csvreader= csv.reader(archivo,delimiter =',')
            encabezado = next(csvreader)
            lista_2000 = list(filter(lambda columna: columna[3] >= '2000', csvreader))
            #for l in lista_2000:
            #   print(l[1])   //para chequeo
            constulta_2000 = lista_2000[:]
            write_json(constulta_2000)
            archivo.close()
            

        if event == "-Atras-":
            window.hide()
            inicio.start()
            break
    return window
