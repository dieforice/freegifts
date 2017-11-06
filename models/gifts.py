from mongoengine import *
from faker import Faker
import mlab
mlab.connect()

class Gift(Document):
    gift = StringField()
    gift_name = StringField()
