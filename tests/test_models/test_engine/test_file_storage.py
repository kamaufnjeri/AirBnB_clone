#!/usr/bin/python3
"""test module"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class Test_file_storage(unittest.TestCase):
    """test class"""
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
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        my_dict = models.storage.all()
        self.assertTrue(type(my_dict) == dict)
        with self.assertRaises(Exception):
            models.storage.new("me")

    def test_new(self):
        bm = BaseModel()
        self.assertTrue(type(bm) == BaseModel)
        models.storage.new(bm)
        self.assertIn("BaseModel.{}".format(bm.id), models.storage.all().keys())
        ur = User()
        self.assertTrue(type(ur) == User)
        models.storage.new(ur)
        self.assertIn("User.{}".format(ur.id), models.storage.all().keys())
        pl = Place()
        self.assertTrue(type(pl) == Place)
        models.storage.new(pl)
        self.assertIn("Place.{}".format(pl.id), models.storage.all().keys())
        st = State()
        self.assertTrue(type(st) == State)
        models.storage.new(st)
        self.assertIn("State.{}".format(st.id), models.storage.all().keys())
        rw = Review()
        self.assertTrue(type(rw) == Review)
        models.storage.new(rw)
        self.assertIn("Review.{}".format(rw.id), models.storage.all().keys())
        ct = City()
        self.assertTrue(type(ct) == City)
        models.storage.new(ct)
        self.assertIn("City.{}".format(ct.id), models.storage.all().keys())
        am = Amenity()
        self.assertTrue(type(am) == Amenity)
        models.storage.new(am)
        self.assertIn("Amenity.{}".format(am.id), models.storage.all().keys())
        with self.assertRaises(Exception):
            models.storage.new("love")
            models.storage.new(None)
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        self.assertTrue(type(models.storage) == FileStorage)
        with self.assertRaises(TypeError):
            models.storage.save(None)

        bm = BaseModel()
        ur = User()
        st = State()
        ct = City()
        pl = Place()
        rw = Review()
        am = Amenity()
        models.storage.new(bm)
        models.storage.new(ur)
        models.storage.new(st)
        models.storage.new(ct)
        models.storage.new(pl)
        models.storage.new(rw)
        models.storage.new(am)
        models.storage.save()
        with open("file.json", "r", encoding="utf-8") as file:
            info = file.read()
            self.assertTrue(type(info) == str)
            self.assertIn("{}.{}".format("BaseModel", bm.id), info)
            self.assertIn("{}.{}".format("User", ur.id), info)
            self.assertIn("{}.{}".format("State", st.id), info)
            self.assertIn("{}.{}".format("City", ct.id), info)
            self.assertIn("{}.{}".format("Place", pl.id), info)
            self.assertIn("{}.{}".format("Review", rw.id), info)
            self.assertIn("{}.{}".format("Amenity", am.id), info)

    def test_reload(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)
        bm = BaseModel()
        ur = User()
        st = State()
        ct = City()
        pl = Place()
        rw = Review()
        am = Amenity()
        models.storage.new(bm)
        models.storage.new(ur)
        models.storage.new(st)
        models.storage.new(ct)
        models.storage.new(pl)
        models.storage.new(rw)
        models.storage.new(am)
        models.storage.save()
        info = FileStorage._FileStorage__objects
        self.assertTrue(type(info) == dict)
        self.assertIn("{}.{}".format("BaseModel", bm.id), info)
        self.assertIn("{}.{}".format("User", ur.id), info)
        self.assertIn("{}.{}".format("State", st.id), info)
        self.assertIn("{}.{}".format("City", ct.id), info)
        self.assertIn("{}.{}".format("Place", pl.id), info)
        self.assertIn("{}.{}".format("Review", rw.id), info)
        self.assertIn("{}.{}".format("Amenity", am.id), info)

