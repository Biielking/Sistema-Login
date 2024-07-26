import PySimpleGUI as sg

Layout = [

    [sg.Text('Usuario')],
    [sg.Input(key='Usuario')],
    [sg.Text('senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('', key='mensagem')],
]

window = sg.Window('login', layout=Layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        senha_correta = "123"
        usuario_correto = 'BielKing'
        usuario = values['usuario']
        senha = values['senha']
        if senha == senha_correta and usuario == usuario_correto:
            window['mensagem'].update('login feito com sucesso')
        else:
            window['mensagem'].update('senha incorreta')
