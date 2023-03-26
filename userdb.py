import time
import mysql.connector
from datetime import datetime

start_time = time.time()

mydb = mysql.connector.connect(
    host="sql12.freesqldatabase.com",
    user='sql12607651',
    password="bFawEBab7c",
    auth_plugin='mysql_native_password',
    database='sql12607651',
    charset='utf8'
)

"""
['time_stamp', 'line_id', 'user_name', 'notify_token', 'es', 'dp', 'cl', 'st_id']
(datetime.datetime(2023, 3, 22, 21, 45, 13), 'line_id', 'vincentdnskj', 'notify', 'es', 'dpwejfoejf', 'cl', 'staefjowjoefo')
"""

cursor = mydb.cursor()

# cursor.execute("SELECT * FROM users")
cursor.execute("SELECT * FROM users WHERE line_id = 'abcdefg'")
# cursor.execute("SELECT * FROM users WHERE line_id = 'abcdefg' ORDER BY time_stamp DESC")


# 獲取欄位名稱
column_names = [i[0] for i in cursor.description]

# 獲取表格內容
table_content = cursor.fetchall()

# 顯示欄位名稱
print(column_names)


# 顯示表格內容
# for row in table_content:
#     print(row)

date = max(table_content, key=lambda x: x[0])
print(dict(zip(column_names, list(date))))

# my_cursor.execute("SHOW DATABASES")
# for db in cursor:
#     print(db)


# sqlStuff = "INSERT INTO users (time_stamp, line_id, user_name, notify_token, es, dp, cl, st_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
# record1 = (datetime(2023, 3, 26, 11, 6, 59), "abcdefg", "吳哲丞", "abcdefg", "五專", "智動科", "智動三", "1092b0006")
# cursor.execute(sqlStuff, record1)
# mydb.commit()

end_time = time.time()
total_time = end_time - start_time
print(f"程式執行時間：{total_time} 秒")

print()