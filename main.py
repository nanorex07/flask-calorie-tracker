from app import app as application
from waitress import serve

if __name__ == "__main__":
    serve(application, host="0.0.0.0", port=8080)
