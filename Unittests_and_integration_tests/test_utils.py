#!/usr/bin/env python3
""" Test
"""
import unittest
from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(TestCase):
    '''
    '''
    test_cases = [
    {"nested_map": {"a": 1}, "path": ("a",)},
    {"nested_map": {"a": {"b": 2}}, "path": ("a",)},
    {"nested_map": {"a": {"b": 2}}, "path": ("a", "b")}
    ]

    @parameterized.parameterized.expand(test_cases)

    def test_access_nested_map(nested_map: Mapping,
                               path: Sequence,
                               except_rez: Any) -> None:

        rez = access_nested_map(nested_map=nested_map, path=path)
        self.assertEqual(rez, except_rez)
