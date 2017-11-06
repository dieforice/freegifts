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
class Stress(Document): #Collection
    # = StringField()
    answerA = StringField()
    answerB = StringField()
    answerC = StringField()
    answerD = StringField()
    correct_answer = StringField()

class Vocab(Document):
    word = StringField()
    wordA = StringField()
    wordB = StringField()
    wordC = StringField()
    wordD = StringField()
    correct_word = StringField()

class Math(Document):
    question = StringField()
    answerA = StringField()
    answerB = StringField()
    answerC = StringField()
    answerD = StringField()
    correct_answer = StringField()

#task = Vocab(word = "reactor", wordA = "steel", wordB = "device", wordC = "rocket", wordD = "law", correct_word = "device")
#task = Math(question = "If 3^(5x) = 27^4, what is the value of x?", answerA = "9/c", answerB = "100c/3", answerC = "300/c", answerD = "c/100", correct_answer = "C")
#task.save()
