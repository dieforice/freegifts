from flask import *
import os
import mlab
from mongoengine import *
from models.questions import Question
from models.users import User
app = Flask(__name__)
app.config["SECRET_KEY"] = "jroweror3PƯƠ]ơ4oo32porwe342e3&^&^&#^@)(@(#or4343r"
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html', questions=Question.objects())

@app.route('/admin')
def admin():
    if "admin" not in session:
        abort(403)
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

        user = User.objects(username=username).first()
        if user is None:
            flash("No such user")
            return render_template("login.html")
        else:
            if user.password != password:
                flash("Wrong Password")
                return render_template('login.html')
            else:
                session['admin'] = True
                return redirect('admin')
        if username == "admin" and password == "admin":
            session['admin'] = True
            return redirect('/admin')
        else:
            flash("Wrong username or password")
            return render_template("login.html")


if __name__ == '__main__':
  app.run(debug=True)
