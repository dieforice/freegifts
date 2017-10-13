from flask import *
import os
import mlab
from mongoengine import *
from models.girl_types import GirlType, dump_data
app = Flask(__name__)
app.config["SECRET_KEY"] = "jroweror3PƯƠ]ơ4oo32porwe342e3&^&^&#^@)(@(#or4343r"
mlab.connect()


@app.route('/')
def index():
    return render_template('index.html', girl_types=GirlType.objects())


@app.route('/bmi-calc')
def bmi_calc():
    return render_template("bmi_calc.html")


@app.route('/bmi')
def bmi():
    args = request.args
    weight = int(args["weight"])
    height = int(args["height"]) / 100
    bmi = weight / (height ** 2)
    return str(bmi)

@app.route('/admin')
def admin():
    if "admin" not in session:
        abort(403)
    else:
        return render_template('admin.html', girl_types=GirlType.objects())

@app.route('/delete_girl_type/<girl_id>')
def delete_girl_type(girl_id):
    girl_type = GirlType.objects().with_id(girl_id)
    if girl_type is not None:
        girl_type.delete()
    return redirect('/admin')

@app.route('/view_girl_type/<girl_id>')
def view_girl_type(girl_id):
    girl_type = GirlType.objects().with_id(girl_id)
    if girl_type is not None:
        return render_template('view.html', girl_type = girl_type)

@app.route('/edit_girl_type/<girl_id>', methods = ['GET','POST'])
def edit_girl_type(girl_id):
    girl_type = GirlType.objects().with_id(girl_id)
    if request.method == "GET":
        if girl_type is not None:
            return render_template('edit.html', girl_type = girl_type)
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        image = form["image"]
        description = form["description"]
        girl_type.update(set__name=name, set__image=image, set__description=description)
        return redirect('/admin')

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
            return "Nub"

@app.route('/images/<image_name>')
def image(image_name):
    image_folder = os.path.join(app.root_path, "static", "images")
    return send_from_directory(image_folder, image_name)

if __name__ == '__main__':
  app.run(debug=True)
