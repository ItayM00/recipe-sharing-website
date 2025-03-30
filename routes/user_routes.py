"""
    Separates Flask route functions instead of keeping everything in app.py.
    user_routes.py → Handles user-related routes.
"""

from flask import Blueprint, redirect, url_for, request, render_template, session, jsonify
from models.user_model import register_user, login_user

user_bp = Blueprint("user", __name__)


@user_bp.route('/login', methods=['POST', 'GET'])
def login_route():
    if request.method == 'POST':
        email = request.form['email_entry']
        password = request.form['password_entry']
        session['email'] = email

        if login_user(email, password):
            return redirect(url_for('home.home_route'))
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    else:
        return render_template('login.html')
    
    
@user_bp.route('/signUp', methods=['POST', 'GET'])
def signUp_route():
    if request.method == 'POST':
        user = {}
        user['username']= session['username'] = request.form['username_entry']
        user['email'] =  request.form['email_entry']
        user['password'] = request.form['password_entry']
        
        if register_user(user):
            return redirect(url_for('home.home_route'))
        else:
            return jsonify({"error": "Invalid credentials, user already exists"}), 400
    else:
        return render_template('signUp.html')