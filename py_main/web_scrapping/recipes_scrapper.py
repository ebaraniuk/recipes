from typing import List

from bs4 import BeautifulSoup
import pymongo
from recipes.py_main.web_scrapping.page_parser import PageParser


class RecipesParser(PageParser):

    def __init__(self, websites: List[str], mongo_client: pymongo.MongoClient):
        super().__init__(websites)
        self.client = mongo_client

    # def read_recipes(self):





