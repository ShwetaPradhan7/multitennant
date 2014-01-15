from django.db import models
from mongoengine import *
from multitennant.settings import DBNAME


# Create your models here.
c= connect(DBNAME)

class sciences(Document):
    user = StringField()
    text = StringField()
