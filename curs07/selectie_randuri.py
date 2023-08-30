import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='grupa17siit'
)
# print(my_db)
cursor = my_db.cursor()

cursor.execute("SELECT * FROM projects")

result = cursor.fetchall()

for x in result:
    print(x)
