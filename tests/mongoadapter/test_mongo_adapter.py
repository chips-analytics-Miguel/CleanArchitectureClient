import unittest
from pymongo import MongoClient
from  src.adapters.mongodb.mongoadapter import MongoDBAdapter

class TestMongoDBAdapter(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient()
        self.db = self.client.test_database
        self.adapter = MongoDBAdapter(mongo_uri='mongodb://localhost:27017/test_database')

    def tearDown(self):
        self.client.drop_database('test_database')

    def test_connection(self):
        self.assertEqual(self.adapter.db.name, 'test_database')

if __name__ == '__main__':
    unittest.main()