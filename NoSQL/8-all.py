#!/usr/bin/env python3
"""
Python 3 Module, using Mongodb.
"""


def list_all(mongo_collection):
    """
    lists all documents in a collection:
    """
    return list(mongo_collection.find())
