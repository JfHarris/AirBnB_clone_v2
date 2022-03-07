#!/usr/bin/python3
"""Unittests for console.py"""
import unittest
import sys
import os
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import inspect
import console


class TestConsole(unittest.TestCase):
    """Testing the console"""

    @classmethod
    def setUpClass(csl):
        """Resets storage for every test"""
        if os.path.exists('file.json'):
            os.remove('file.json')
            out = StringIO()
            sys.stdout = out

    def test_docstring_Con(self):
        """testing if docstring exists"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")
