import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password="ntutgalaxy1092b",
    auth_plugin='mysql_native_password',
    database='userdb'
)

my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE userdb")

# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)

# my_cursor.execute("CREATE TABLE users (user_id VARCHAR(255) PRIMARY KEY, name VARCHAR(255), class VARCHAR(255), student_id VARCHAR(255))")

# sqlStuff = "INSERT INTO users (user_id, name, class, student_id) VALUE (%s, %s, %s, %s)"
# record1 = ('jfr1511546255563325854w56e', "Mary", "經管一", "111570021")
# my_cursor.execute(sqlStuff, record1)
# mydb.commit()
# my_cursor.execute("SELECT * FROM users")

sql = "SELECT * FROM users WHERE class=%s"
my_cursor.execute(sql, ('經管一',))

my_result = my_cursor.fetchall()
for data in my_result:
    print(data)