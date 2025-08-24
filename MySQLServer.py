import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "msec",
        password = "root",
    
    )

    if mydb.is_connected():
        # creating a variable for the cursor
        mycursor = mydb.cursor()

        # creating the database
        mycursor.execute("""
        CREATE DATABASE IF NOT EXISTS alx_book_store
        """)
        print("Database 'alx_book_store' created successfully!")
        mycursor.close()
        mydb.close()


        # connect the database just created
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "msec",
        password = "root",
        database = "alx_book_store"
    )

except Error as e:
    print(e)


