import PySimpleGUI as sg
from ventana import menu_estadios
from componente import inicio
import csv
import json
from collections import Counter
import os

def write_json(consulta_generada, filename='/home/alumno/Documentos/actividad_teoria/estadios.json'):
    """Escribe en el archivo json la info requerida en la consulta"""
    with open(filename,'w') as json_file:
        json.dump(consulta_generada, json_file, indent=4)

def start():
    """Lanza la ejecución de la ventana del dataset opcion ESTADIOS"""
    window = loop()
    window.close()


def loop():
    """Loop de la ventana de consulta Estadios que capta los eventos al presionar las opciones"""
    window = menu_estadios.build()
    archivo_path= os.path.join(os.getcwd(),'dataset2.csv')
    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-","-Salir-"):
            break

        if event == "-CAPACIDAD-":
            archivo = open(archivo_path,"r") 
            csvreader= csv.reader(archivo,delimiter =',')
            encabezado = next(csvreader)
            maximo= Counter()
            for columna in csvreader:
                #el nombre del estadio de la columna capacidad
                maximo[(columna[1])]= int(columna[4])
            estadios_json =(maximo.most_common(10))
            #para chequeo
            #print(estadios_json)
            constulta_estadios = estadios_json[:]
            write_json(constulta_estadios)
            archivo.close()
          
        if event == "-CAP_ARG-":
            archivo = open(archivo_path,"r") 
            csvreader= csv.reader(archivo,delimiter =',')
            encabezado = next(csvreader)
            maximo= Counter()
            csvreader = filter(lambda columna: columna[5] == 'Argentina', csvreader)
            for columna in csvreader:
                maximo[(columna[1])]= int(columna[4])
            estadios_json =(maximo.most_common(3))
            #para chequeo
            #print(estadios_json)
            constulta_estadios = estadios_json[:]
            write_json(constulta_estadios)
            archivo.close()
           

        if event == "-ATRAS-":
            window.hide()
            inicio.start()
            break
    return window
