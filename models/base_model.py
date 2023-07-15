#!/usr/bin/python3
"""Base Class for other Classes"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """The Base class"""
    def __init__(self, *args, **kwargs):
        """initializing class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) > 0:
            for key, obj in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(obj)
                elif key != "__class__":
                    self.__dict__[key] = obj
        else:
            models.storage.new(self)

    def __str__(self):
        """string representation of instance of the class"""
        return "[{}] ({}) {}"\
               .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates updated_at with current date"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """create dictionary"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
