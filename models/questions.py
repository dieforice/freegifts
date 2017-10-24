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

#task = Question(question = "I managed to finish all the work _______________ I was very tired", answerA = "although", answerB = "so", answerC = "but", answerD = "because")
#task.save()
