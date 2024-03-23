#!/usr/bin/python3
''' Test City '''

import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    def test_init(self):
        city = City()
        self.assertIsNotNone(city.id)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertEqual(city.state_id, '')
        self.assertEqual(city.name, '')

        city = City(id='1',
                    created_at='2024-01-01T00:00:00',
                    updated_at='2024-01-02T00:00:00',
                    state_id='2',
                    name='test')
        self.assertEqual(city.id, '1')
        self.assertEqual(city.created_at,
                         datetime.fromisoformat('2024-01-01T00:00:00'))
        self.assertEqual(city.updated_at,
                         datetime.fromisoformat('2024-01-02T00:00:00'))
        self.assertEqual(city.state_id, '2')
        self.assertEqual(city.name, 'test')

    def test_to_dict(self):
        city = City(id='1',
                    created_at='2024-01-01T00:00:00',
                    updated_at='2024-01-02T00:00:00',
                    state_id='2',
                    name='test')
        expected = {
                'id': '1',
                '__class__': 'City',
                'created_at': '2024-01-01T00:00:00',
                'updated_at': '2024-01-02T00:00:00',
                'state_id': '2',
                'name': 'test'
                }
        self.assertEqual(expected, city.to_dict())


if __name__ == '__main__':
    unittest.main()
