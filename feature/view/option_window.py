import PySimpleGUI as sg

sg.theme('GreenTan')  # give our window a spiffy set of colors

user_name = 'りょう'

layout = [[sg.Text("こんにちは、{}さん。操作を選択してください".format(user_name), size=(60, 1))],
          [sg.Button('名前の更新', button_color=(
              sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True, size=(80, 3))],
          [sg.Button('MOWASとの会話を開始する', button_color=(sg.YELLOWS[0], sg.GREENS[0]), size=(80, 3))]]

window = sg.Window('MOWAS', layout, font=('Helvetica', ' 13'),
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
