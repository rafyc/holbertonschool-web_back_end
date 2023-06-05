#!/usr/bin/env python3
""" Test
"""
import unittest
from unittest import TestCase
from utils import access_nested_map
from typing import Mapping, Sequence


class TestAccessNestedMap(TestCase):
    '''
    '''
    @parameterized.expand
    def test_access_nested_map(nested_map: Mapping,
                               path: Sequence,
                               except_rez: Any) -> None:

        rez = access_nested_map(nested_map=nested_map, path=path)
        self.assertEqual(rez, except_rez)
