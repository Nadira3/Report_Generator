#!/usr/bin/python3
""" This module contains storage file initialization """

from models import base_model, history, complaint, patient, review, utils
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
