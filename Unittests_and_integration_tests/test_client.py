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
        ('google.org'),
        ('abc.org')
    ])
    @patch('client.get_json')
    def test_org(self, ORG_URL: str, mock_get):
        '''
        '''
        expected_result = {}

        mock_get.return_value = expected_result
        client = GithubOrgClient(org_name=ORG_URL).org
        mock_get.assert_called_once()
