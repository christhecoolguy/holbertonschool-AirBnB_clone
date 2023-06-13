#!/usr/bin/python3
""" unit test for review """

import unittest
import os 
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.review import review


myreview = Review()

class TestReview(unittest.TestCase):
    """ Class for Review tests """

    def test_id(self):
        """ Unittesting test_id instance """
        self.assertTrue(isinstance(myreview.id, str))

    def test_place_id(self):
        """ Make sure place_id is string """
        self.assertTrue(isinstance(Review.place_id, str))
        self.assertTrue(isinstance(myreview.place_id, str))

    def test_user_id(self):
        """ Make sure user_id is string """
        self.assertTrue(isinstance(Review.user_id, str))
        self.assertTrue(isinstance(myreview.user_id, str))

    def test_text(self):
        """ Make sure text is string """
        self.assertTrue(isinstance(Review.text, str))
        self.assertTrue(isinstance(myreview.text, str))
