#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv

storage_comm = getenv('HBNB_TYPE_STORAGE')


if storage_comm == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage
else:
    storage = FileStorage()
storage.reload()

# Add things for DBStorage here---task 6
