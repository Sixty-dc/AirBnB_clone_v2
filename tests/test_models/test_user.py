#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """Test class for the User class"""

    def __init__(self, *args, **kwargs):
        """init for the test class of the user class"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Test for the first_name"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test for the last_name"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Test for the user email"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Test for the user password"""
        new = self.value()
        self.assertEqual(type(new.password), str)
