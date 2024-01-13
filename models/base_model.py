#!/usr/bin/python3

"""Module: Base class module"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """Base class"""
    def __init__(self, *args, **kwargs):
        """
            Args: 
                - *args: list of arguments
                - **kwargs: key word arguments
        """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__[key] = datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            created_at = datetime.now()
            self.created_at = created_at
            self.updated_at = created_at
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    
    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        obj_dict = self.__dict__
        obj_dict['__class__'] = self.__class__.__name__

        if 'created_at' in obj_dict and isinstance(obj_dict['created_at'], datetime):
            obj_dict['created_at'] = obj_dict['created_at'].isoformat()

        if 'updated_at' in obj_dict and isinstance(obj_dict['updated_at'], datetime):
            obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()

        return obj_dict

