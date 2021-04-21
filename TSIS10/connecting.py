import psycopg2

DB_NAME = "newdb"
DB_USER = "postgres"
DB_PASSWORD = 'Zh534231'
DB_HOST = 'localhost'
DB_PORT = '5432'

try:
    con = psycopg2.connect(database = DB_NAME, user = DB_USER,
                           password = DB_PASSWORD, host = DB_HOST, port = DB_PORT)    

    print('connected successfully')

except:
    print('no connect')