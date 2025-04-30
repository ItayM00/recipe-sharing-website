"""
    Separates Flask route functions instead of keeping everything in app.py.
    error_route.py → Handles error-related routes.
"""

from flask import Blueprint, render_template

error_bp = Blueprint("error", __name__)



@error_bp.app_errorhandler(400)
def error_400_route(e):
    return render_template("error-400.html"), 400


@error_bp.app_errorhandler(401)
def error_401_route(e):
    return render_template("error-401.html"), 401


@error_bp.app_errorhandler(403)
def error_403_route(e):
    return render_template("error-403.html"), 403


@error_bp.app_errorhandler(404)
def error_404_route(e):
    return render_template("error-404.html"), 404
    