# Importing all the required modules
import json
from pymongo import *

class MongoDB:

    """ This is class dedicated to establish MongoDB Atlas Connection, feeding data into it as well
     accessing them. """

    def __init__(self):
        file = open(".\\mongoDB\\info.json")
        js = json.load(file)
        self.client = MongoClient(js['MongoDBContents'][0]['Connection String'])

        self.db = self.client['test']
        # post = self.db.entities
        print("MongoDB Database Connection established...")

    def addData(self, filename, name, doctor, phone, date, address, rupees,
                invoice, gst, org, med, medCond, pathogens, fraudColor):

        entry = {"filename": filename, "name": name, "doctor": doctor, "phone": phone, "date": date,
                 "address":address, "rupees": rupees, "invoice": invoice, "gst": gst, "org": org,
                 "med": med, "medCond": medCond, "pathogens": pathogens, "fraudColor": fraudColor}

        post = self.db.entities
        id = post.insert_one(entry)

        print("Successfully added data to test.entities...")
        return id

    def getData(self):
        # Getting the filename & path from web
        post = self.db.files
        # return post.find()
        # return post.find({}).sort({'_id':-1}).limit(1)

        # Define the field to sort by and the sorting order (descending)
        sort_field = "createdAt"  # Replace with the actual field name
        sorting_order = DESCENDING

        # Use find_one with sort to get the latest record
        latest_record = post.find_one(sort = [(sort_field, sorting_order)])

        print("Successfully retrieved data from test.files...")
        return latest_record

    def __call__(self, *args, **kwargs):
        pass

    def __del__(self):
        # self.client.close()
        print("MongoDB database connection lost...")


