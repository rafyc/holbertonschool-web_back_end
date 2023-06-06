#!/usr/bin/env python3
""" Test
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
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
        '''
        '''

        rez = access_nested_map(nested_map=nested_map, path=path)
        self.assertEqual(rez, except_rez)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence,) -> None:
        '''
        '''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map=nested_map, path=path)


class TestGetJson(unittest.TestCase):
    '''
    '''
    @parameterized.expand([
        ('http://example.com', {"payload": True}),
        ('http://holberton.io', {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url: str,
                      expected_payload, mock_get) -> None:

        mock_json = Mock(return_value=expected_payload)
        mock_get.return_value = Mock(json=mock_json)

        rez = get_json(url=test_url)

        self.assertEqual(rez, expected_payload)


class TestMemoize(unittest.TestCase):
    '''
    '''
    def test_memoize(self):
        '''
        '''
        class TestClass:
            '''
            '''
            def a_method(self):
                '''
                '''
                return 42

            @memoize
            def a_property(self):
                '''
                '''
                return self.a_method()

        test_instance = TestClass()
        with patch.object(TestClass, 'a_method') as mock_meth:
            mock_meth.return_value = 42
            rez1 = test_instance.a_property
            rez2 = test_instance.a_property

            mock_meth.assert_called_once()

            # Assert that the results are the same
            self.assertEqual(rez1, rez2)
            self.assertEqual(rez1, 42)
