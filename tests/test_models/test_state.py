#!/usr/bin/python3
"""test module for State class"""
import os
from models import storage
from models.state import State
import json
import unittest
from datetime import datetime


class test_insatiation(unittest.TestCase):
    """INstatiation class"""
    def test_class_attr_type(self):
        self.assertTrue(type(State.name) == str)

    def test_class_type(self):
        st = State()
        self.assertTrue(type(st) == State)
        self.assertTrue(type(st.id) == str)
        self.assertTrue(type(st.created_at) == datetime)
        self.assertTrue(type(st.updated_at) == datetime)

    def test_updated_at(self):
        st = State()
        st.name = "Florence"
        self.assertLess(st.created_at, st.updated_at)

    def test_id_different(self):
        st = State()
        st2 = State()
        self.assertTrue(st.id != st2.id)

    def test_kwargs(self):
        st = State(id="1234", name="Flo")
        self.assertTrue(st.id == "1234")
        self.assertTrue(st.name == "Flo")
        self.assertTrue(type(st.id) == str)
        self.assertTrue(type(st.name) == str)
        st2 = State(id=222)
        self.assertEqual(type(st2.id), int)

    def test_args(self):
        st = State()
        st.id = "1234"
        st.name = "Flo"
        self.assertTrue(st.id == "1234")
        self.assertTrue(st.name == "Flo")
        self.assertTrue(type(st.id) == str)
        self.assertTrue(type(st.name) == str)
        st2 = State()
        st2.id = 122
        self.assertEqual(type(st2.id), int)

    def test_None(self):
        st = State(id=None)
        self.assertTrue(st.id is None)
        with self.assertRaises(TypeError):
            st = State(created_at=None)


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
        st = State()
        test = st.__str__()
        test2 = "[{}] ({}) {}".format(st.__class__.__name__,
                                      st.id, st.__dict__)
        self.assertTrue(test == test2)

    def test_save(self):
        st = State()
        first_update = st.updated_at
        st.save()
        self.assertLess(first_update, st.updated_at)
        st2 = State()
        st2.save()
        self.assertLess(st.updated_at, st2.updated_at)
        second_update = st2.updated_at
        st2.name = "florence"
        st2.save()
        self.assertLess(second_update, st2.updated_at)

    def test_save_file_and_args(self):
        st = State()
        st.save()
        with self.assertRaises(TypeError):
            st.save(None)
        with open("file.json", "r") as f:
            save = f.read()
            self.assertIn("{}.{}".format("State", st.id), save)

    def test_to_dict(self):
        st = State()
        dicti = st.to_dict()
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
        st = State()
        st.id = "1234"
        st.name = "Flo"
        dicti = st.to_dict()
        self.assertIn('id', dicti.keys())
        self.assertIn('name', dicti.keys())
        self.assertTrue(dicti["name"] == "Flo")
        self.assertTrue(dicti["id"] == "1234")
        self.assertTrue(type(dicti["name"]) == str)
        self.assertTrue(type(dicti["id"]) == str)

    def test_to_dict_contrast(self):
        st = State()
        dicti = st.to_dict()
        dic = st.__dict__
        self.assertNotEqual(dicti, dic)

    def test_to_dict_with_args(self):
        with self.assertRaises(TypeError):
            st = State()
            dicti = st.to_dict(None)


if __name__ == "__main__":
    unittest.main()
