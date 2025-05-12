"""
    Separates Flask route functions instead of keeping everything in app.py.
    recipe_route.py → Handles recipes-related routes.
"""

from flask import Blueprint, redirect, url_for, request, render_template, jsonify, session, abort
from datetime import date
from models.recipe_model import create_recipe, get_recipe_by_id, get_recipes_by_filter, objectid_to_str
from models.user_model import get_user_by_email


recipe_bp = Blueprint("recipe", __name__)
    

@recipe_bp.route('/create-recipe', methods=['POST', 'GET'])
def create_recipe_route():
    if request.method == 'POST': # submiting a form (recipe)
        try:
            data = request.json
            if not data:
                abort(400)

            data['create_date'] = str(date.today())
            creator_email = session['email']

            if not creator_email:
                abort(401) # "error": "User not logged in"
            
            user = get_user_by_email(creator_email)
            data['creator_id'] = user['_id']
            print("Received Recipe Data:", data)

            if create_recipe(data):
                print("Redirecting to home route...")
                return redirect(url_for('home.home_route'))
            else:
                abort(400) # "error": "Error in creating the recipe"
        
        except Exception as e:
            abort(400)
        
    else: # somone enters the page
        if 'email' not in session: # if user is not logged in
            return redirect(url_for('home.landing_page_route'))
        
        user = get_user_by_email(session['email'])

        if not user or 'username' not in user:
            return redirect(url_for('home.landing_page_route'))
        
        return render_template('createRecipe.html', username=user['username'])
    

@recipe_bp.route('/recipes')
def all_recipes_route():
    if 'email' not in session:  # Check if the user is logged in
       abort(401) # 'error': 'Unauthorized access to a page'
    
    return render_template('all-recipes.html')


@recipe_bp.route('/recipes/<recipe_id>')
def recipe_route(recipe_id):
    if 'email' not in session:  # Check if the user is logged in
        abort(401) # 'error': 'Unauthorized access to a page'
    
    recipe = get_recipe_by_id(recipe_id)

    if recipe == None:
        abort(404) # 'error': 'Recipe not found'
    
    return jsonify({'message': "Details for recipe: (to be implemented)"})


@recipe_bp.route('/api/recipes', methods=['GET'])
def get_recipes_api():
    if 'email' not in session:
        abort(401) # 'error': 'Unauthorized access to a page'

    filters = {}
    title = request.args.get('title')
    category = request.args.get('category')

    if title:
        filters['title'] = title
    if category:
        filters['category'] = category

    recipe_list = get_recipes_by_filter(filters)

    # Convert any ObjectId attribute to string
    recipe_list = objectid_to_str(recipe_list)

    return jsonify(recipe_list)