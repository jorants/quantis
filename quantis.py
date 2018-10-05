from flask import Flask, jsonify, render_template
from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired, Length


import randomstr
from tests import all_tests



app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

@app.route("/rand/<int:n>")
def rand(n):
    return jsonify(randomstr.get_alphabet(n))


class MainForm(FlaskForm):
    text = TextAreaField(
        'Text',
        validators = [Length(100, 100, "Type het vak vol.")]
    )

@app.route("/",methods=["GET","POST"])
def form():
    form = MainForm()
    if form.validate_on_submit():
        passed, score, results = all_tests(form.text.data.lower())
        return render_template('results.html', results = results, passed = passed)
    else:
        return render_template('form.html', form=form)



if __name__ == "__main__":
    app.run("0.0.0.0",8080)
