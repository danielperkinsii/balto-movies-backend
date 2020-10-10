
from peewee import *

DATABASE = SqliteDatabase('movies.db')


class Movie(Model):
    title = CharField()
    year = CharField()
    origin = CharField()
    director = CharField()
    cast = CharField()
    genre = CharField()
    wiki = CharField()
    plot = CharField()

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Movie], safe=True)
    print("TABLES Created")
    DATABASE.close()