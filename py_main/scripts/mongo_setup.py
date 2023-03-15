import pymongo
import os

from py_main.web_scrapping.page_parser import PageParser


def food_scrapping(client: pymongo.MongoClient):
    sites = [s for s in client['recipes']['sources'].find({'source_name': 'food'})][0]['url']
    parser = PageParser([sites])
    bss = parser.read()[0]
    cleaned_bss = [tag for tag in bss.find_all('ul') if 'dropdown' in str(tag)]
    contents = [content.contents[1::2] for content in cleaned_bss]
    contents = [c for content in contents for c in content]
    contents = contents[7::]
    links_part = [str(a).split('href=')[1].split(" ")[0][1:-3] for a in contents]
    full_links = [sites + l for l in links_part]
    names = ["_".join(n.split('/')[-1][:-8].split('-')[:-1]) for n in full_links]
    docs = [{'source_name':n, 'url': u} for u, n in zip(full_links, names)]
    client['recipes']['sources'].insert_many(docs)
    client['recipes']['sources'].delete_one({'site_name': 'food'})


if __name__ == '__main__':
    mongo_path = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(mongo_path)
    sites_db = client['recipes']
    collection = sites_db['sources']
    collection.drop()
    with open(os.path.abspath('../../data/somesites.txt')) as file:
        sites = file.readlines()
    sites = [s.replace('\n', '') for s in sites]
    names = [s.split('www.')[1] for s in sites]
    names = [s.split('.com')[0] for s in names]
    add_dict = [{'source_name': name, 'url': url} for name, url in zip(names, sites)]
    collection.insert_many(add_dict)
    food_scrapping(client)

