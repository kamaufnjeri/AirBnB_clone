#!/usr/bin/python3
"""test module for Place class"""
import os
from models import storage
from models.place import Place
import json
import unittest
from datetime import datetime


class test_insatiation(unittest.TestCase):
    """INstatiation class"""
    def test_class_type(self):
        pl = Place()
        self.assertTrue(type(pl), Place)
        self.assertTrue(type(pl.id), str)
        self.assertTrue(type(pl.created_at), datetime)
        self.assertTrue(type(pl.updated_at), datetime)

    def test_updated_at(self):
        pl = Place()
        pl.name = "Florence"
        self.assertLess(pl.created_at, pl.updated_at)

    def test_id_different(self):
        pl = Place()
        pl2 = Place()
        self.assertTrue(pl.id != pl2.id)

    def test_kwargs(self):
        pl = Place(id="1234", name="Flo")
        self.assertTrue(pl.id == "1234")
        self.assertTrue(pl.name == "Flo")
        self.assertTrue(type(pl.id) == str)
        self.assertTrue(type(pl.name) == str)
        pl2 = Place(id=222)
        self.assertEqual(type(pl2.id), int)

    def test_args(self):
        pl = Place()
        pl.id = "1234"
        pl.name = "Flo"
        self.assertTrue(pl.id == "1234")
        self.assertTrue(pl.name == "Flo")
        self.assertTrue(type(pl.id) == str)
        self.assertTrue(type(pl.name) == str)
        pl2 = Place()
        pl2.id = 122
        self.assertEqual(type(pl2.id), int)

    def test_None(self):
        pl = Place(id=None)
        self.assertTrue(pl.id == None)
        with self.assertRaises(TypeError):
            pl = Place(created_at=None)


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
        pl = Place()
        test = pl.__str__()
        test2 = "[{}] ({}) {}".format(pl.__class__.__name__, pl.id, pl.__dict__)
        self.assertTrue(test == test2)

    def test_save(self):
        pl = Place()
        first_update = pl.updated_at
        pl.save()
        self.assertLess(first_update, pl.updated_at)
        pl2 = Place()
        pl2.save()
        self.assertLess(pl.updated_at, pl2.updated_at)
        second_update = pl2.updated_at
        pl2.name = "florence"
        pl2.save()
        self.assertLess(second_update, pl2.updated_at)

    def test_save_file_and_args(self):
        pl = Place()
        pl.save()
        with self.assertRaises(TypeError):
            pl.save(None)
        with open("file.json", "r") as f:
            save = f.read()
            self.assertIn("{}.{}".format("Place", pl.id), save)
    
    def test_to_dict(self):
        pl = Place()
        dicti = pl.to_dict()
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
        pl = Place()
        pl.id = "1234"
        pl.name = "Flo"
        dicti = pl.to_dict()
        self.assertIn('id', dicti.keys())
        self.assertIn('name', dicti.keys())
        self.assertTrue(dicti["name"] == "Flo")
        self.assertTrue(dicti["id"] == "1234")
        self.assertTrue(type(dicti["name"]) == str)
        self.assertTrue(type(dicti["id"]) == str)

    def test_to_dict_contrast(self):
        pl = Place()
        dicti = pl.to_dict()
        dic = pl.__dict__
        self.assertNotEqual(dicti, dic)

    def test_to_dict_with_args(self):
        with self.assertRaises(TypeError):
            pl = Place()
            dicti = pl.to_dict(None)

if __name__ == "__main__":
    unittest.main()
