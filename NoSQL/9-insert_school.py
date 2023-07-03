#!/usr/bin/env python3
""" pymongo """
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection based on kwargs """
    documents = mongo_collection.document.insert(kwargs)
    return documents
