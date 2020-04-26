# Imports the drive.
import mysql.connector 

# Defines connection characteristics.
dbconfig = {'host':'ip_index_server',
            'user':'dbuser_name',
            'password':'dbpassword',
            'database':'db_name',}

# Establish the connection.
conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()

# Instantiate an object with the command to insert values into a table in the database.
_SQL = """insert into log 
(locate_table_insert)
values
(%s, %s, %s, %s, %s)"""

# Run the query.
cursor.execute(_SQL,('value_insert'))
conn.commit() # Make sure that the data entered is saved in the table.

# This query asks to see all the data in the table.
_SQL = """select * from table_name"""
cursor.execute(_SQL)

# View selected table information in an organized way.
for raw in cursor.fetchall():
    print(raw)

# Closes the cursor and the connection.
cursor.close()
conn.close()
