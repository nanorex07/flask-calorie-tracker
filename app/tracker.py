from flask import Blueprint, flash, render_template, request, abort
from flask_login import current_user, login_required
from .models import db, Item, User

tracker = Blueprint("tracker", __name__)


@tracker.route("/<id>", methods=["GET"])
def track_with_id(id):
    user = User.query.filter_by(id=id).first()
    if user:
        return render_template("user.html", user=user)

    return abort(404)


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
    pass_user = request.args.get("user")
    if pass_user:
        return render_template("tracker.html", user=pass_user)
    return render_template("tracker.html", user=current_user)
