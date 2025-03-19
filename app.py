"""
    The main Flask app that initializes everything.
"""
from flask import Flask, redirect, url_for, request, render_template, session

app = Flask(__name__)
app.secret_key = "thesupersecretkeyofitay"

@app.route('/home')
def home_route():
    user = session.get('username', 'Guest')
    return render_template('home.html', name=user)


@app.route('/login', methods=['POST', 'GET'])
def login_route():
    if request.method == 'POST':
        session['username'] = request.form['username_entry']
        session['password'] = request.form['password_entry']
        return redirect(url_for('home_route'))
    else:
        return render_template('login.html')
    
    
@app.route('/signUp', methods=['POST', 'GET'])
def signUp_route():
    if request.method == 'POST':
        session['username'] = request.form['username_entry']
        session['password'] = request.form['password_entry']
        session['confirmPassword'] = request.form['confirm_password_entry']
        session['email'] = request.form['email_entry']
        return redirect(url_for('home_route'))
    else:
        return render_template('signUp.html')
    

@app.route('/recipe')
def recipe_route():
    return render_template('recipe.html', name="Recipe page entered<br> Steak Recipe")


if __name__ == "__main__":
    app.run(debug=True)
