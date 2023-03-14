from typing import List
import requests
import certifi
import ssl

from bs4 import BeautifulSoup


class WebScrapper:

    def __init__(self, websites: List[str]):
        self.https = [requests.get(url).content for url in websites]

    def read(self):
        b_soup_objs = [BeautifulSoup(http, 'html.parser') for http in self.https]
        return b_soup_objs

