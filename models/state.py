#!/usr/bin/python3
"""
    state module
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
        State class for User object
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
            initializes the instance of an object
        """
        super().__init__(*args, **kwargs)
