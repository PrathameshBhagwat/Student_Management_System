from pymongo import MongoClient

connection = MongoClient("mongodb+srv://bhagvatprathu_db_user:qc10hnPK1Nb8Ugp0@cluster0.sbar8o1.mongodb.net/?appName=Cluster0")
database = connection["StudentManagementDB"]
collection = database["students"]
