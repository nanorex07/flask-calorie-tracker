from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Text, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    profile_pic = db.Column(db.String(100))
    name = db.Column(db.String(1000))
