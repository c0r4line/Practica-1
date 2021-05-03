import PySimpleGUI as sg

def build():
    """construye la ventana de menu del dataset opcion 2 ESTADIOS"""

    layout= [[sg.Text('Elige una opcion', size=(30,1), font=("MathJax_Typewriter", 20), justification= 'center')],    
            [sg.Button('Los 10 estadios con mas capacidad del mundo', size=(60, 2), key="-CAPACIDAD-")],
            [sg.Button('Los 3 estadios con mas capacidad de Argentina', size=(60, 2), key="-CAP_ARG-")],
            [sg.Button('Atras',size=(60,2), key="-Atras-")]]

    board=sg.Window('Actividad 1 -TEORIA-').Layout(layout)
       
    return board