from flask import Blueprint, flash, render_template, request
from flask_login import current_user, login_required
from .models import db, Item

tracker = Blueprint("tracker", __name__)


@login_required
@tracker.route("/", methods=["GET", "POST"])
def track():
    if request.method == "POST":
        name = request.form.get("name").strip()
        calories = request.form.get("calories").strip()
        if not name or not calories or not calories.isdigit():
            flash("Can't add, empty or improper fields", category="error")
        else:
            item = Item(name=name, calories=calories, user=current_user)
            db.session.add(item)
            db.session.commit()

    return render_template("tracker.html", user=current_user)
