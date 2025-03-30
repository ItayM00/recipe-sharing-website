"""
    Database logic
    recipe_model.py → Handles recipe-related database functions.
"""
from database.db import db 

recipe_collection = db['recipes']


def create_recipe(recipe) -> bool:
    result = recipe_collection.insert_one(recipe)

    return bool(result.inserted_id)


def update_recipe(title, user_email, new_recipe) -> bool:
    result = recipe_collection.update_one(
        {'title': title, 'creator_email':user_email},
        {'$set': new_recipe}
    )
    
    return result.modified_count > 0



def delete_recipe(title, user_email) -> bool:
    result = recipe_collection.delete_one({'title':title, 'creator_email':user_email})

    return result.deleted_count > 0



def get_all_recipes() -> list:
    return list(recipe_collection.find())



def get_recipe_by_user(title, user_email) -> dict:
    recipe = recipe_collection.find_one({'creator_email':user_email, 'title':title})

    if recipe:
        return recipe
    else:
        return {'msg':'recipe not found!'}
    

def get_all_recipes_by_user(user_email) -> list:
    return list(recipe_collection.find({'creator_email':user_email}))



def get_recipe_by_title(recipe_title) -> dict:
    recipe = recipe_collection.find_one({'title':recipe_title})

    if recipe:
        return recipe
    else:
        return {'msg':'recipe not found!'}



def get_recipes_by_category(category) -> list:
    return list(recipe_collection.find({'category':category}))