import time
import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
    host="sql12.freesqldatabase.com",
    user='sql12607651',
    password="bFawEBab7c",
    auth_plugin='mysql_native_password',
    database='sql12607651',
    charset='utf8'
)

def get_userInfo(user_id):
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM users WHERE line_id='{user_id}'")

    column_names = [i[0] for i in cursor.description]
    table_content = cursor.fetchall()

    date = max(table_content, key=lambda x: x[0])
    user_dict = dict(zip(column_names, list(date)))

    return [user_dict['st_id'], user_dict['cl'], user_dict['es']]
