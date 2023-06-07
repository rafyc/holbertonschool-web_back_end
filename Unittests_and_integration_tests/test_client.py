#!/usr/bin/env python3
""" Test
"""
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from typing import Mapping, Sequence, Any
from unittest.mock import patch, Mock, PropertyMock


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

    def test_public_repos_url(self):
        '''
        '''
        mock_obj = 'client.GithubOrgClient.org'
        mock_value = {'https://api.github.com/orgs/google'}

        with patch(mock_obj,
                   new_callable=PropertyMock,
                   return_value=mock_value) as mock_repos_url:
            result = GithubOrgClient("Google").org
            self.assertEqual(result, mock_repos_url.return_value)

    def test_public_repos(self):
        '''
        '''
        mock_obj = 'client.GithubOrgClient.org._public_repos_url'
        mock_value = {'https://api.github.com/orgs/google'}
        with patch(mock_obj, new_callable=PropertyMock, return_value=mock_value)

            rez = GithubOrgClient('Google').public_repos()
            self.assertEqual(result, ['Google'])
            mock_get.assert_called_once()
            mock_public_repos.assert_called_once()
