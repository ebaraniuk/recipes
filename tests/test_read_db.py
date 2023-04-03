import pymongo
from py_main.web_scrapping.recipes_scrapper import RecipesParser

def test_read_recipes():

    mongo_client = pymongo.MongoClient('localhost:27017')
    parser = RecipesParser(mongo_client)
    # recipes = parser.read_recipes()