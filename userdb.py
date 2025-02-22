import time
import mysql.connector
import pymysql
from datetime import datetime

hostname = "server.gems.com.tw"
username = "vincent"
password = "qwerty1324"
database = "NTUT_GALAXY"

# Connect to the database
mydb = pymysql.connect(host=hostname, user=username, password=password, db=database, charset='utf8')

def get_userInfo(user_id):
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM users WHERE line_id='{user_id}'")

    column_names = [i[0] for i in cursor.description]
    table_content = cursor.fetchall()

    date = max(table_content, key=lambda x: x[0])
    user_dict = dict(zip(column_names, list(date)))

    return [user_dict['st_id'], user_dict['cl'], user_dict['es']]
