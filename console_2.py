#!/usr/bin/env python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class Console(cmd.Cmd):
    prompt = "(hbnb) "

    __classes = {"BaseModel": BaseModel, "User": User, "Place": Place, "State": State, "City": City, "Amenity": Amenity, "Review": Review}
    def do_EOF(self, line):
        """press ctr-d to exit console"""
        return True

    def do_quit(self, line):
        """type quit to exit console"""
        return True

    def emptyline(self):
        """Empty line"""
        pass

    def do_create(self, line):
        """Creates a new instance of a class"""
        lis = line.split(" ")
        if len(line) == 0:
            print("class name missing")
        elif lis[0] not in self.__classes.keys():
            print("Class name doen't exist")
        else:
            insta = self.__classes[lis[0]]()
            insta.save()
            print(insta.id)

    def do_show(self, line):
        """Show instance with the id"""
        lis = line.split(" ")
        dicti = storage.all()
        if len(line) == 0:
            print("class name missing")
        elif lis[0] not in self.__classes.keys():
            print("Class name doen't exist")
        elif len(lis) == 1:
            print("you did not enter id")
        elif "{}.{}".format(lis[0], lis[1]) not in dicti.keys():
            print("id doesn't exist")
        else:
            obj = dicti["{}.{}".format(lis[0], lis[1])]
            print(obj)

    def do_destroy(self, line):
        """deleting an object created"""
        lis = line.split(" ")
        dicti = storage.all()
        if len(line) == 0:
            print("class name missing")
        elif lis[0] not in self.__classes.keys():
            print("Class name doen't exist")
        elif len(lis) == 1:
            print("you did not enter id")
        elif "{}.{}".format(lis[0], lis[1]) not in dicti.keys():
            print("id doesn't exist")
        else:
            del(dicti["{}.{}".format(lis[0], lis[1])])
            storage.save()

    def do_all(self, line):
        """all instances or of a class"""
        dicti = storage.all()
        lis = []
        lis_2 = line.split(" ")
        if len(line) == 0:
            for key, value in dicti.items():
                lis.append(str(value))
        elif lis_2[0] not in self.__classes.keys():
            print("class doesn't exist")
        else:
            for key, value in dicti.items():
                cls = key.split(".")
                if lis_2[0] == cls[0]:
                    lis.append(str(value))
                else:
                    pass
        print(lis)
        
    def do_update(self, line):
        """To update attributes"""
        lis = line.split(" ")
        dicti = storage.all()
        if len(line) == 0:
            print("class name missing")
        elif lis[0] not in self.__classes.keys():
            print("Class name doen't exist")
        elif len(lis) == 1:
            print("you did not enter id")
        elif "{}.{}".format(lis[0], lis[1]) not in dicti.keys():
            print("id doesn't exist")
        elif len(lis) == 2:
            print("attribute missing")
        elif len(lis) == 3:
            print("attribute value missing")
        else:
            obj = dicti["{}.{}".format(lis[0], lis[1])]
            value = lis[3]





if __name__ == "__main__":
    Console().cmdloop()
