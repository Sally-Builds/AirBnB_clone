#!/usr/bin/python3

"""Module: Base class module"""

import uuid
from datetime import datetime

class BaseModel:
    """Base class"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        created_at = datetime.now()
        self.created_at = created_at
        self.updated_at = created_at

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__
        obj_dict['__class__'] = self.__class__.__name__

        if 'created_at' in obj_dict and isinstance(obj_dict['created_at'], datetime):
            obj_dict['created_at'] = obj_dict['created_at'].isoformat()

        if 'updated_at' in obj_dict and isinstance(obj_dict['updated_at'], datetime):
            obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()

        return obj_dict

my_model = BaseModel()
my_model.age = 89
print(my_model)
print("--------------")
print(my_model.to_dict())
