#!/usr/bin/python3
"""test module for Amenity class"""
import os
from models import storage
from models.amenity import Amenity
import json
import unittest
from datetime import datetime


class test_insatiation(unittest.TestCase):
    """INstatiation class"""
    def test_class_type(self):
        am = Amenity()
        self.assertTrue(type(am), Amenity)
        self.assertTrue(type(am.id), str)
        self.assertTrue(type(am.created_at), datetime)
        self.assertTrue(type(am.updated_at), datetime)

    def test_updated_at(self):
        am = Amenity()
        am.name = "Florence"
        self.assertLess(am.created_at, am.updated_at)

    def test_id_different(self):
        am = Amenity()
        am2 = Amenity()
        self.assertTrue(am.id != am2.id)

    def test_kwargs(self):
        am = Amenity(id="1234", name="Flo")
        self.assertTrue(am.id == "1234")
        self.assertTrue(am.name == "Flo")
        self.assertTrue(type(am.id) == str)
        self.assertTrue(type(am.name) == str)
        am2 = Amenity(id=222)
        self.assertEqual(type(am2.id), int)

    def test_args(self):
        am = Amenity()
        am.id = "1234"
        am.name = "Flo"
        self.assertTrue(am.id == "1234")
        self.assertTrue(am.name == "Flo")
        self.assertTrue(type(am.id) == str)
        self.assertTrue(type(am.name) == str)
        am2 = Amenity()
        am2.id = 122
        self.assertEqual(type(am2.id), int)

    def test_None(self):
        am = Amenity(id=None)
        self.assertTrue(am.id == None)
        with self.assertRaises(TypeError):
            am = Amenity(created_at=None)


class test_base_model_class(unittest.TestCase):
    """Test the class"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test___str__(self):
        am = Amenity()
        test = am.__str__()
        test2 = "[{}] ({}) {}".format(am.__class__.__name__, am.id, am.__dict__)
        self.assertTrue(test == test2)

    def test_save(self):
        am = Amenity()
        first_update = am.updated_at
        am.save()
        self.assertLess(first_update, am.updated_at)
        am2 = Amenity()
        am2.save()
        self.assertLess(am.updated_at, am2.updated_at)
        second_update = am2.updated_at
        am2.name = "florence"
        am2.save()
        self.assertLess(second_update, am2.updated_at)

    def test_save_file_and_args(self):
        am = Amenity()
        am.save()
        with self.assertRaises(TypeError):
            am.save(None)
        with open("file.json", "r") as f:
            save = f.read()
            self.assertIn("{}.{}".format("Amenity", am.id), save)
    
    def test_to_dict(self):
        am = Amenity()
        dicti = am.to_dict()
        self.assertTrue(type(dicti) == dict)
        self.assertIn('id', dicti.keys())
        self.assertIn('created_at', dicti.keys())
        self.assertIn('updated_at', dicti.keys())
        self.assertIn('__class__', dicti.keys())
        self.assertTrue(type(dicti["__class__"]) == str)
        self.assertTrue(type(dicti["id"]) == str)
        self.assertEqual(type(dicti["created_at"]), str)
        self.assertTrue(type(dicti["updated_at"]) == str)

    def test_to_dict_additional_attributes(self):
        am = Amenity()
        am.id = "1234"
        am.name = "Flo"
        dicti = am.to_dict()
        self.assertIn('id', dicti.keys())
        self.assertIn('name', dicti.keys())
        self.assertTrue(dicti["name"] == "Flo")
        self.assertTrue(dicti["id"] == "1234")
        self.assertTrue(type(dicti["name"]) == str)
        self.assertTrue(type(dicti["id"]) == str)

    def test_to_dict_contrast(self):
        am = Amenity()
        dicti = am.to_dict()
        dic = am.__dict__
        self.assertNotEqual(dicti, dic)

    def test_to_dict_with_args(self):
        with self.assertRaises(TypeError):
            am = Amenity()
            dicti = am.to_dict(None)

if __name__ == "__main__":
    unittest.main()
