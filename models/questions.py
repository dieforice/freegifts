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

#task = Question(question = "Alexander the Great created one of the largest _______ of the ancient world ____ the age of thirty", answerA = "kingdoms/up until", answerB = "empires/at", answerC = "empires/by", answerD = "nations/at", correct_answer = "empires/by")
#task = Stress(answerA = "visitor", answerB = "attraction", answerC = "borrowing", answerD = "goverment", correct_answer= "attraction")
#task.save()
