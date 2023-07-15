import json


cls = BaseModel()
val = [cls name] (id) dict
val.to_dict()

print(cls)
__objects = {}
def all(self):
    return self.__objects
def new(self, obj):
    key = "{}.{}".format(obj.___class__.__name__, obj.id) key = BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2
    self.__objects[key] = obj 
def save(self):
    dicti = {}
    for key, value in self.__objects.items():
	    dicti[key] = value.to_dict()

    with open(self.__file_path, "w", encoding="utf-8") as f:
	    json.dump(dicti, f)

def reload(self):
    try:
        with open(self.__file_path, 'r', encoding='utf-8') as file:
            dicti = json.load(file)
            for val in dicti.values():                
                clsnm = eval(val["__class__"])
                obj = clsnm(**val) 
                self.new(obj)
    except FileNotFoundError:
        pass


    [BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301), 'name': 'My_First_Model', 'my_number': 89}
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'my_number': 89

        {"BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2": {"__class__": "BaseModel", "id": "e79e744a-55d4-45a3-b74a-ca5fae74e0e2", "updated_at": "2017-09-28T21:08:06.151750", "created_at": "2017-09-28T21:08:06.151711", "name": "My_First_Model", "my_number": 89}, "BaseModel.080cce84-c574-4230-b82a-9acb74ad5e8c": {"__class__": "BaseModel", "id": "080cce84-c574-4230-b82a-9acb74ad5e8c", "updated_at": "2017-09-28T21:07:51.973308", "created_at": "2017-09-28T21:07:51.973301", "name": "My_First_Model", "my_number": 89}, "BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"__class__": "BaseModel", "id": "ee49c413-023a-4b49-bd28-f2936c95460d", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "my_number": 89}}
