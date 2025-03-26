"""
    The main Flask app that initializes everything.
"""
from flask import Flask
from routes import bluprints

app = Flask(__name__)
app.secret_key = "thesupersecretkeyofitay"


for bp in bluprints:
    app.register_blueprint(bp)


if __name__ == "__main__":
    app.run(debug=True)
