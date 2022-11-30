from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Text, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    profile_pic = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    items = db.relationship("Item", backref="user")


class Item(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True), default=func.now())
    calories = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Text, db.ForeignKey("user.id"))
