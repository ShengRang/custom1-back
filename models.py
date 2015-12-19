from mongoengine import *
from mongoengine.queryset import DoesNotExist
from bson.objectid import ObjectId

connect('quora')

class User(Document):
    name = StringField(required=True,min_length=4,max_length=20)
    password = StringField(required=True)
    position = StringField(required=False)
    priority = IntField(required=True,default=0)

    def get_by_id(id):
        if id:
            try:
                return User.objects.get(id=ObjectId(id))
            except DoesNotExist as e:
                return None
        return None

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
