from pymongo import MongoClient

class BancoDado:

    def __init__(self, database='db', host='localhost', port=27017):
        self.database = database
        self.client = MongoClient(host=host, port=port)
        self.db = self.client[self.database]

    def add(self, collection='collection', json={}):
        return self.db[collection].insert_one(json).inserted_id