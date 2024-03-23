#!/usr/bin/python3
''' Test BaseModel '''

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

        model = BaseModel(id='1',
                          created_at='2024-01-01T00:00:00',
                          updated_at='2024-01-02T00:00:00')
        self.assertEqual(model.id, '1')
        self.assertEqual(model.created_at,
                         datetime.fromisoformat('2024-01-01T00:00:00'))
        self.assertEqual(model.updated_at,
                         datetime.fromisoformat('2024-01-02T00:00:00'))

    def test_save(self):
        model = BaseModel()
        updated_at_old = model.updated_at
        model.save()
        self.assertNotEqual(updated_at_old, model.updated_at)
        self.assertGreater(model.updated_at, updated_at_old)

    def test_to_dict(self):
        model = BaseModel(id='1',
                          created_at='2024-01-01T00:00:00',
                          updated_at='2024-01-02T00:00:00')
        expected = {
                'id': '1',
                '__class__': 'BaseModel',
                'created_at': '2024-01-01T00:00:00',
                'updated_at': '2024-01-02T00:00:00'
                }
        self.assertEqual(expected, model.to_dict())


if __name__ == '__main__':
    unittest.main()
