import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='grupa17siit'
)
cursor = my_db.cursor()

sql = "UPDATE projects SET address='Bucuresti' where address='Bucharest'"

cursor.execute(sql)

my_db.commit()

print(cursor.rowcount)
