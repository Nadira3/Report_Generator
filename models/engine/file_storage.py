#!/usr/bin/python3
"""
    filestorage module with class that
    serializes instances to a JSON file
    and deserializes JSON file to instances
"""

import json


class FileStorage:
    """
        serializes instances to a JSON file
        and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            returns a list of all created objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
            adds a new object to the savwd list
        """
        FileStorage.__objects[
                obj.__class__.__name__ + "." + obj.id] = obj.to_dict()

    def save(self):
        """
            saves the updated object to a storage file
        """
        with open(FileStorage.__file_path, "w+", encoding="utf-8") as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """
            saves all the saved objects from a storage file
        """
        try:
            with open(FileStorage.__file_path, "r+", encoding="utf-8") as file:
                FileStorage.__objects = json.load(file)
                return FileStorage.__objects
        except FileNotFoundError:
            pass
