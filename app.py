from flask import *
import os
import mlab
import random
from mongoengine import *
from models.questions import Question
from models.users import User
app = Flask(__name__)
app.config["SECRET_KEY"] = "jroweror3PƯƠ]ơ4oo32porwe342e3&^&^&#^@)(@(#or4343r"
mlab.connect()

@app.route('/',  methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        a = random.randint(0,11)
        b = random.randint(11,21)
        c = random.randint(21,31)
<<<<<<< HEAD
        return render_template('index.html', questions=Question.objects()[a], questions2=Question.objects()[b], questions3=Question.objects()[c])
=======
        d = random.randint(31,41)
        return render_template('index.html', questions=Question.objects()[a], questions2=Question.objects()[b], questions3=Question.objects()[c], questions4=Question.objects()[d])
>>>>>>> b997075ffa28c1a077ff2f862f338368632575f3

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
