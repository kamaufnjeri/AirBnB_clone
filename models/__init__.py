#!/usr/bin/python3
"""
Contains the Storage in storage variable
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
