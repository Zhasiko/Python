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
cur.execute("DELETE FROM Employe WHERE ID = 20030317")
con.commit()
print("Data deleted Successfully")
print('Total row affected ' + str(cur.rowcount))
con.close()