from mongoengine import *
from faker import Faker
import mlab
mlab.connect()
class Question(Document): #Collection
    question = StringField()
    answerA = StringField()
    answerB = StringField()
    answerC = StringField()
    answerD = StringField()
    correct_answer = StringField()

#task = Question(question = "If I _____ an animal, I ______ a cat", answerA="was/will be", answerB = "was/would be", answerC = "were/will be", answerD = "were/would be", correct_answer = "were/would be")
#task.save()
