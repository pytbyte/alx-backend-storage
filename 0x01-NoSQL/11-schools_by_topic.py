#!/usr/bin/env python3
'''schools_by_topic module.
'''


def schools_by_topic(mongo_collection, topic):
    """ Returns the list of schools having a specific topic """
    targer_topic = {'topics': {'$elemMatch': {'$eq': topic}}}
    return [doc for doc in mongo_collection.find(targer_topic)]
