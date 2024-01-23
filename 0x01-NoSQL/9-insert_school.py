#!/usr/bin/env python3
""" insert_into_mongo """


def insert_school(mongo_collection, **kwargs):
    """ Inserting a new document in a mongo school collection """
    new_entry = mongo_collection.insert_one(kwargs)
    return new_entry.inserted_id
