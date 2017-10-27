from flask import *
import os
import mlab
import random
from mongoengine import *
from models.questions import Question, Stress
from models.users import User
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
    if request.method == "GET":
        return render_template('index.html', question=Question.objects()[a], question2=Question.objects()[b], question3=Question.objects()[c], question4=Question.objects()[d], stress=Stress.objects()[a])
    elif request.method == "POST":
        form = request.form
        answer1 = form["answer1"]
        answer2 = form["answer2"]
        answer3 = form["answer3"]
        answer4 = form["answer4"]
        answer5 = form["answer5"]
        id1 = form['id1']
        id2 = form['id2']
        id3 = form['id3']
        id4 = form['id4']
        id5 = form['id5']
        question1 = Question.objects().with_id(id1)
        question2 = Question.objects().with_id(id2)
        question3 = Question.objects().with_id(id3)
        question4 = Question.objects().with_id(id4)
        stress1 = Stress.objects().with_id(id5)
        if answer1 == question1.correct_answer:
            point += 1
        if answer2 == question2.correct_answer:
            point += 1
        if answer3 == question3.correct_answer:
            point += 1
        if answer4 == question4.correct_answer:
            point += 1
        if answer5 == stress1.correct_answer:
            point += 1
        return (str(point))
@app.route('/admin', methods = ["GET","POST"])
def admin():
    if request.method == "GET":
        if "admin" not in session:
            return abort(403)
        else:
            return render_template('admin.html', questions=Question.objects(), stress = Stress.objects())

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
            return redirect('admin')
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

if __name__ == '__main__':
  app.run(debug=True)
