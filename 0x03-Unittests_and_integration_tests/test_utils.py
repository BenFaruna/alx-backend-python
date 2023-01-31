#!/usr/bin/env python3
"""Module containing test cases for utils module"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from typing import Any
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """class tests access_nested =_map function of the utils module"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self, nested_map: dict, path: tuple, expected: Any):
        """test method for access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(
            self, nested_map: dict, path: tuple):
        """test access_nested_map exception on KeyError"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """test cases for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url: str, payload: dict) -> None:
        """test get_json function using a mock object to test its response"""
        class TestClass:
            def json(self):
                return payload

        r = TestClass()

        with patch('requests.get', return_value=r) as mock_get_json:
            self.assertTrue(hasattr(mock_get_json, 'json'))
            self.assertEqual(get_json(url), payload)
            mock_get_json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """test cases for memoize function in utils"""

    def test_memoize(self) -> None:
        """test memoize function"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            test_instance = TestClass()

            result1 = test_instance.a_property
            result2 = test_instance.a_property

            self.assertEqual(result1, result2)

            mock_method.assert_called_once()
