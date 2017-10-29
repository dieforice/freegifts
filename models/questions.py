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

#task = Vocab(word = "reactor", wordA = "steel", wordB = "device", wordC = "rocket", wordD = "law", correct_word = "device")
#task = Stress(answerA = "reference", answerB = "decision", answerC = "refusal", answerD = "important", correct_answer = "reference")
#task.save()
