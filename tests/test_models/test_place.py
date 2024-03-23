#!/usr/bin/python3
''' Test Place '''

import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    def test_init(self):
        place = Place()
        self.assertIsNotNone(place.id)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertEqual(place.city_id, '')
        self.assertEqual(place.user_id, '')
        self.assertEqual(place.name, '')
        self.assertEqual(place.description, '')
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

        place = Place(id='1',
                      created_at='2024-01-01T00:00:00',
                      updated_at='2024-01-02T00:00:00',
                      city_id='2',
                      user_id='3',
                      name='test',
                      description='test1',
                      number_rooms=3,
                      number_bathrooms=2,
                      max_guest=4,
                      price_by_night=50,
                      latitude=7.0,
                      longitude=8.0,
                      amenity_ids=['4', '5'])
        self.assertEqual(place.id, '1')
        self.assertEqual(place.created_at,
                         datetime.fromisoformat('2024-01-01T00:00:00'))
        self.assertEqual(place.updated_at,
                         datetime.fromisoformat('2024-01-02T00:00:00'))
        self.assertEqual(place.city_id, '2')
        self.assertEqual(place.user_id, '3')
        self.assertEqual(place.name, 'test')
        self.assertEqual(place.description, 'test1')
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 50)
        self.assertEqual(place.latitude, 7.0)
        self.assertEqual(place.longitude, 8.0)
        self.assertEqual(place.amenity_ids, ['4', '5'])

    def test_to_dict(self):
        place = Place(id='1',
                      created_at='2024-01-01T00:00:00',
                      updated_at='2024-01-02T00:00:00',
                      city_id='2',
                      user_id='3',
                      name='test',
                      description='test1',
                      number_rooms=3,
                      number_bathrooms=2,
                      max_guest=4,
                      price_by_night=50,
                      latitude=7.0,
                      longitude=8.0,
                      amenity_ids=['4', '5'])
        expected = {
                'id': '1',
                '__class__': 'Place',
                'created_at': '2024-01-01T00:00:00',
                'updated_at': '2024-01-02T00:00:00',
                'city_id': '2',
                'user_id': '3',
                'name': 'test',
                'description': 'test1',
                'number_rooms': 3,
                'number_bathrooms': 2,
                'max_guest': 4,
                'price_by_night': 50,
                'latitude': 7.0,
                'longitude': 8.0,
                'amenity_ids': ['4', '5']
                }
        self.assertEqual(expected, place.to_dict())


if __name__ == "__main__":
    unittest.main()
