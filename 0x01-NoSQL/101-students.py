#!/usr/bin/env python3
"""
This code, returns all students sorted by score
Prototype:
	def top_students(mongo_collection):
	 mongo_collection will be the pymongo
	collection object
"""


def top_students(mongo_collection):
    """ students sorted by score """
    return mongo_collection.aggregate([
        {
            '$project': {
                'name': '$name',
                'averageScore': {
                    '$avg': "$topics.score"
                }
            }
        },
        {
            '$sort': {
                "averageScore": -1
            }
        }
    ])
