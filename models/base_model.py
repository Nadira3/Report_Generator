#!/usr/bin/python3
"""
    basemodel module
"""

import datetime
import uuid
import models
from prettytable import PrettyTable

def tabulate(object_dict):
    objTab = PrettyTable()

    column = ["index", "attr", "value"]
    objTab._max_width = {"value" : 50}
    col = [data for data in object_dict.keys()]
    val = [data if not isinstance(data, dict) else "" for data in object_dict.values()]
    
    objTab.add_column(column[0], [d for d in range(len(col))])
    objTab.add_column(column[1], [d for d in col])
    objTab.add_column(column[2], [d for d in val])

    return objTab

class BaseModel:
    """
        base class for all other classes
    """

    def __init__(self, *args, **kwargs):
        """
            initializes the instance of an object
        """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.datetime.fromisoformat(value)
                elif key != "__class__":
                    self.__dict__[key] = value

    def __str__(self):
        """
            prints an object instance attributes
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
            saves an object instance attributes
            and updates its time
        """

        self.updated_at = datetime.datetime.now()
        o_key = self.__class__.__name__ + "." + self.id
        obj_dict = models.storage.all()
        for key in obj_dict.keys():
            if key == o_key:
                obj_dict[key].update(self.to_dict())
        models.storage.save()

    def to_dict(self):
        """
            returns an object instance dict
        """
        object_dict = {}
        for key, value in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                object_dict[key] = datetime.datetime.isoformat(value)
            else:
                object_dict[key] = value
        object_dict["__class__"] = self.__class__.__name__
        return object_dict

    def to_table(self):
        object_dict = self.to_dict()
        objTab = tabulate(object_dict)
        return objTab
