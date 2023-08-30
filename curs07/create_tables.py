import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='grupa17siit'
)
# print(my_db)
cursor = my_db.cursor()
try:
    cursor.execute('CREATE TABLE projects (id INT AUTO_INCREMENT PRIMARY KEY, '
                   'name VARCHAR(255),'
                   'address VARCHAR(255),'
                   'project_number INT)')
except mysql.connector.errors.ProgrammingError:
    pass
try:
    cursor.execute('ALTER TABLE projects ADD COLUMN user_id INT')
except mysql.connector.errors.ProgrammingError:
    pass

sql = "INSERT INTO projects (name, address, user_id) VALUES (%s, %s, %s)"
val = [
    ('Peter', 'Bucharest', 1),
    ('Paul', 'Cluj', 2),
    ('Mihai', 'Bacau', 3),
]
cursor.executemany(sql, val)
my_db.commit()

