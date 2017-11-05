from flask import *
import os
import mlab
import random
from mongoengine import *
from models.questions import Question, Stress, Vocab
from models.users import User
from models.gifts import Gift
from gmail import *
app = Flask(__name__)
app.config["SECRET_KEY"] = "jroweror3PƯo32porwe342e3&^&^&#^@)(@(#or4343r"
mlab.connect()

@app.route('/',  methods = ["GET", "POST"])
def index():
    point = 0
    a = random.randint(0,9)
    b = random.randint(10,19)
    c = random.randint(20,29)
    d = random.randint(30,39)
    e = random.randint(40,49)
    f = random.randint(50,69)
    g = random.randint(70,89)
    h = random.randint(0,19)
    j = random.randint(20,39)
    if request.method == "GET":
        return render_template('index.html', question=Question.objects()[h], question2=Question.objects()[f], question3=Question.objects()[g], question4=Question.objects()[j],question5 =Question.objects()[e], stress=Stress.objects()[a],stress2 = Stress.objects()[b], vocab= Vocab.objects()[a], vocab2= Vocab.objects()[b], vocab3= Vocab.objects()[c] )
    elif request.method == "POST":
        form = request.form
        answer1 = form["answer1"]
        answer2 = form["answer2"]
        answer3 = form["answer3"]
        answer4 = form["answer4"]
        answer5 = form["answer5"]
        answer6 = form["answer6"]
        answer7 = form["answer7"]
        answer8 = form["answer8"]
        answer9 = form["answer9"]
        answer10 = form["answer10"]
        id1 = form['id1']
        id2 = form['id2']
        id3 = form['id3']
        id4 = form['id4']
        id5 = form['id5']
        id6 = form['id6']
        id7 = form['id7']
        id8 = form['id8']
        id9 = form['id9']
        id10 = form['id10']
        question1 = Question.objects().with_id(id1)
        question2 = Question.objects().with_id(id2)
        question3 = Question.objects().with_id(id3)
        question4 = Question.objects().with_id(id4)
        question5 = Question.objects().with_id(id10)
        stress1 = Stress.objects().with_id(id5)
        stress2 = Stress.objects().with_id(id6)
        vocab = Vocab.objects().with_id(id7)
        vocab2 = Vocab.objects().with_id(id8)
        vocab3 = Vocab.objects().with_id(id9)
        if answer1.upper() == question1.correct_answer:
            point += 1
        if answer2.upper() == question2.correct_answer:
            point += 1
        if answer3.upper() == question3.correct_answer:
            point += 1
        if answer4.upper() == question4.correct_answer:
            point += 1
        if answer5.upper() == stress1.correct_answer:
            point += 1
        if answer6.upper() == stress2.correct_answer:
            point += 1
        if answer7.upper() == vocab.correct_word:
            point += 1
        if answer8.upper() == vocab2.correct_word:
            point += 1
        if answer9.upper() == vocab3.correct_word:
            point += 1
        if answer10.upper() == question5.correct_answer:
            point += 1
        if point < 6:
            return render_template('no_gift.html', point = point)
        if point == 6:
            z = random.randint(0,1)
            user_gift = Gift.objects()[z]
            #gift_id = str(user_gift.id)
            return render_template('send_gift.html', user_gift = user_gift, point= point)
        elif point == 7:
            z = random.randint(2,3)
            user_gift = Gift.objects()[z]
            #gift_id = str(user_gift.id)
            return render_template('send_gift.html', user_gift = user_gift, point= point)
        elif point == 8:
            z = random.randint(4,5)
            user_gift = Gift.objects()[z]
            #gift_id = str(user_gift.id)
            return render_template('send_gift.html', user_gift = user_gift, point= point)
        elif point == 9:
            user_gift = Gift.objects()[6]
            #gift_id = str(user_gift.id)
            return render_template('send_gift.html', user_gift = user_gift, point= point)
        elif point == 10:
            user_gift = Gift.objects()[7]
            #gift_id = str(user_gift.id)
            return render_template('send_gift.html', user_gift = user_gift, point= point)


@app.route('/admin', methods = ["GET","POST"])
def admin():
    if request.method == "GET":
        if "admin" not in session:
            return abort(403)
        else:
            return render_template('admin.html', questions=Question.objects(), stress = Stress.objects(), vocab = Vocab.objects(), gifts = Gift.objects())

@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]
        user = User.objects(username=username).first()
    if user is None:
            flash("No such user")
            return render_template("login.html")
    else:
        if user.password != password:
            flash("Wrong password")
            return render_template('login.html')
        else:
            session['admin'] = True
            return redirect('/admin')
    # if username == "admin" and password == "admin":
    #     session['admin'] = True
    #     return redirect('/admin')
    # else:
    #     flash("Username or Password was wrong")
    #     return render_template("login.html")

@app.route('/edit_mp/<question_id>', methods = ["GET","POST"])
def edit_mp(question_id):
    question_edit= Question.objects().with_id(question_id)
    if request.method == "GET":
        if question_edit is not None:
            return render_template('edit_mp.html', question_edit = question_edit)
    elif request.method =="POST":
        form = request.form
        question = form["question"]
        answerA = form["answerA"]
        answerB = form["answerB"]
        answerC = form["answerC"]
        answerD = form["answerD"]
        correct_answer = form["correct_answer"]
        question_edit.update(set__question = question, set__answerA= answerA, set__answerB =answerB, set__answerC = answerC, set__answerD= answerD, set__correct_answer = correct_answer)
        return redirect('/admin')

@app.route('/edit_stress/<question_id>', methods = ["GET","POST"])
def edit_stress(question_id):
    question_edit= Stress.objects().with_id(question_id)
    if request.method == "GET":
        if question_edit is not None:
            return render_template('edit_stress.html', question_edit = question_edit)
    elif request.method =="POST":
        form = request.form
        answerA = form["answerA"]
        answerB = form["answerB"]
        answerC = form["answerC"]
        answerD = form["answerD"]
        correct_answer = form["correct_answer"]
        question_edit.update(set__answerA= answerA, set__answerB =answerB, set__answerC = answerC, set__answerD= answerD, set__correct_answer = correct_answer)
        return redirect('/admin')

@app.route('/edit_vocab/<vocab_id>', methods = ["GET","POST"])
def edit_vocab(vocab_id):
    vocab_edit= Vocab.objects().with_id(vocab_id)
    if request.method == "GET":
        if vocab_edit is not None:
            return render_template('edit_vocab.html', vocab_edit = vocab_edit)
    elif request.method =="POST":
        form = request.form
        word = form["word"]
        wordA = form["wordA"]
        wordB = form["wordB"]
        wordC = form["wordC"]
        wordD = form["wordD"]
        correct_word = form["correct_word"]
        vocab_edit.update(set__word = word, set__wordA= wordA, set__wordB =wordB, set__wordC = wordC, set__wordD= wordD, set__correct_word = correct_word)
        return redirect('/admin')

@app.route('/send_gift/<gift_id>', methods = ["GET", "POST"])
def send_gift(gift_id):
    user_gift = Gift.objects().with_id(gift_id)
    if request.method == "GET":
        if user_gift is not None:
            return render_template('send_gift.html', user_gift = user_gift)
    if request.method == "POST":
        form = request.form
        email = form["email"]
        wish = form["wish"]
        gmail = GMail('Cadeaux<dieforice@gmail.com>','areqiznzrwzjaolz')
        msg = Message(wish,to=email,text = user_gift.gift)
        gmail.send(msg)
        return render_template('gift_sent.html')
@app.route('/admingift', methods = ["GET", "POST"])
def admingift():
    if request.method == "GET":
        return render_template('admingift.html',gifts = Gift.objects())

if __name__ == '__main__':
  app.run(debug=True)
