"""
    Database logic
    user_model.py → Handles user-related database functions.
"""
from database.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId

users_collection = db["users"]


def register_user(user) -> bool:
    """
    All the tests for correct input will be done in the js file
    """
    if users_collection.find_one({"username":user["username"]}):
        return False
    
    # Hash the password for security
    hashed_password = generate_password_hash(user["password"])

    user["password"] = hashed_password

    # Insert user to the database
    result = users_collection.insert_one(user)

    if result.inserted_id:
        return True
    else:
        return False
    

def login_user(username, password) -> bool:
    """
    Authenticate user through email from the database, return appropriate msg
    """
    user = users_collection.find_one({"username":username})

    if user and check_password_hash(user["password"], password):
        return True
    
    return False


def get_all_users() -> list:
    """
    Get all the users in the database
    """
    return list(users_collection.find())
    

def get_user_by_email(email) -> dict:
    """
    Get all the user details via email
    """
    user = users_collection.find_one({"email":email})

    if user:
        return user
    
    return {"error":"user not found! email or password incorect"}


def get_user_by_username(username) -> dict:
    """
    Get all the user details via username
    """
    user = users_collection.find_one({"username":username})

    if(user):
        return user
    
    return {"error": "user not found! username might be incorrect"}


def get_email_by_username(username) -> str:
    user_details = get_user_by_username(username)

    if "error" in user_details:
        return user_details["error"]

    return user_details["email"]


def get_user_by_id(user_id) -> dict:
    id = ObjectId(user_id)
    user = users_collection.find_one({'_id': id})

    if user:
        return user
    
    return {'error': 'no user found in database'}
        


def update_user_details(email, new_user_details):
    user = get_user_by_email(email)

    if "error" in user:
        return user["error"]
    
    else:
        result = users_collection.update_one(
            {'email':email},
            {'$set':new_user_details}
        )

        if result.modified_count > 0:
            return {"success":"successfuly updated user information"}
        else:
            {"error":"Error in updating users information"}


def delete_user(email) -> bool:
    """
    delete a user from the database using his email
    """
    result = users_collection.delete_one({"email": email})

    return result.deleted_count > 0


