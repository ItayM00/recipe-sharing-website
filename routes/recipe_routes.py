"""
    Separates Flask route functions instead of keeping everything in app.py.
    recipe_route.py → Handles recipes-related routes.
"""

from flask import Blueprint, redirect, url_for, request, render_template, jsonify, session
from datetime import date
from models.recipe_model import create_recipe, get_recipe_by_id


recipe_bp = Blueprint("recipe", __name__)
    

@recipe_bp.route('/create-recipe', methods=['POST', 'GET'])
def create_recipe_route():
    if request.method == 'POST': # submiting a form (recipe)
        try:
            data = request.json

            if not data:
                return jsonify({"error": "No data received"}), 400

            data['create_date'] = str(date.today())
            data['creator_email'] = session.get('email')

            if not data['creator_email']:
                return jsonify({"error": "User not logged in"}), 401

            print("Received Recipe Data:", data)

            if create_recipe(data):
                print("Redirecting to home route...")
                return redirect(url_for('home.home_route'))
            else:
                return jsonify({"error": "Error in creating the recipe"}), 500
        
        except Exception as e:
            return jsonify({"error": str(e)}), 400
        
    else: # somone enters the page
        return render_template('createRecipe.html')
    

@recipe_bp.route('/recipes')
def all_recipes_route():
    if 'email' not in session:  # Check if the user is logged in
        return jsonify({'error': 'Unauthorized access to a page'}), 401
    
    return jsonify({'message': 'List of recipes (to be implemented in the future)'})


@recipe_bp.route('/recipes/<recipe_id>')
def recipe_route(recipe_id):
    if 'email' not in session:  # Check if the user is logged in
        return jsonify({'error': 'Unauthorized access to a page'}), 401
    
    recipe = get_recipe_by_id(recipe_id)

    if recipe == None:
        return jsonify({'error': 'Recipe not found'}), 404
    
    return jsonify({'message': "Details for recipe: (to be implemented)"})