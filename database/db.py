"""
    The connection logic to the local MongoDB server.
    Other files will import this for the database's data
"""

from pymongo import MongoClient


#   Create a single instance of the database
client = MongoClient("mongodb://localhost:27017/")
db = client["RecipeWebsite"]