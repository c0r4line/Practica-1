import PySimpleGUI as sg
from ventana import inicio

def start():
    """Lanza la ejecución de la ventana del menú"""
    window = loop()
    window.close()


def loop():
    """Loop de la ventana de menú que capta los eventos al presionar las opciones"""
    window = inicio.build()

    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Salir"):
            break
        if event == "-dataset1-":
            pass
        if event == "-dataset2-":
            pass
    return window
