import mysql.connector


class Sql:
    cnx = None
    cursor = None

    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(
                user='user',  # ユーザー名
                password='password',  # パスワード
                host='localhost',  # ホスト名(IPアドレス）
                database='mowas',
            )

            if self.cnx.is_connected:
                print("Connected!")

        except Exception as e:
            print(f"Error Occurred: {e}")

    def select_name(self):
        try:
            cursor = self.cnx.cursor()

            query = '''
                    SELECT  name 
                    FROM    users
                    '''
            cursor.execute(query)
            rows = cursor.fetchall()

            if rows == []:
                raise Exception
            for row in rows:
                return row[0]
        except:
            print('データが取得できませんでした')
            return None
        finally:
            # クローズ
            if cursor is not None:
                cursor.close()
            if self.cnx is not None and self.cnx.is_connected():
                self.cnx.close()
