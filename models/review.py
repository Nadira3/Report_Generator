#!/usr/bin/python3
"""
    review module
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
        Review class for other classes
    """

    patient_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
            initializes the instance of an object
        """
        super().__init__(*args, **kwargs)
