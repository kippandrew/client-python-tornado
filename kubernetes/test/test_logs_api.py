# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.8.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import kubernetes.client
from kubernetes.client.api.logs_api import LogsApi  # noqa: E501
from kubernetes.client.rest import ApiException


class TestLogsApi(unittest.TestCase):
    """LogsApi unit test stubs"""

    def setUp(self):
        self.api = client.api.logs_api.LogsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_log_file_handler(self):
        """Test case for log_file_handler

        """
        pass

    def test_log_file_list_handler(self):
        """Test case for log_file_list_handler

        """
        pass


if __name__ == '__main__':
    unittest.main()