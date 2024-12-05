import psycopg2

#connect to "chinook" database
#can pass other parameters like user, password, host, port
connection = psycopg2.connect(database="chinook", port="5433")

#build a cursor object of the database
#cursor is a control structure that enables traversal over the records in a database
cursor = connection.cursor() 

#Query 1 - select all records from the "Artist" table
cursor.execute('SELECT * FROM "Artist"')

#fetch the results (multiple)   
results = cursor.fetchall()

#fetch the results (single)
#result = cursor.fetchone()

#close the connection
connection.close()

#display the results
for result in results:
    print(result)