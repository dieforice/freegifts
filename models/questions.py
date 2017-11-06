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
#task = Question(question = "The coach does not expect his players to be _____, that is, lacking energy before an important game", answerA = "irksome", answerB = "pejorative", answerC = "verisimilitude", answerD = "listless", correct_answer = "C")
#task.save()
