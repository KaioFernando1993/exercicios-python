from PySimpleGUI import PySimpleGUI as sg
# Layout
sg. theme ('Reddit')
layout = [ 
[sg.text('Usuário'), sg input(key='usoario')],
[sg.text('senha'), sg Input( key='senha', password_char='*')],
[sg.checkbox('salvar o login?')],
[sg.button('entrar')] ]
             


# Janela
janela = sg.window('Tela de Login', layout)
#Ler os eventos 
while True:
   eventos, valores  =  janela.read()
   if eventos == sg. window_cloosed:
       break
   if eventos ['usoario'] == 'jhonatan' and valores['senha']
   == '123455' :
       print('bem vindo a inteface grafica ')