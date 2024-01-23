#!/usr/bin/env python3
""" list_from_mongo """


def list_all(mongo_collection):
    """ Listing all documents in a mongo collection """
    all_docs = mongo_collection.find()
    return list(all_docs)
