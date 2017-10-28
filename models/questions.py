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

#task = Vocab(word = "convivial", wordA = "loudly", wordB = "stealthy", wordC = "sociable", wordD = "vintage", correct_word = "sociable")
#task = Stress(answerA = "reference", answerB = "decision", answerC = "refusal", answerD = "important", correct_answer = "reference")
#task.save()
