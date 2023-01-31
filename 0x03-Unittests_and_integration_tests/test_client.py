#!/usr/bin/env python3
"""module containing test cases for client module"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from typing import Any

from parameterized import parameterized, parameterized_class

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """test cases for TestGithubOrgClient class and its methods"""

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google"),
        ("abc", "https://api.github.com/orgs/abc"),
    ])
    @patch('client.get_json')
    def test_org(
            self, org: str, expected_result: str, mock_get_json: Any) -> None:
        """test that GithubOrgClient.org returns the correct value"""
        client = GithubOrgClient(org)
        mock_get_json.return_value = expected_result
        self.assertEqual(client.org, expected_result)
        mock_get_json.assert_called_once()

    def test_public_repos_url(self) -> None:
        """method to unit-test GithubOrgClient._public_repos_url"""
        expected_result = "https://api.github.com/orgs/google/repos"
        with patch(
            'client.GithubOrgClient.org', new_callable=PropertyMock
                ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/orgs/google/repos"
                }
            client = GithubOrgClient('google')
            self.assertEqual(client._public_repos_url, expected_result)

    @parameterized.expand([
        ('google', {'repos_url': 'https://api.github.com/orgs/google/repos'}),
        ('github', {'repos_url': 'https://api.github.com/orgs/github/repos'}),
    ])
    @patch('client.get_json')
    def test_public_repos(
            self, org: str, payload: dict, mock_get_json: Any) -> None:
        """Tests the list of repos is what is expected from the chosen payload
        Tests that the mocked property and the mocked get_json was called once
        """
        mock_get_json.return_value = payload
        expected_result = payload['repos_url']
        with patch(
            'client.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock) as mock_public_repos:
            client = GithubOrgClient(org)
            mock_public_repos.return_value = mock_get_json()['repos_url']
            self.assertEqual(client._public_repos_url, expected_result)
            mock_public_repos.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(
            self, license: dict, key: str, expected_result: bool) -> None:
        """unit-test GithubOrgClient.has_license"""
        self.assertEqual(
            GithubOrgClient.has_license(license, key),
            expected_result
            )


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD,
    )
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration testing for GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        pass
