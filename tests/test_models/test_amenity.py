#!/usr/bin/python3
''' Test Amenity '''

import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    def test_init(self):
        amenity = Amenity()
        self.assertIsNotNone(amenity.id)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertEqual(amenity.name, '')

        amenity = Amenity(id='1',
                          created_at='2024-01-01T00:00:00',
                          updated_at='2024-01-02T00:00:00',
                          name='test')
        self.assertEqual(amenity.id, '1')
        self.assertEqual(amenity.created_at,
                         datetime.fromisoformat('2024-01-01T00:00:00'))
        self.assertEqual(amenity.updated_at,
                         datetime.fromisoformat('2024-01-02T00:00:00'))
        self.assertEqual(amenity.name, 'test')

    def test_to_dict(self):
        amenity = Amenity(id='1',
                          created_at='2024-01-01T00:00:00',
                          updated_at='2024-01-02T00:00:00',
                          name='test')
        expected = {
                'id': '1',
                '__class__': 'Amenity',
                'created_at': '2024-01-01T00:00:00',
                'updated_at': '2024-01-02T00:00:00',
                'name': 'test'
                }
        self.assertEqual(expected, amenity.to_dict())


if __name__ == '__main__':
    unittest.main()
