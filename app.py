from flask import *
import mlab
from mongoengine import *
from models.girl_types import GirlType, dump_data
app = Flask(__name__)

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

@app.route('/edit_girl_type/<girl_id>')
def edit_girl_type(girl_id):
    girl_type = GirlType.objects().with_id(girl_id)
    if girl_type is not None:
        return render_template('edit.html', girl_type = girl_type)

if __name__ == '__main__':
  app.run(debug=True)
