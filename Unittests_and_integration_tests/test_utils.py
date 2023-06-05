#!/usr/bin/env python3
""" Test
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    '''
    '''
    test_cases = [
    {"nested_map": {"a": 1}, "path": ("a",), "except_rez": 1},
    {"nested_map": {"a": {"b": 2}}, "path": ("a",), "except_rez": {"b": 2}},
    {"nested_map": {"a": {"b": 2}}, "path": ("a", "b"), "except_rez": 2}
    ]

    @parameterized.parameterized.expand(test_cases)

    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence,
                               except_rez: Any) -> None:

        rez = access_nested_map(nested_map=nested_map, path=path)
        self.assertEqual(rez, except_rez)
