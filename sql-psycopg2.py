import psycopg2


# Connect to the "Chinook database
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 fromt the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select only the albums with "ArtistId" #51 on the "Album"
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])



# fetch the results (multiple)
# results = cursor.fetchall()

# fethc the result (single)
results = cursor.fetchone()

# close the connection
connection.close()

for result in results:
    print(result)
