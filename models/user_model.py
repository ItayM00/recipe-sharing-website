"""
    Database logic
    user.py → Handles user-related database functions.
"""
from database.db import db
from werkzeug.security import generate_password_hash, check_password_hash

users_collection = db["users"]


def register_user(user):
    """
    All the tests for correct input will be done in the js file
    """
    if users_collection.find_one({"email":user["email"]}):
        return False
    
    # Hash the password for security
    hashed_password = generate_password_hash(user["password"])

    user["password"] = hashed_password

    # Insert user to the database
    users_collection.insert_one(user)
    return True
    

def login_user(email, password):
    """
    Authenticate user through email from the database, return appropriate msg
    """
    user = users_collection.find_one({"email":email})

    if user and check_password_hash(user["password"], password):
        return True
    
    return False


def get_all_users():
    """
    Get all the users in the database
    """
    return users_collection
    

def get_user_details(email):
    """
    Get all the user details via email
    """
    user = users_collection.find_one({"email":email})

    if user:
        return user
    
    return {"msg":"Error! email or password incorect"}


def update_user_details(email):
    user = get_user_details(email)

    if user.get("msg"):
        return user["msg"]
    else:
        pass # for now


def delete_user(email):
    """
    delete a user from the database using his email
    """
    result = users_collection.delete_one({"email": email})

    if result.deleted_count > 0:
        return True # code for "user deleted successfuly"
    
    return False # code for "an error of some kind"


