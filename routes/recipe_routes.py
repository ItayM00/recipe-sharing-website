"""
    Separates Flask route functions instead of keeping everything in app.py.
    recipe_route.py → Handles recipes-related routes.
"""

from flask import Blueprint, redirect, url_for, request, render_template, jsonify, session
from datetime import date
from models.recipe_model import create_recipe


recipe_bp = Blueprint("recipe", __name__)
    

@recipe_bp.route('/createRecipe', methods=['POST', 'GET'])
def create_recipe_route():
    if request.method == 'POST': # submiting a form (recipe)
        try:
            data = request.json

            if not data:
                return jsonify({"error": "No data received"}), 400

            data['create_date'] = date.today()
            data['creator_email'] = session.get('email')

            if not data['creator_email']:
                return jsonify({"error": "User not logged in"}), 401

            print("Received Recipe Data:", data)

            if create_recipe(data):
                return redirect(url_for('home.home_route'))
            else:
                return jsonify({"error": "Error in creating the recipe"}), 401
        
        except Exception as e:
            return jsonify({"error": str(e)}), 400
        
    else: # somone enters the page
        return render_template('createRecipe.html')