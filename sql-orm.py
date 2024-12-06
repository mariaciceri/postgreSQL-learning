from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#executing the instructions from the database
db = create_engine('postgresql:///postgres')# /// means local host and postgres is the database name
base = declarative_base() #take the metadata and creates a subclass to map everything

class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))

class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


#instead of connecting to the database directly, we will ask for a session
#create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
#opens and actual session by calling the Session() subclass defined above
session = Session()
#creating the database using declarative_base subclass
base.metadata.create_all(db)

#query 1 - select all records from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=' | ')

#query 2 - select only the "Name" column from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

#query 3 - select only "Queen" from the "Artist" table
# artist = session.query(Artist).filter_by(Name="Queen").first()#first() returns the first result
# print(artist.ArtistId, artist.Name, sep=' | ')

#query 4 - select only the albums with "ArtistId" of 51 from the "Album" table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=' | ')

tracks = session.query(Track).filter_by(Composer = "Queen")
for track in tracks:
    print(track.TrackId,
          track.Name,
          track.AlbumId,
          track.MediaTypeId,
          track.GenreId,
          track.Composer,
          track.Milliseconds,
          track.Bytes,
          track.UnitPrice,
          sep=' | ')