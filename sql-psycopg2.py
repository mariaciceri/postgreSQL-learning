import psycopg2

#connect to "chinook" database
#can pass other parameters like user, password, host, port
connection = psycopg2.connect(database="postgres")

#build a cursor object of the database
#cursor is a control structure that enables traversal over the records in a database
cursor = connection.cursor() 

#Query 1 - select all records from the "Artist" table
#cursor.execute('SELECT * FROM "Artist"')

#Query 2 - select only the "Name" column from the "Artist" table
#cursor.execute('SELECT "Name" FROM "Artist"')

#query 3 - select only "Queen" from the "Artist" table
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"]) #need a placeholder for the string value because of quotes 

#Query 4 - select only by "ArtistId" #51 from the "Artist" table
#cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

#Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
cursor.execute('SELECT * FROM "Album" WHERE "AlbumId" = %s', [7])

#fetch the results (multiple)   
#results = cursor.fetchall()

#fetch the results (single)
results = cursor.fetchone()

#display the results
for result in results:
    print(result)

#close the cursor
cursor.close()
#close the connection
connection.close()