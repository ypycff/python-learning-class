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

    # Display initial details for employee 1. Note the use of a parameterized SQL statement. Also note the use of fetchone().
    cursor.execute("select * from EMPLOYEES where EmployeeID = %s", ("1",))
    row = cursor.fetchone()  
    print("Initial details: [%d] %s %f %s" % (row[0], row[1], row[2], row[3]))

    # Execute a SQL statement to increase employee 1's salary by 50%. Note, you must call commit() for this change to persist.
    cursor.execute("update EMPLOYEES set Salary = Salary * %s where EmployeeID = %s", ("1.5", "1"))
    connection.commit()
    print("%d rows affected" % cursor.rowcount)  # Should be 1 row affected.
    
    # Display the details for employee 1, after 50% payrise. 
    cursor.execute("select * from EMPLOYEES where EmployeeID = %s", ("1",))
    row = cursor.fetchone()  
    print("Updated details: [%d] %s %f %s" % (row[0], row[1], row[2], row[3]))

except Error as e:
    print("Error connecting to database", e)

finally:
    if connection and connection.is_connected():
        connection.close()
   