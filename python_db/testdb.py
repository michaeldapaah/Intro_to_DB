import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "msec", 
    password = "root",
    database = "UNIVERSITYSTORE"
)

mycursor = mydb.cursor()

# create a table for customers if it doesn't exist
mycursor.execute(
    """CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
    )"""
)

print("TABLE CREATED SUCCESSFULLY")

# to insert some data into the customers table.
query = """INSERT INTO customers (name, email) VALUES (%s, %s)"""
val = ("johnnyy doe", "johnnyydoe@example.com")
mycursor.execute(query, val)
mydb.commit()

print(mycursor.rowcount, "record(s) inserted")

val = ("mikine smith", "smithmikine@gmail.com")
mycursor.execute(query, val)
mydb.commit()

print(mycursor.rowcount, "record(s) inserted")


# read all the customer data
mycursor.execute("""SELECT * FROM customers""")
myresult = mycursor.fetchall()

print("customers:")

for row in myresult:
    print(row)

# Updata a customer email.
query = ("""UPDATE customers SET Email = %s WHERE id = %s""")
val = ("michaeldapaah@example.com", "1")
mycursor.execute(query, val)
mydb.commit()

print(mycursor.rowcount, "record(s) updated")

# read updated customer info.
mycursor.execute("""SELECT * FROM customers WHERE id = 1""")
myresult = mycursor.fetchone()

print("updated customer:")
print(myresult)

# Delete a customer
query = """DELETE FROM customers WHERE id = 2"""
mycursor.execute(query)
mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

# close connections
mycursor.close()
mydb.close()
print("Database connections closed.")