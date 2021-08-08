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

    # Execute a SQL statement to query all rows in the EMPLOYEES statement.
    cursor.execute("select * from EMPLOYEES")
    
    # Fetch all the rows of the query result set. 
    rows = cursor.fetchall()
    
    # Display the row count.
    print("Number of employees: %d" % len(rows))
    
except Error as e:
    print("Error connecting to database", e)

finally:
    if connection and connection.is_connected():
        connection.close()
   