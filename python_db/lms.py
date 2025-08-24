import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "msec",
    password = "root",
    database = "UNIVERSITYSTORE"
)

mycursor = mydb.cursor()

# CREATE A LMS TABLE IF IT DOESN'T EXIST
mycursor.execute("""
CREATE TABLE IF NOT EXISTS LMSs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    isbn VARCHAR(20) NOT NULL
)
""")


# print("TABLE CREATED SUCCESSFULLY")

# ADDING A BOOK (INSERT)
def addBook(title, author, isbn):
    sql = """INSERT INTO LMSs (title, author, isbn) VALUES (%s, %s, %s)"""
    val = (title, author, isbn)
    # val = (1, "How to sell", "Michael J. Dapaah", 43218)
    mycursor.execute(sql, val)
    mydb.commit()

# LIST ALL BOOKS (READ)

def listBook():
    sql = """SELECT * FROM LMSs"""
    mycursor.execute(sql)
    results = mycursor.fetchall()
    print("All books in the library: ")
    for book in results:
        print(f"ID: {book[0]}, Title: {book[1]}, author: {book[2]}, isbn: {book[3]}")


def searchbook(title):
    sql = """SELECT * FROM LMSs WHERE title LIKE %s"""
    mycursor.execute(sql, ('%' + title + '%',))
    result = mycursor.fetchall()
    if result:
        print("Search result:")
        for book in result:
            print(f"ID: {book[0]}, Title: {book[1]}, author: {book[2]}, isbn: {book[3]}")
    else: 
        print("no books found")

def deletebook(isbn):
    sql = """DELETE FROM LMSs WHERE isbn = %s"""
    val = (isbn,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(f"Book with ISBN {isbn} deleted successfully")

    



while True: 
    print("Library Management System")
    print("1. Add Book")
    print("2. list all books")
    print("3. Search book")
    print("4. Delete book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':

        title = input("Enter book title: ")
        author = input("Enter the name of the author: ")
        isbn = input("Enter the isbn number: ")
        addBook(title, author, isbn)

    elif choice == '2':
        listBook()

    elif choice == '3':
        title = input("Enter the title of the book you want to search")
        searchbook(title)

    elif choice == '4':
        isbn = input("Enter the isbn number of the book you want to delete:")
        deletebook(isbn)

    elif choice == '5':
        print("Exiting....")
        break

    else:
        print("invalid choice, try again")


mycursor.close()
mydb.close()