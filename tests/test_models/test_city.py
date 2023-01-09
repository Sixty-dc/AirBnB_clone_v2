#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """Test for the class city"""

    def __init__(self, *args, **kwargs):
        """init test for the city class"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test for the states_id method"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test for for the test_name method"""
        new = self.value()
        self.assertEqual(type(new.name), str)
