from flask import Blueprint, render_template, session
from flask_login import current_user

home = Blueprint("home", __name__)


@home.route("/")
def index():
    return render_template("index.html", user=current_user)
