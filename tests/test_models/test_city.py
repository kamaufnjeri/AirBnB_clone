#!/usr/bin/python3
"""test module for City class"""
import os
from models import storage
from models.city import City
import json
import unittest
from datetime import datetime


class test_insatiation(unittest.TestCase):
    """INstatiation class"""
    def test_class_type(self):
        ct = City()
        self.assertTrue(type(ct), City)
        self.assertTrue(type(ct.id), str)
        self.assertTrue(type(ct.created_at), datetime)
        self.assertTrue(type(ct.updated_at), datetime)

    def test_updated_at(self):
        ct = City()
        ct.name = "Florence"
        self.assertLess(ct.created_at, ct.updated_at)

    def test_id_different(self):
        ct = City()
        ct2 = City()
        self.assertTrue(ct.id != ct2.id)

    def test_kwargs(self):
        ct = City(id="1234", name="Flo")
        self.assertTrue(ct.id == "1234")
        self.assertTrue(ct.name == "Flo")
        self.assertTrue(type(ct.id) == str)
        self.assertTrue(type(ct.name) == str)
        ct2 = City(id=222)
        self.assertEqual(type(ct2.id), int)

    def test_args(self):
        ct = City()
        ct.id = "1234"
        ct.name = "Flo"
        self.assertTrue(ct.id == "1234")
        self.assertTrue(ct.name == "Flo")
        self.assertTrue(type(ct.id) == str)
        self.assertTrue(type(ct.name) == str)
        ct2 = City()
        ct2.id = 122
        self.assertEqual(type(ct2.id), int)

    def test_None(self):
        ct = City(id=None)
        self.assertTrue(ct.id == None)
        with self.assertRaises(TypeError):
            ct = City(created_at=None)


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
        ct = City()
        test = ct.__str__()
        test2 = "[{}] ({}) {}".format(ct.__class__.__name__, ct.id, ct.__dict__)
        self.assertTrue(test == test2)

    def test_save(self):
        ct = City()
        first_update = ct.updated_at
        ct.save()
        self.assertLess(first_update, ct.updated_at)
        ct2 = City()
        ct2.save()
        self.assertLess(ct.updated_at, ct2.updated_at)
        second_update = ct2.updated_at
        ct2.name = "florence"
        ct2.save()
        self.assertLess(second_update, ct2.updated_at)

    def test_save_file_and_args(self):
        ct = City()
        ct.save()
        with self.assertRaises(TypeError):
            ct.save(None)
        with open("file.json", "r") as f:
            save = f.read()
            self.assertIn("{}.{}".format("City", ct.id), save)
    
    def test_to_dict(self):
        ct = City()
        dicti = ct.to_dict()
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
        ct = City()
        ct.id = "1234"
        ct.name = "Flo"
        dicti = ct.to_dict()
        self.assertIn('id', dicti.keys())
        self.assertIn('name', dicti.keys())
        self.assertTrue(dicti["name"] == "Flo")
        self.assertTrue(dicti["id"] == "1234")
        self.assertTrue(type(dicti["name"]) == str)
        self.assertTrue(type(dicti["id"]) == str)

    def test_to_dict_contrast(self):
        ct = City()
        dicti = ct.to_dict()
        dic = ct.__dict__
        self.assertNotEqual(dicti, dic)

    def test_to_dict_with_args(self):
        with self.assertRaises(TypeError):
            ct = City()
            dicti = ct.to_dict(None)

if __name__ == "__main__":
    unittest.main()
