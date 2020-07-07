#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This file handles Databaseconnections.
"""

import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId


class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Mongo_Connection(metaclass=Singleton):

    """Represents the Database connection and offers
    the necessary steps to save the desired data


    Attributes:
        client (obj): MongoClient
        collection (obj): Collection in MongoDB
    """

    def __init__(self, mongo_ip, mongo_host, db_name):
        """Initiates connection to MongoDB

        Args:
            mongo_ip (str): IP-Address of MongoDB
            mongo_host (str): Host of MongoDB
            db_name (str): Name of Database in MongoDB
            db_name (str): Name of Collection in MongoDB
        """
        self.client = MongoClient(mongo_ip, int(mongo_host))
        self.collection_car = self.client[db_name]['cars']
        self.collection_person = self.client[db_name]['person']

    def save_person(self, person):
        """Sample Function for saving a person

        Args:
            person (json_tag): represents a person

        Returns:
            [ObjectId]: the object_id of the saved person in mongodb
        """        
        return self.collection_person.insert_one(person).inserted_id
