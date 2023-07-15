#!/usr/bin/python3
"""test module for Review class"""
import os
from models import storage
from models.review import Review
import json
import unittest
from datetime import datetime


class test_insatiation(unittest.TestCase):
    """INstatiation class"""
    def test_class_attt(self):
        self.assertTrue(type(Review.place_id) == str)
        self.assertTrue(type(Review.user_id) == str)
        self.assertTrue(type(Review.text) == str)

    def test_class_type(self):
        rw = Review()
        self.assertTrue(type(rw) == Review)
        self.assertTrue(type(rw.id) == str)
        self.assertTrue(type(rw.created_at) == datetime)
        self.assertTrue(type(rw.updated_at) == datetime)

    def test_updated_at(self):
        rw = Review()
        rw.name = "Florence"
        self.assertLess(rw.created_at, rw.updated_at)

    def test_id_different(self):
        rw = Review()
        rw2 = Review()
        self.assertTrue(rw.id != rw2.id)

    def test_kwargs(self):
        rw = Review(id="1234", name="Flo")
        self.assertTrue(rw.id == "1234")
        self.assertTrue(rw.name == "Flo")
        self.assertTrue(type(rw.id) == str)
        self.assertTrue(type(rw.name) == str)
        rw2 = Review(id=222)
        self.assertEqual(type(rw2.id), int)

    def test_args(self):
        rw = Review()
        rw.id = "1234"
        rw.name = "Flo"
        self.assertTrue(rw.id == "1234")
        self.assertTrue(rw.name == "Flo")
        self.assertTrue(type(rw.id) == str)
        self.assertTrue(type(rw.name) == str)
        rw2 = Review()
        rw2.id = 122
        self.assertEqual(type(rw2.id), int)

    def test_None(self):
        rw = Review(id=None)
        self.assertTrue(rw.id is None)
        with self.assertRaises(TypeError):
            rw = Review(created_at=None)


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
        rw = Review()
        test = rw.__str__()
        test2 = "[{}] ({}) {}".format(rw.__class__.__name__,
                                      rw.id, rw.__dict__)
        self.assertTrue(test == test2)

    def test_save(self):
        rw = Review()
        first_update = rw.updated_at
        rw.save()
        self.assertLess(first_update, rw.updated_at)
        rw2 = Review()
        rw2.save()
        self.assertLess(rw.updated_at, rw2.updated_at)
        second_update = rw2.updated_at
        rw2.name = "florence"
        rw2.save()
        self.assertLess(second_update, rw2.updated_at)

    def test_save_file_and_args(self):
        rw = Review()
        rw.save()
        with self.assertRaises(TypeError):
            rw.save(None)
        with open("file.json", "r") as f:
            save = f.read()
            self.assertIn("{}.{}".format("Review", rw.id), save)

    def test_to_dict(self):
        rw = Review()
        dicti = rw.to_dict()
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
        rw = Review()
        rw.id = "1234"
        rw.name = "Flo"
        dicti = rw.to_dict()
        self.assertIn('id', dicti.keys())
        self.assertIn('name', dicti.keys())
        self.assertTrue(dicti["name"] == "Flo")
        self.assertTrue(dicti["id"] == "1234")
        self.assertTrue(type(dicti["name"]) == str)
        self.assertTrue(type(dicti["id"]) == str)

    def test_to_dict_contrast(self):
        rw = Review()
        dicti = rw.to_dict()
        dic = rw.__dict__
        self.assertNotEqual(dicti, dic)

    def test_to_dict_with_args(self):
        with self.assertRaises(TypeError):
            rw = Review()
            dicti = rw.to_dict(None)


if __name__ == "__main__":
    unittest.main()
