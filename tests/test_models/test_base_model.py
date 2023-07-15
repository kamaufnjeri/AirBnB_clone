#!/usr/bin/python3
"""test module for BaseModel class"""
import os
from models import storage
from models.base_model import BaseModel
import json
import unittest
from datetime import datetime


class test_insatiation(unittest.TestCase):
    """INstatiation class"""
    def test_class_type(self):
        bm = BaseModel()
        self.assertTrue(type(bm), BaseModel)
        self.assertTrue(type(bm.id), str)
        self.assertTrue(type(bm.created_at), datetime)
        self.assertTrue(type(bm.updated_at), datetime)

    def test_updated_at(self):
        bm = BaseModel()
        bm.name = "Florence"
        self.assertLess(bm.created_at, bm.updated_at)

    def test_id_different(self):
        bm = BaseModel()
        bm2 = BaseModel()
        self.assertTrue(bm.id != bm2.id)

    def test_kwargs(self):
        bm = BaseModel(id="1234", name="Flo")
        self.assertTrue(bm.id == "1234")
        self.assertTrue(bm.name == "Flo")
        self.assertTrue(type(bm.id) == str)
        self.assertTrue(type(bm.name) == str)
        bm2 = BaseModel(id=222)
        self.assertEqual(type(bm2.id), int)

    def test_args(self):
        bm = BaseModel()
        bm.id = "1234"
        bm.name = "Flo"
        self.assertTrue(bm.id == "1234")
        self.assertTrue(bm.name == "Flo")
        self.assertTrue(type(bm.id) == str)
        self.assertTrue(type(bm.name) == str)
        bm2 = BaseModel()
        bm2.id = 122
        self.assertEqual(type(bm2.id), int)

    def test_None(self):
        bm = BaseModel(id=None)
        self.assertTrue(bm.id == None)
        with self.assertRaises(TypeError):
            bm = BaseModel(created_at=None)


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
        bm = BaseModel()
        test = bm.__str__()
        test2 = "[{}] ({}) {}".format(bm.__class__.__name__, bm.id, bm.__dict__)
        self.assertTrue(test == test2)

    def test_save(self):
        bm = BaseModel()
        first_update = bm.updated_at
        bm.save()
        self.assertLess(first_update, bm.updated_at)
        bm2 = BaseModel()
        bm2.save()
        self.assertLess(bm.updated_at, bm2.updated_at)
        second_update = bm2.updated_at
        bm2.name = "florence"
        bm2.save()
        self.assertLess(second_update, bm2.updated_at)

    def test_save_file_and_args(self):
        bm = BaseModel()
        bm.save()
        with self.assertRaises(TypeError):
            bm.save(None)
        with open("file.json", "r") as f:
            save = f.read()
            self.assertIn("{}.{}".format("BaseModel", bm.id), save)
    
    def test_to_dict(self):
        bm = BaseModel()
        dicti = bm.to_dict()
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
        bm = BaseModel()
        bm.id = "1234"
        bm.name = "Flo"
        dicti = bm.to_dict()
        self.assertIn('id', dicti.keys())
        self.assertIn('name', dicti.keys())
        self.assertTrue(dicti["name"] == "Flo")
        self.assertTrue(dicti["id"] == "1234")
        self.assertTrue(type(dicti["name"]) == str)
        self.assertTrue(type(dicti["id"]) == str)

    def test_to_dict_contrast(self):
        bm = BaseModel()
        dicti = bm.to_dict()
        dic = bm.__dict__
        self.assertNotEqual(dicti, dic)

    def test_to_dict_with_args(self):
        with self.assertRaises(TypeError):
            bm = BaseModel()
            dicti = bm.to_dict(None)

if __name__ == "__main__":
    unittest.main()
