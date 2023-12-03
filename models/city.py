#!/usr/bin/python3
"""
    city module
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
        City class for User object
    """

    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """ initializes an object instance """

        super().__init__(*args, **kwargs)
