#!/usr/bin/python3
''' Test FileStorage '''

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        os.remove('file.json')
        self.storage._FileStorage__objects = {}
        del self.storage

    def test_init(self):
        self.assertEqual(self.storage._FileStorage__file_path, 'file.json')
        self.assertEqual(self.storage._FileStorage__objects, {})

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        o = BaseModel()
        self.storage.new(o)
        key = o.__class__.__name__ + '.' + o.id
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_save_reload(self):
        o1 = BaseModel()
        o2 = User()
        o3 = State()
        self.storage.new(o1)
        self.storage.new(o2)
        self.storage.new(o3)
        self.storage.save()

        storage_new = FileStorage()
        storage_new.reload()
        self.assertEqual(len(storage_new.all()), 3)

    def test_save_json_format(self):
        o = BaseModel()
        self.storage.new(o)
        self.storage.save()

        with open(self.storage._FileStorage__file_path, 'r') as file:
            data = json.load(file)
            self.assertIn(o.__class__.__name__ + '.' + o.id, data)
            self.assertIn('__class__',
                          data[o.__class__.__name__ + '.' + o.id])
            self.assertIn('created_at',
                          data[o.__class__.__name__ + '.' + o.id])
            self.assertIn('updated_at',
                          data[o.__class__.__name__ + '.' + o.id])


if __name__ == "__main__":
    unittest.main()
