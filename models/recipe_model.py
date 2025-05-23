"""
    Database logic
    recipe_model.py → Handles recipe-related database functions.
"""
from database.db import db 
from bson import ObjectId

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


def delete_recipe(id) -> bool:
    result = recipe_collection.delete_one({'_id':id})

    return result.deleted_count > 0


def add_comment(recipe_id, comment) -> bool:
    id = ObjectId(recipe_id)

    result = recipe_collection.update_one(
        {'_id': id},
        {'$push': {'comments':comment}}
    )

    return result.modified_count > 0



def get_all_recipes() -> list:
    return list(recipe_collection.find())


def get_recipes_by_filter(filters) -> list:
    allowed_filters = ['title', 'category', 'likes']  # List allowed fields
    sanitized_filters = {key: value for key, value in filters.items() if key in allowed_filters}

    if 'title' in sanitized_filters:
        sanitized_filters['title'] = {'$regex': f"^{sanitized_filters['title']}", '$options': 'i'}

    if 'likes' in sanitized_filters:
        sanitized_filters['likes'] = {'likes': {'$gt': filters['likes']}}

    return list(recipe_collection.find(sanitized_filters))


def get_recipe_by_user(title, user_email) -> dict:
    recipe = recipe_collection.find_one({'creator_email':user_email, 'title':title})

    if recipe:
        return recipe
    else:
        return None
    

def get_all_recipes_by_user(user_email) -> list:
    return list(recipe_collection.find({'creator_email':user_email}))


def get_recipe_by_id(recipe_id) -> dict:
    recipe_id = ObjectId(recipe_id)
    recipe = recipe_collection.find_one({'_id':recipe_id})

    if recipe:
        recipe['ingredients'] = zip(recipe['ingredients'], recipe['sizes']) 
        objectid_to_str(recipe)
        return recipe
    else:
        return None
    

def objectid_to_str(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    elif isinstance(obj, dict):
        # If obj is a dictionary, iterate over its keys and values
        return {key: objectid_to_str(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        # If obj is a list, iterate over each item in the list
        return [objectid_to_str(item) for item in obj]
    return obj