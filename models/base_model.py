#!/usr/bin/python3
"""
    basemodel module
"""

import datetime
import uuid
import models


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
