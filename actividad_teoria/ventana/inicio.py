import PySimpleGUI as sg
sg.theme('DarkGrey5')
def build():
    """construye la ventana de menu principal"""

    layout= [[sg.Text('¿ QUE  DATOS  ANALIZAMOS ?', size=(30,1), font=("MathJax_Typewriter", 20), justification= 'center')],    
            [sg.Button('Los 100 mejores METAL edition', size=(60, 2), key="-DATASET1-")],
            [sg.Button('Estadios de Futbol', size=(60, 2), key="-DATASET2-")],
            [sg.Button('Salir',size=(60,2), key="-SALIR-")]]

    board=sg.Window('Actividad 1 -TEORIA-').Layout(layout)
       
    return board