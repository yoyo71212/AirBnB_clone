#!/usr/bin/python3
''' Test State '''

import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    def test_init(self):
        state = State()
        self.assertIsNotNone(state.id)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertEqual(state.name, '')

        state = State(id='1',
                      created_at='2024-01-01T00:00:00',
                      updated_at='2024-01-02T00:00:00',
                      name='test')
        self.assertEqual(state.id, '1')
        self.assertEqual(state.created_at,
                         datetime.fromisoformat('2024-01-01T00:00:00'))
        self.assertEqual(state.updated_at,
                         datetime.fromisoformat('2024-01-02T00:00:00'))
        self.assertEqual(state.name, 'test')

    def test_to_dict(self):
        state = State(id='1',
                      created_at='2024-01-01T00:00:00',
                      updated_at='2024-01-02T00:00:00',
                      name='test')
        expected = {
                'id': '1',
                '__class__': 'State',
                'created_at': '2024-01-01T00:00:00',
                'updated_at': '2024-01-02T00:00:00',
                'name': 'test'
                }
        self.assertEqual(expected, state.to_dict())


if __name__ == '__main__':
    unittest.main()
