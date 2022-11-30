from os import environ as env
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = env.get("SECRET_KEY", "flask")

GOOGLE_CLIENT_ID = env.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = env.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"


SQLALCHEMY_DATABASE_URI = env.get("SQLALCHEMY_DATABASE_URI")
