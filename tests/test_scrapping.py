import pymongo
from recipes.py_main.web_scrapping.page_parser import PageParser


def test_scrapping():
    mongo_client = pymongo.MongoClient('localhost:27017')
    sites = [s for s in mongo_client['recipes']['sources'].find()][1]['url']
    parser = PageParser([sites])
    bss = parser.read_websites()[0]
    cleaned_bss = [str(a) for a in bss.find_all('a', href=True) if 'www.allrecipes' in str(a)]
    cleaned_bss = [a.split('href=')[1].split(" ")[0] for a in cleaned_bss]

