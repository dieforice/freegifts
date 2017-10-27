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
    if request.method == "GET":
        a = random.randint(0,10)
        b = random.randint(11,20)
        c = random.randint(21,30)
        d = random.randint(31,40)
        return render_template('index.html', questions=Question.objects()[a], questions2=Question.objects()[b], questions3=Question.objects()[c], questions4=Question.objects()[d], stress=Stress.objects()[a])
    elif request.method == "POST":
        form = request.form
        answer1 = form["answer1"]
        answer2 = form["answer2"]
        answer3 = form["answer3"]
        answer4 = form["answer4"]
        answer5 = form["answer5"]
        if answer1 == Question.objects(correct_answer)[a]:
            return render_template('login.html')
        if answer2 == Question.objects(correct_answer)[b]:
            return render_template('login.html')
        if answer3 == Question.objects(correct_answer)[c]:
            return render_template('login.html')
        if answer4 == Question.objects(correct_answer)[d]:
            return render_template('login.html')
        if answer5 == Stress.objects(correct_answer)[a]:
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
