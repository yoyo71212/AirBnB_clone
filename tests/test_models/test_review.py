#!/usr/bin/python3
''' Test Review '''

import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    def test_init(self):
        review = Review()
        self.assertIsNotNone(review.id)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
        self.assertEqual(review.place_id, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.text, '')

        review = Review(id='1',
                        created_at='2024-01-01T00:00:00',
                        updated_at='2024-01-02T00:00:00',
                        place_id='2',
                        user_id='3',
                        text='test')
        self.assertEqual(review.id, '1')
        self.assertEqual(review.created_at,
                         datetime.fromisoformat('2024-01-01T00:00:00'))
        self.assertEqual(review.updated_at,
                         datetime.fromisoformat('2024-01-02T00:00:00'))
        self.assertEqual(review.place_id, '2')
        self.assertEqual(review.user_id, '3')
        self.assertEqual(review.text, 'test')

    def test_to_dict(self):
        review = Review(id='1',
                        created_at='2024-01-01T00:00:00',
                        updated_at='2024-01-02T00:00:00',
                        place_id='2',
                        user_id='3',
                        text='test')
        expected = {
                'id': '1',
                '__class__': 'Review',
                'created_at': '2024-01-01T00:00:00',
                'updated_at': '2024-01-02T00:00:00',
                'place_id': '2',
                'user_id': '3',
                'text': 'test'
                }
        self.assertEqual(expected, review.to_dict())


if __name__ == "__main__":
    unittest.main()
