"""
    Separates Flask route functions instead of keeping everything in app.py.
    user_route.py → Handles user-related routes.
"""

from flask import Blueprint, redirect, url_for, request, render_template, session

user_bp = Blueprint("user", __name__)


@user_bp.route('/login', methods=['POST', 'GET'])
def login_route():
    if request.method == 'POST':
        session['username'] = request.form['username_entry']
        session['password'] = request.form['password_entry']
        return redirect(url_for('home_route'))
    else:
        return render_template('login.html')
    
    
@user_bp.route('/signUp', methods=['POST', 'GET'])
def signUp_route():
    if request.method == 'POST':
        session['username'] = request.form['username_entry']
        session['password'] = request.form['password_entry']
        session['confirmPassword'] = request.form['confirm_password_entry']
        session['email'] = request.form['email_entry']
        return redirect(url_for('home_route'))
    else:
        return render_template('signUp.html')