from sqlalchemy import (
    create_engine, MetaData, Table, Column, Integer, String, Float, ForeignKey
)

#exceting the instructions to connect to the database
db = create_engine("postgresql:///postgres")

meta = MetaData(db)

#create variable for "Artist" table
artist_table = Table(
    "Artist", meta, 
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

#create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

#create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

#making the connection
with db.connect() as connection:
    #query 1 - select all records from the "Artist" table
    #select_query = artist_table.select()

    #query 2 - select only the "Name" column from the "Artist" table
    #select_query = artist_table.select().with_only_columns([artist_table.c.Name])# .c is a shortcut for the column method. it is used to access the columns of a table.

    #query 3 - select only "Queen" from the "Artist" table
    #select_query = artist_table.select().where(artist_table.c.Name =="Queen") #.where is used to filter the results of a query based on a condition.

    #query 4 - select tracks that belong to the "Queen" artist from the "Track" table
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)