#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Test for the review class"""

    def __init__(self, *args, **kwargs):
        """init test for the review class"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test for the place_id"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Test for the place id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Test for the text"""
        new = self.value()
        self.assertEqual(type(new.text), str)
