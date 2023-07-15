#!/usr/bin/python3
"""File storage for instances of a class created"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Class created"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return all objs created from a class"""
        return self.__objects

    def new(self, obj):
        """Add a new instance of a class to _-objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serialization"""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """from json string to python objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                dicti = json.load(file)
            for val in dicti.values():
                clsnm = eval(val["__class__"])
                obj = clsnm(**val)
                self.new(obj)
        except FileNotFoundError:
            pass
