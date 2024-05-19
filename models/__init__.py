#!/usr/bin/python3
"""
This is the __init__.py file
"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
