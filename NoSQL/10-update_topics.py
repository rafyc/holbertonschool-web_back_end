#!/usr/bin/env python3
""" pymongo """
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """ inserts a new document in a collection based on kwargs """
    documents = mongo_collection.update(name, topics)
    return documents
