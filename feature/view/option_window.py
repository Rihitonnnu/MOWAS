import PySimpleGUI as sg
from sql import Sql

sg.theme('GreenTan')  # give our window a spiffy set of colors

user_name = Sql().select('''
                    SELECT  name 
                    FROM    users
                    ''')


def make_main_window():
    main_layout = [[sg.Text("こんにちは、{}さん。操作を選択してください".format(user_name), size=(60, 1))],
                   [sg.Button('名前の更新', button_color=(
                    sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True, size=(80, 3))],
                   [sg.Button('運転を開始する', button_color=(sg.YELLOWS[0], sg.GREENS[0]), size=(80, 3))]]

    return sg.Window('MOWAS', main_layout, font=('Helvetica', ' 13'),
                     default_button_element_size=(8, 2), use_default_focus=False)


def make_name_change_window():
    sub_layout = [[sg.Text("変更したい名前を入力してください".format(user_name), size=(60, 1))],
                  [sg.Input(default_text=user_name, font=(
                      'Helvetica 10'), key='name_input')],
                  [sg.Button('更新', button_color=(
                      sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True, size=(60, 1))],
                  [sg.Button('戻る', button_color=(
                      sg.YELLOWS[0], sg.GREENS[0]), bind_return_key=True, size=(60, 1))],
                  ]

    return sg.Window('名前変更', sub_layout, font=('Helvetica', ' 13'),
                     default_button_element_size=(8, 2), use_default_focus=False)


window = make_main_window()

while True:     # The Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'EXIT'):            # quit if exit button or X
        break
    if event == "名前の更新":
        window.close()
        window = make_name_change_window()
    if event == "更新":
        Sql().change_name(values['name_input'])
        window.close()
        user_name = Sql().select('''
                    SELECT  name 
                    FROM    users
                    ''')
        window = make_main_window()
    if event == "戻る":
        window.close()
        window = make_main_window()
    if event == "運転を開始する":
        window.close()
    if event == 'SEND':
        query = values['-QUERY-'].rstrip()
        # EXECUTE YOUR COMMAND HERE
        print('The command you entered was {}'.format(query), flush=True)
