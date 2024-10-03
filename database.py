import mysql.connector

# database info
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
)

# prepare the cursor
cursor = dataBase.cursor()

#create a database
cursor.execute("CREATE DATABASE k_database")

print("Database created")