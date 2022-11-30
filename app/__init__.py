from flask import Flask
from .auth import auth
from .home import home
from .config import SECRET_KEY, SQLALCHEMY_DATABASE_URI
from flask_login import LoginManager
from .models import db, User

app = Flask(__name__)


app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


with app.app_context():
    db.create_all()

# blueprints
app.register_blueprint(home, url_prefix="/")
app.register_blueprint(auth, url_prefix="/auth")
