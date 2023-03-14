import pymongo
import os

if __name__ == '__main__':
    mongo_path = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(mongo_path)
    sites_db = client['recipes']
    collection = sites_db['sources']
    with open(os.path.abspath('../../data/somesites.txt')) as file:
        sites = file.readlines()
    sites = [s.replace('\n', '') for s in sites]
    names = [s.split('www.')[1] for s in sites]
    names = [s.split('.com')[0] for s in names]
    add_dict = [{'site_name': name, 'url': url} for name, url in zip(names, sites)]
    collection.insert_many(add_dict)
