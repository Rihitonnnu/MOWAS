import mysql.connector
import os
import time
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

    def select(self, query):
        try:
            cursor = self.cnx.cursor()

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

    def change_name(self, input):
        cursor = self.cnx.cursor()
        query = f'''
                    UPDATE users 
                    SET name='{input}'
                    WHERE id=1
                    '''
        cursor.execute(query)
        self.cnx.commit()
        if cursor is not None:
            cursor.close()
        if self.cnx is not None and self.cnx.is_connected():
            self.cnx.close()

    def store_conversation(self):
        cursor = self.cnx.cursor()
        with open("../log/conversation.log", encoding="UTF-8") as f:
            now = time.localtime()
            d = time.strftime('%Y-%m-%d %H:%M:%S', now)
            conversation_log = f.read()

            query = f'''
                    INSERT INTO conversations (content,created_at)
                    VALUES ('{conversation_log}','{d}')
                    '''

            cursor.execute(query)
            self.cnx.commit()
            print('store conversation completed.')
            if cursor is not None:
                cursor.close()
            if self.cnx is not None and self.cnx.is_connected():
                self.cnx.close()

    def store_conversation_summary(self, summary):
        cursor = self.cnx.cursor()
        query = f'''
                    UPDATE users 
                    SET summary='{summary}'
                    WHERE id=1
                    '''
        cursor.execute(query)
        self.cnx.commit()
        print('updating summary completed.')
        if cursor is not None:
            cursor.close()
        if self.cnx is not None and self.cnx.is_connected():
            self.cnx.close()
