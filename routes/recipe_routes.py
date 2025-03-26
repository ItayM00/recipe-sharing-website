"""
    Separates Flask route functions instead of keeping everything in app.py.
    recipe_route.py → Handles recipes-related routes.
"""

from flask import Blueprint, redirect, url_for, request, render_template, session


recipe_bp = Blueprint("recipe", __name__)



@recipe_bp.route('/recipe')
def recipe_route():
    return render_template('recipe.html', name="Recipe page entered<br> Steak Recipe")