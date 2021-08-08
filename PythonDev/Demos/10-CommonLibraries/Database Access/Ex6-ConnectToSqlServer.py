import pyodbc 
import pandas as pd

conn = pyodbc.connect("driver={ODBC Driver 17 for SQL Server};"
                      "server=(localdb)\\MSSQLLocalDB;"
                      "database=MySampleDatabase;"
                      "integrated security=true")

query = "SELECT * FROM Products"

print("\nExecute a SQL query and loop through rows manually...")
cursor = conn.cursor()
cursor.execute(query)
for row in cursor:
    print('row = %s' % (row,))
    
print("\nUse Pandas to execute the statement and create a DataFrame...")
df = pd.read_sql(query, conn)
print(df.head(3))

df.to_json("Products.json")
