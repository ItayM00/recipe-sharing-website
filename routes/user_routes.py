"""
    Separates Flask route functions instead of keeping everything in app.py.
    user_routes.py → Handles user-related routes.
"""

from flask import Blueprint, redirect, url_for, request, render_template, session, jsonify, abort
from models.user_model import register_user, login_user, get_email_by_username, get_user_by_email

user_bp = Blueprint("user", __name__)


@user_bp.route('/login', methods=['POST', 'GET'])
def login_route():
    if request.method == 'POST':
        username = request.form['username_entry']
        password = request.form['password_entry']

        if login_user(username, password):
            session.pop('email', None)
            session['email'] = get_email_by_username(username)
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
            session.pop('email', None)
            session["email"] = user['email']
            return redirect(url_for('home.home_route'))
        else:
            return jsonify({"error": "Invalid credentials, user already exists"}), 400
    else:
        return render_template('signUp.html')
    

@user_bp.route('/logout', methods=['POST'])
def logout_route():
    session.clear()
    return redirect(url_for('user.login_route'))
    

@user_bp.route('/<username>/profile', methods=['GET'])
def user_profile_route(username):
    if 'email' not in session:
        return redirect(url_for('user.login_route'))
    
    user = get_user_by_email(session['email'])

    if 'error' in user:
        abort(404)
    
    if user['username'] != username:  
        abort(403)
    
    return render_template('profile.html', name=user['username'])