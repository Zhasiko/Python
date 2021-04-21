import psycopg2

DB_NAME = "newdb"
DB_USER = "postgres"
DB_PASSWORD = 'Zh534231'
DB_HOST = 'localhost'
DB_PORT = '5432'

con = psycopg2.connect(
    database = DB_NAME, user = DB_USER,
    password = DB_PASSWORD, host = DB_HOST, port = DB_PORT)

print("Database connected Successfully")

cur = con.cursor()
cur.execute('SELECT ID , NAME , EMAIL from Employe')

rows = cur.fetchall()

for data in rows:
    print("ID: " + str(data[0]))
    print("NAME: " + data[1])
    print("EMAIL: " + data[2])

print("Data selected Successfully")
con.close()