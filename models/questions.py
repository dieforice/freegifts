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

<<<<<<< HEAD
#task = Question(question = "If I _____ an animal, I ______ a cat", answerA="was/will be", answerB = "was/would be", answerC = "were/will be", answerD = "were/would be", correct_answer = "were/would be")
=======
#task = Question(question = "Alexander the Great created one of the largest _______ of the ancient world ____ the age of thirty", answerA = "kingdoms/up until", answerB = "empires/at", answerC = "empires/by", answerD = "nations/at", correct_answer = "empires/by")
>>>>>>> b997075ffa28c1a077ff2f862f338368632575f3
#task.save()
