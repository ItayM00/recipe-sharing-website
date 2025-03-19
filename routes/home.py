"""
    Separates Flask route functions instead of keeping everything in app.py.
    home.py → Handles homepage-related routes.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name="itay Mesh :)")


if __name__ == "__main__":
    app.run(debug=True)