#3005 Assignment 3 - Question 1
#Lucy Wang - 101234579

#imports
import psycopg2

#getting postgres connection info from user
db = input("Enter database name: ")
username = input("Enter user name: ")
pswd = input("Enter password: ")

#making connection
connection = psycopg2.connect(
        dbname=db,
        user=username,
        password=pswd,
        host="localhost",
        port="5432"
    )

#cursor object to run queries
cursor = connection.cursor()

#CRUD FUNCTIONS
#Retrieves and displays all records from the students table
def getAllStudents():
    cursor.execute("SELECT * FROM students")
    dataset = cursor.fetchall()

    print("\nDisplaying...")
    print("student_id\tfirst_name\tlast_name\temail\t\t\t\tenrollment_date")
    for data in dataset:
        print(" {}\t\t {}\t\t {}\t\t {}\t\t {}".format(data[0], data[1], data[2], data[3], data[4]))
        #print(data)

#nserts a new student record into the students table
def addStudent(first_name, last_name, email, enrollment_date):
    values = "VALUES ('{}', '{}', '{}', '{}')".format(first_name, last_name, email, enrollment_date)
    cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) " + values)
    print("Successfully added new student")

#Updates the email address for a student with the specified student_id
def updateStudentEmail(student_id, new_email):
    cursor.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
    print("Successfully updated student's email")

#Deletes the record of the student with the specified student_id
def deleteStudent(student_id):
    cursor.execute("DELETE FROM students WHERE student_id = " + student_id)
    print("Successfully deleted student")

#APPLICATION SET UP
#options menu
print("\nSelect one of the following options (# only):")
print("\t 1. Display entire students table")
print("\t 2. Add a new student")
print("\t 3. Update email of a student")
print("\t 4. Delete a student")
print("\t 5. Quit")

#getting user input and executing based off input
select = ""
while select != "5":
    select = input("\nSelect: ")

    if select == "1":
        getAllStudents()
    elif select == "2":
        print("\nEnter student's")
        fname = input("\t First name: ")
        lname = input("\t Last name: ")
        email = input("\t Email: ")
        enrollment = input("\t Enrollment date (yyyy-mm-dd): ")
        addStudent(fname, lname, email, enrollment)
    elif select == "3":
        print("\nEnter student's")
        id = input("\t ID number: ")
        email = input("\t New email: ")
        updateStudentEmail(id, email)
    elif select == "4":
        id = input("\nEnter student's ID number: ")
        deleteStudent(id)
    elif select == "5":
        print("Have a nice day :)")
    else:
        print("Invalid option, try again")
    
    connection.commit()


#closing cursor and connection
cursor.close()
connection.close()