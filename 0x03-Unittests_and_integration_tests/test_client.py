#!/usr/bin/env python3
"""Defines TestGithubOrgClient class"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock

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

    def test_public_repos_url(self):
        """Test public_repos_url property"""
        with patch.object(GithubOrgClient,
                          'org', new_callable=PropertyMock) as org_mock:
            org_mock.return_value = {"repos_url": "google"}

            github_client = GithubOrgClient("google")
            self.assertEqual(github_client._public_repos_url, "google")
