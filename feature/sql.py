import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


class Sql:
    cnx = None
    cursor = None

    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(
                user=os.environ['MYSQL_USER'],  # ユーザー名
                password=os.environ['MYSQL_PASSWORD'],  # パスワード
                host=os.environ['HOST'],  # ホスト名(IPアドレス）
                database=os.environ['DATABASE'],
            )

            if self.cnx.is_connected:
                print("Database connected.")

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
                print("Data successfully retrieved.")
                return row[0]
        except:
            print('Data could not be successfully retrieved.')
            return None
        finally:
            # クローズ
            if cursor is not None:
                cursor.close()
            if self.cnx is not None and self.cnx.is_connected():
                self.cnx.close()
