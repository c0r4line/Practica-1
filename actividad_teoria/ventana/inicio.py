import PySimpleGUI as sg
sg.theme('DarkTeal1')
def build():
    """construye la ventana de menu"""

    layout= [[sg.Text('¿ QUE  DATOS  ANALIZAMOS ?', size=(30,1), font=("MathJax_Typewriter", 20), justification= 'center')],    
            [sg.Button('DATASET-1', size=(60, 2), key="-dataset1-")],
            [sg.Button('DATASET-2', size=(60, 2), key="-dataset2-")],
            [sg.Button('Salir',size=(60,2))]]

    board=sg.Window('Actividad 1 -TEORIA-').Layout(layout)
       
    return board