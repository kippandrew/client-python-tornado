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
from kubernetes.client.api.admissionregistration_api import AdmissionregistrationApi  # noqa: E501
from kubernetes.client.rest import ApiException


class TestAdmissionregistrationApi(unittest.TestCase):
    """AdmissionregistrationApi unit test stubs"""

    def setUp(self):
        self.api = client.api.admissionregistration_api.AdmissionregistrationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_api_group(self):
        """Test case for get_api_group

        """
        pass


if __name__ == '__main__':
    unittest.main()
