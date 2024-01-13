#!/usr/bin/python3

"""File Storage """

import json
import os

class FileStorage:
    """ """
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """ """
        return FileStorage.__objects

    def new(self, obj):
        """ """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ """
        with open(FileStorage.__file_path, 'w') as file:
            data = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
            json.dump(data, file, indent=2)

    def reload(self):
        """ """
        from models.base_model import BaseModel
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                data = json.load(file)
                FileStorage.__objects = {k: BaseModel(**v) for k, v in data.items()}

