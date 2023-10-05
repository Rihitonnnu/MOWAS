import mysql.connector


class Sql:
    cnx = None
    cursor = None

    def __init__():
        try:
            cnx = mysql.connector.connect(
                user='user',  # ユーザー名
                password='password',  # パスワード
                host='localhost'  # ホスト名(IPアドレス）
            )

            if cnx.is_connected:
                print("Connected!")

        except Exception as e:
            print(f"Error Occurred: {e}")

    def select_name(self):
        cursor = self.cnx.cursor()
        query = '''select name from users'''
        print(cursor)
        # print('username is {}'.format(user_name))
