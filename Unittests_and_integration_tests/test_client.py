#!/usr/bin/env python3
""" Test
"""
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from typing import Mapping, Sequence, Any
from unittest.mock import patch, Mock


class TestGithubOrgClient(unittest.TestCase):
    '''
    '''
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, ORG_URL: str, mock_get):
        '''
        '''
        mock_get.return_value = {}

        rez = GithubOrgClient(org_name=ORG_URL).org
        self.assertEqual(rez, mock_get.return_value)
        mock_get.assert_called_once()
