import mysql.connector
from mysql.connector import Error

connection = None
try:

    # Create a connection to the "MYSCHEMA" database, on the MySQL instance running on localhost (port 3333).
    connection = mysql.connector.connect(host="localhost",
                                         port=3333,
                                         database="MYSCHEMA",
                                         user="root",
                                         password="password")
                                         
    # Create a cursor object, which we will use to execute SQL statements.                                                                                
    cursor = connection.cursor()

    # Ask user for details for new employee. 
    newName   = input("Name of new employee?   ")
    newSalary = input("Salary of new employee? ")
    newRegion = input("Region of new employee? ")

    # Execute a SQL statement to insert an employee. Note, you must call commit() for this change to persist.
    cursor.execute("insert into EMPLOYEES (Name, Salary, Region) values (%s, %s, %s)", (newName, newSalary, newRegion))
    connection.commit()
    print("%d rows affected" % cursor.rowcount)
    
    # Display the details of all employees, to verify a new employee has been inserted successfully. 
    cursor.execute("select * from EMPLOYEES")
    rows = cursor.fetchall()
    for row in rows:
        print("[%d] %s %f %s" % (row[0], row[1], row[2], row[3]))

except Error as e:
    print("Error connecting to database", e)

finally:
    if connection and connection.is_connected():
        connection.close()
   