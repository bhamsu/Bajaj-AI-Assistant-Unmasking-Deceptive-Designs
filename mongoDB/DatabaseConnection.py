# Importing all the required modules
import json
from pymongo import *

class MongoDB:

    """ This is class dedicated to establish MongoDB Atlas Connection, feeding data into it as well
     accessing them. """

    def __init__(self):
        file = open("info.json")
        js = json.load(file)
        self.client = MongoClient(js['MongoDBContents'][0]['Connection String'])

        self.db = self.client['test']
        # post = self.db.entities

    def addData(self, name, doctor, phone, date, address, rupees,
                invoice, gst, org, med, medCond, pathogens, fraudColor):

        entry = {"id": 2, "name": name, "doctor": doctor, "phone": phone, "date": date,
                 "address":address, "rupees": rupees, "invoice": invoice, "gst": gst, "org": org,
                 "med": med, "medCond": medCond, "pathogens": pathogens, "fraudColor": fraudColor}

        post = self.db.entities
        id = post.insert_one(entry)

        return id

    def __call__(self, *args, **kwargs):
        pass

    def __del__(self):
        pass



# mn = MongoDB()


