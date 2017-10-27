from flask import *
import os
import mlab
import random
from mongoengine import *
from models.questions import Question, Stress
from models.users import User
app = Flask(__name__)
app.config["SECRET_KEY"] = "jroweror3PƯƠ]ơ4oo32porwe342e3&^&^&#^@)(@(#or4343r"
mlab.connect()

@app.route('/',  methods = ["GET", "POST"])
def index():
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
            return render_template('login.html')
        if answer2 == question2.correct_answer:
            return render_template('login.html')
        if answer3 == question3.correct_answer:
            return render_template('login.html')
        if answer4 == question4.correct_answer:
            return render_template('login.html')
        if answer5 == stress1.correct_answer:
            return render_template('login.html')
@app.route('/admin')
def admin():
    if "admin" not in session:
        return abort(403)
    else:
        return render_template('admin.html', questions=Question.objects())

@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]


    if username == "admin" and password == "admin":
        session['admin'] = True
        return redirect('/admin')
    else:
        return abort(403)


if __name__ == '__main__':
  app.run(debug=True)
