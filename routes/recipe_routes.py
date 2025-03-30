"""
    Separates Flask route functions instead of keeping everything in app.py.
    recipe_route.py → Handles recipes-related routes.
"""

from flask import Blueprint, redirect, url_for, request, render_template, jsonify


recipe_bp = Blueprint("recipe", __name__)



@recipe_bp.route('/storeRecipe', methods=['POST'])
def recipe_route():
    try:
        data = request.json
        print("Received Recipe Data:", data)

        # Process the data (saving it to the database here)
        
        return redirect(url_for('home.home_route'))
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    

@recipe_bp.route('/createRecipe', methods=['POST'])
def create_recipe_route():

    return render_template('createRecipe.html')