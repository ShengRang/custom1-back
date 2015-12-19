from mongoengine import *

class User(Document):
    name = StringField(required=True,min_length=4,max_length=20)
    password = StringField(required=True)
    position = StringField(required=False)
    priority = IntField(required=True,default=0)

class Bill(Document):
    #id = LongField(primary_key = True)
    name = StringField(required = True)
    obj = StringField(required = True)
    xls = FileField()

class Set(Document):
    #id = LongField(primary_key = True)
    name = StringField(required = True, max_length = 256)
    sets = ListField(ReferenceField(Bill))

class Cat(Document):
    #id = LongField(primary_key = True)
    name = StringField(required = True, max_length = 256)
    cats = ListField(ReferenceField(Set))

class BillMeta(Document):
    #id = LongField(primary_key = True)
    col_names = DictField()
