#!/usr/bin/python3
"""Unittests for console.py"""
import unittest
import sys
import os
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO

class TestConsole(unittest.TestCase):
    """Testing the console"""

    @classmethod
    def setUpClass(csl):
        """Resets storage for every test"""
        if os.path.exists('file.json'):
            os.remove('file.json')
            out = StringIO()
            sys.stdout = out
