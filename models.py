from mongoengine import connect, Document, CASCADE
from mongoengine.fields import ReferenceField, ListField, StringField



class Author(Document):
    fullname = StringField(max_length=50)
    born_date = StringField(max_length=20)
    born_location = StringField(max_length=100)
    bio = StringField()


class Quote(Document):
    tags = ListField()
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField()
