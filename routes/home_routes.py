"""
    Separates Flask route functions instead of keeping everything in app.py.
    home_route.py → Handles homepage-related routes.
"""

from flask import Blueprint, redirect, url_for, request, render_template, session

home_bp = Blueprint("home", __name__)


@home_bp.route('/home')
def home_route():
    user = session.get('username', 'Guest')
    return render_template('home.html', name=user)