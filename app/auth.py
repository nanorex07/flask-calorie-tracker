from flask import Blueprint, url_for, redirect
from authlib.integrations.flask_client import OAuth
from flask import current_app as app
from .config import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_DISCOVERY_URL
from flask_login import login_user, login_required, logout_user
from .models import User, db

auth = Blueprint("auth", __name__)
oauth = OAuth(app)
oauth.register(
    name="google",
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    server_metadata_url=GOOGLE_DISCOVERY_URL,
    client_kwargs={"scope": "openid email profile"},
)


@auth.route("/login", methods=["GET"])
def login():
    google = oauth.create_client("google")
    redirect_uri = url_for("auth.callback", _external=True)
    return google.authorize_redirect(redirect_uri)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home.index"))


@auth.route("/login/callback")
def callback():
    google = oauth.create_client("google")
    token = google.authorize_access_token()
    res = google.parse_id_token(token, nonce="")
    user = User.query.filter_by(email=res["email"]).first()
    if not user:
        user = User(
            id=res["sub"],
            email=res["email"],
            profile_pic=res["picture"],
            name=res["given_name"] + " " + res["family_name"],
        )
        db.session.add(user)
        db.session.commit()
    login_user(user=user)
    return redirect(url_for("home.index"))
