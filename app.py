"""
    The main Flask app that initializes everything.
"""
from flask import Flask
from routes import bluprints

def create_flask_app():

    app = Flask(__name__)
    app.secret_key = "thesupersecretkeyofitay"


    for bp in bluprints:
        app.register_blueprint(bp)

    app.run(debug=True)


if __name__ == "__main__":
    create_flask_app()
