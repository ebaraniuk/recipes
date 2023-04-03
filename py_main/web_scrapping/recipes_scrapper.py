from typing import List

from bs4 import BeautifulSoup
import pymongo
from recipes.py_main.web_scrapping.page_parser import PageParser


class RecipesParser(PageParser):

    def __init__(self, mongo_client: pymongo.MongoClient):
        collected_data = mongo_client['recipes']['sources'].find()
        websites = [d['url'] for d in collected_data]
        super().__init__(websites)
    #
    # def read_recipes(self):
        