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
<<<<<<< HEAD
#task = Stress(answerA = "technical", answerB = "government", answerC = "parallel", answerD = "understand", correct_answer= "understand")
=======
#task = Stress(answerA = "visitor", answerB = "attraction", answerC = "borrowing", answerD = "goverment", correct_answer= "attraction")
>>>>>>> c17391586a18a69ae2b4fd54208bebfb764bf53f
#task.save()
