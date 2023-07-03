#!/usr/bin/env python3
""" pymongo """
from pymongo import MongoClient


def list_all(mongo_collection):
    """ List all documents """
    documents = mongo_collection.find()
    if not documents:
        return []
    return documents
