#!/usr/bin/python3
"""
Testing db storage
"""
import unittest
import os
from models import storage
from models.base_model import BaseModel


class test_dbstorage(unittest. TestCase):
    """
    Testing db storage
    """

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertNotEqual(len(storage.all()), 0)

    def test_all(self):
        """
        test all method
        """
        new = BaseModel()
        holder = storage.all()
        self.assertIsInstance(holder, dict)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        new.save()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))
