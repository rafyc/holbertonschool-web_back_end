#!/usr/bin/env python3
""" Test
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from typing import Mapping, Sequence, Any
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    '''utils module
    '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence,
                               except_rez: Any) -> None:

        rez = access_nested_map(nested_map=nested_map, path=path)
        self.assertEqual(rez, except_rez)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                               path: Sequence,) -> None:
        with self.assertRaises(KeyError):
            access_nested_map(nested_map=nested_map, path=path)

class TestGetJson(unittest.TestCase):
    '''
    '''
    @parameterized.expand([
        ('http://example.com', {"payload": True}),
        ('http://holberton.io',{"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url : str, expected_payload, mock_get) -> None:

        mock_json = Mock(return_value=expected_payload)
        mock_get.return_value = Mock(json=mock_json)

        rez = get_json(url = test_url)

        self.assertEqual(rez, expected_payload)
