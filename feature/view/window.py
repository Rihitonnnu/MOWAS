import PySimpleGUI as sg

sg.theme('GreenTan')  # give our window a spiffy set of colors

layout = [[sg.Text('会話内容を入力して下さい', size=(40, 1))],
          [sg.Output(size=(110, 20), font=('Helvetica 10'))],
          [sg.Multiline(size=(70, 5), enter_submits=True, key='-QUERY-', do_not_clear=False),
           sg.Button('送信', button_color=(
               sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
           sg.Button('終了', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]

window = sg.Window('Chat window', layout, font=('Helvetica', ' 13'),
                   default_button_element_size=(8, 2), use_default_focus=False)

while True:     # The Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'EXIT'):            # quit if exit button or X
        break
    if event == 'SEND':
        query = values['-QUERY-'].rstrip()
        # EXECUTE YOUR COMMAND HERE
        print('The command you entered was {}'.format(query), flush=True)

window.close()
