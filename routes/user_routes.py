"""
    Separates Flask route functions instead of keeping everything in app.py.
    user_routes.py → Handles user-related routes.
"""

from flask import Blueprint, redirect, url_for, request, render_template, session, jsonify, abort
from models.user_model import *
from datetime import date

user_bp = Blueprint("user", __name__)


@user_bp.route('/login', methods=['POST', 'GET'])
def login_route():
    if request.method == 'POST':
        username = request.form['username_entry']
        password = request.form['password_entry']

        if login_user(username, password):
            session.pop('email', None)
            session['email'] = get_email_by_username(username)
            return jsonify({'redirect_url': url_for('home.home_route')}), 200
        else:
            return jsonify({'message': 'username or password are incorrect! please check'}), 401
    else:
        return render_template('login.html')
    
    
@user_bp.route('/signUp', methods=['POST', 'GET'])
def signUp_route():
    if request.method == 'POST':
        user = {}
        user['username']= session['username'] = request.form['username_entry']
        user['email'] =  request.form['email_entry']
        user['password'] = request.form['password_entry']
        user['birthdate'] = request.form['date_entry']
        user['profile_pic'] = '' 
        user['followers'] = [] 
        user['join_date'] = str(date.today())
        user['bio'] = ''
        
        if register_user(user):
            session.pop('email', None)
            session["email"] = user['email']
            return jsonify({'redirect_url': url_for('home.home_route')}), 200
        else:
            return jsonify({"error": "Invalid credentials, user already exists"}), 409
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