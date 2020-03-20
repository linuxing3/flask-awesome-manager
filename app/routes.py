from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route("/")
def index():
    key = app.config["SECRET_KEY"]
    appconfig = {"name": "emacs", "key": key}
    return render_template("index.html", app=appconfig)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            "Login Request for user {}, with me{}".format(
                form.username.data, form.remember_me.data
            )
        )
        return redirect("/")
    return render_template("login.html", form=form)
