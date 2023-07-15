#!/usr/bin/python3
"""test module for User class"""
import os
from models import storage
from models.user import User
import json
import unittest
from datetime import datetime


class test_insatiation(unittest.TestCase):
    """INstatiation class"""
    def test_class_type(self):
        ur = User()
        self.assertTrue(type(ur), User)
        self.assertTrue(type(ur.id), str)
        self.assertTrue(type(ur.created_at), datetime)
        self.assertTrue(type(ur.updated_at), datetime)

    def test_updated_at(self):
        ur = User()
        ur.name = "Florence"
        self.assertLess(ur.created_at, ur.updated_at)

    def test_id_different(self):
        ur = User()
        ur2 = User()
        self.assertTrue(ur.id != ur2.id)

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_kwargs(self):
        ur = User(id="1234", name="Flo")
        self.assertTrue(ur.id == "1234")
        self.assertTrue(ur.name == "Flo")
        self.assertTrue(type(ur.id) == str)
        self.assertTrue(type(ur.name) == str)
        ur2 = User(id=222)
        self.assertEqual(type(ur2.id), int)

    def test_args(self):
        ur = User()
        ur.id = "1234"
        ur.name = "Flo"
        self.assertTrue(ur.id == "1234")
        self.assertTrue(ur.name == "Flo")
        self.assertTrue(type(ur.id) == str)
        self.assertTrue(type(ur.name) == str)
        ur2 = User()
        ur2.id = 122
        self.assertEqual(type(ur2.id), int)

    def test_None(self):
        ur = User(id=None)
        self.assertTrue(ur.id is None)
        with self.assertRaises(TypeError):
            ur = User(created_at=None)


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
        ur = User()
        test = ur.__str__()
        test2 = "[{}] ({}) {}".format(ur.__class__.__name__,
                                      ur.id, ur.__dict__)
        self.assertTrue(test == test2)

    def test_save(self):
        ur = User()
        first_update = ur.updated_at
        ur.save()
        self.assertLess(first_update, ur.updated_at)
        ur2 = User()
        ur2.save()
        self.assertLess(ur.updated_at, ur2.updated_at)
        second_update = ur2.updated_at
        ur2.name = "florence"
        ur2.save()
        self.assertLess(second_update, ur2.updated_at)

    def test_save_file_and_args(self):
        ur = User()
        ur.save()
        with self.assertRaises(TypeError):
            ur.save(None)
        with open("file.json", "r") as f:
            save = f.read()
            self.assertIn("{}.{}".format("User", ur.id), save)

    def test_to_dict(self):
        ur = User()
        dicti = ur.to_dict()
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
        ur = User()
        ur.id = "1234"
        ur.name = "Flo"
        dicti = ur.to_dict()
        self.assertIn('id', dicti.keys())
        self.assertIn('name', dicti.keys())
        self.assertTrue(dicti["name"] == "Flo")
        self.assertTrue(dicti["id"] == "1234")
        self.assertTrue(type(dicti["name"]) == str)
        self.assertTrue(type(dicti["id"]) == str)

    def test_to_dict_contrast(self):
        ur = User()
        dicti = ur.to_dict()
        dic = ur.__dict__
        self.assertNotEqual(dicti, dic)

    def test_to_dict_with_args(self):
        with self.assertRaises(TypeError):
            ur = User()
            dicti = ur.to_dict(None)


if __name__ == "__main__":
    unittest.main()
