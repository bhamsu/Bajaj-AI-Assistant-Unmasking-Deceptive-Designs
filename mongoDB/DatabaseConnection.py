# Importing all the required modules
from pymongo import *

class MongoDB:

    """ This is class dedicated to establish MongoDB Atlas Connection, feeding data into it as well
     accessing them. """

    def __init__(self, connectionString):
        self.client = MongoClient(connectionString)
        self.db = self.client['sample-database']

    def __call__(self, *args, **kwargs):
        post = self.db.class11
        print(post.find_one({'roll': 64}))

    def __del__(self):
        pass
