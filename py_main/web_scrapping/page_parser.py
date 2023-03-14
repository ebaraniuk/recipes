from typing import List

from bs4 import BeautifulSoup
import pymongo
from recipes.py_main.web_scrapping.web_scrapper import WebScrapper


class PageParser(WebScrapper):

    def __init__(self, websites: List[str]):
        super().__init__(websites)



