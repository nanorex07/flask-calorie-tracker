from flask import Blueprint, render_template, url_for, redirect
from flask_login import current_user

home = Blueprint("home", __name__)


@home.route("/")
def index():
    if not current_user.is_authenticated:
        return render_template("index.html", user=current_user)

    return redirect(url_for("tracker.track"))
