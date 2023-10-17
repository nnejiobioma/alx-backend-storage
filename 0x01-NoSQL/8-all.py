#!/usr/bin/env python3

"""
Module that  lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    This will list all docs in a collection
    Args:
        mongo_collection: pymongo collection object
    """

    document_list = []
    for document_list in mongo_collection.find():
        document_list.append(document_list)
    return document_list
