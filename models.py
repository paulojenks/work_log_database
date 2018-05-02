import datetime

from peewee import *


db = SqliteDatabase('work_log.db')


class Entry(Model):
    name = CharField(max_length=255)
    task = CharField(max_length=255)
    timestamp = DateTimeField(default=datetime.date.today)
    minutes = IntegerField()
    notes = TextField()

    class Meta:
        database = db

def initialize():
    db.connect()
    db.create_tables([Entry], safe=True)


if __name__ == "__main__":
    initialize()