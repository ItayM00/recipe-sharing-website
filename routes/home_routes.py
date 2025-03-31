"""
    Separates Flask route functions instead of keeping everything in app.py.
    home_route.py → Handles homepage-related routes.
"""

from flask import Blueprint, redirect, url_for, render_template, session
from models.user_model import  get_user_details

home_bp = Blueprint("home", __name__)


@home_bp.route('/home')
def home_route():
    if 'email' not in session: # if user is not logged in
        return  redirect(url_for('home_bp.landing_page_route'))
    
    user = get_user_details(session['email'])

    if 'error' in user:
        return redirect(url_for('user.login_route'))
    
    return render_template('home.html', username=user['username'])


@home_bp.route('/')
def landing_page_route():
    return render_template('landingPage.html')
