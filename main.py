from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5


class MyForm(FlaskForm):
    email = StringField(label='Emai', validators=[DataRequired(), Email(message='enter a valid email',
                                                                         check_deliverability=True)])
    password = PasswordField(label='Password',
                             validators=[DataRequired(), Length(min=8, message="atleast 8 character")])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "dhoommachale"
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    log = MyForm()
    if log.validate_on_submit():  # <form_object>.<form_field>.data
        if log.email.data == "suyashj90@gmail.com" and log.password.data == "123456789":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", forms=log)


if __name__ == '__main__':
    app.run(debug=True)
