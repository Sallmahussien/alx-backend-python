#!/usr/bin/env python3
"""Defines test_utils module"""

import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized

from utils import *


class TestAccessNestedMap(unittest.TestCase):
    """Class to test access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map with keyError exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class to test get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload", True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, get_mock):
        """Test get_json with two different urls"""
        get_mock.json.return_value = test_payload
        get_mock.return_value = get_mock

        self.assertEqual(get_json(test_url), test_payload)
        get_mock.assert_called_once_with(test_url)
