import PySimpleGUI as sg
from ventana import inicio
from componente import menu1

def start():
    """Lanza la ejecución de la ventana INICIO"""
    window = loop()
    window.close()


def loop():
    """Loop de la ventana INICIO que capta los eventos al presionar las opciones"""
    window = inicio.build()

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "-SALIR-"):
            break
        if event == "-DATASET1-":
            window.hide()
            menu1.start()
            break
            #creo q aca hay un loop infinito
        if event == "-DATASET2-":
            pass
    return window
