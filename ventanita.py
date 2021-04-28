import PySimpleGUI as sg    

#sg.Popup('Mi primera ventanita', button_color=('black', 'red'))

#sg.PopupYesNo('Mi primera ventanita', button_color=('black', 'green'))

#sg.PopupOKCancel('Mi primera ventanita', button_color=('black', 'grey'))

#texto = sg.PopupGetText('Titulo', 'Ingresá algo')

#sg.Popup('Resultados', 'Ingresaste el siguiente texto: ', texto)
layout = [ [sg.Text('Ingresá primer valor'), sg.InputText()],
[sg.Text('Ingresá segundo valor'), sg.InputText()],
[sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window("Segundo Demo", layout, margins=(200, 150))
while True:
    event, values = window.read()
    if event == "Cancel" or event == sg.WIN_CLOSED:
        break
    print('Datos ingresados: ', values)
window.close()

layout = [[sg.Input('Ingresa algo')],
[sg.Listbox(values=('Item 1', 'Item 2', 'Item 3'))],
[sg.OK()]]
window = sg.Window("Elementos básicos", layout, margins=(200, 150))
event, values = window.read()
sg.Popup(event, values, line_width=200)

#esta no anduvo
sg.ChangeLookAndFeel('DarkAmber')
layout = [[sg.Listbox(values=('Item 1', 'Item 2', 'Item 3'),background_color='yellow', size=(20,3)),[sg.Input('Last input')],[sg.ColorChooserButton(" Elegi color")],[sg.OK()]]]

