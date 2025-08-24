import mysql.connector

def get_Connection():
    return mysql.connector.connect(
        host = "localhost",
        user = "msec",
        password = "root",
        database = "UNIVERSITYSTORE"
    )

# insert new student informaiton
def create_student():
    conn = get_Connection()
    print("Connection Successful")
    cursor = conn.cursor()
    query = """INSERT INTO Students (StudentID, FirstName, LastName, Email, EnrollmentDate) VALUES (%s, %s, %s, %s, %s)"""
    values = ("student_id, first_name, last_name, email, enrollment_date")
    cursor.execute(query, values)
    conn.commit()
    print("Student Created Successfully")
    cursor.close()
    conn.close()


# fetch all student information
def read_students():
    conn = get_Connection()
    print("connection successful")
    cursor = conn.cursor()
    cursor.execute("SELECT StudentID, FirstName, LastName, Email, EnrollmentDate FROM Students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()

def update_student_email(StudentID, new_email):
    conn = get_Connection()
    print("connection successful")
    cursor = conn.cursor()
    query = """UPDATE Students SET Email = %s  WHERE StudentID = %s"""
    cursor.execute(query, (new_email, StudentID))
    conn.commit()
    print("Student Email Updated Successfully")
    cursor.close()
    conn.close()

def delete_student(StudentID):
    conn = get_Connection()
    print("connection successful")
    cursor = conn.cursor()
    query = """DELETE FROM Students WHERE StudentID = %s"""
    cursor.execute(query, (StudentID))
    conn.commit()
    print("Student Deleted Successfully")
    cursor.close()
    conn.close()


if __name__ == "__main__":
    # create_student()
    update_student_email("103", "michaeldapaah@gmail.com")
    read_students()
    # delete_student("S12345")
    getconn = get_Connection()
    print(getconn.server_info)
    # print(get_Connection().get_server_info())