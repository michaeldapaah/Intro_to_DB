import mysql.connector

try:
    # First connection to create the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="msec",
        password="root"
    )

    if mydb.is_connected():
        print("Connected to MySQL Server")
        mycursor = mydb.cursor()

        # Create database if it doesn't exist
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

        # Close first connection
        mycursor.close()
        mydb.close()

        # Reconnect to the newly created database
        mydb = mysql.connector.connect(
            host="localhost",
            user="msec",
            password="root",
            database="alx_book_store"
        )

        if mydb.is_connected():
            print("Connected to database 'alx_book_store'")
            mycursor = mydb.cursor()

           

except mysql.connector.Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    if 'mycursor' in locals() and mycursor:
        mycursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("MySQL connection is closed")
