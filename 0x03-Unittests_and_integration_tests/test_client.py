#!/usr/bin/env python3
"""Defines TestGithubOrgClient class"""

import unittest
from parameterized import parameterized
from unittest.mock import patch

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Implement TestGithubOrgClient class"""
    @parameterized.expand(['google', 'abc'])
    @patch('client.get_json')
    def test_org(self, org_name, get_mock):
        """Test org method"""
        get_mock.return_value = lambda: {"org_name": org_name}

        github_client = GithubOrgClient(org_name)
        self.assertEqual(github_client.org(), {"org_name": org_name})
        get_mock.assert_called_once()
