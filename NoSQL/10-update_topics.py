#!/usr/bin/env python3
""" pymongo """
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """ Change school topics """
    query = {"name": name}
    update = {"$set":{"topics":topics}}
    mongo_collection.updateMany(query, update)
