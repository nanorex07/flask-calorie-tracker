from flask import Blueprint, render_template, url_for, redirect
from flask_login import current_user
from .models import User

home = Blueprint("home", __name__)


@home.route("/")
def index():
    users = User.query.all()
    return render_template("index.html", users=users, current=current_user)
