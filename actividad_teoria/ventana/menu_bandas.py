import PySimpleGUI as sg

def build():
    """construye la ventana de menu del dataset opcion 1 METAL"""

    layout= [[sg.Text('Elige una opcion', size=(30,1), font=("MathJax_Typewriter", 20), justification= 'center')],    
            [sg.Button('Albums con 5 estrellas', size=(60, 2), key="-estrellas-")],
            [sg.Button('Los mejores de los 2000',size=(60,2), key="-2000-")],
            [sg.Button('Atras',size=(60,2), key="-Atras-")]]

    board=sg.Window('Actividad 1 -TEORIA-').Layout(layout)
       
    return board