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
from kubernetes.client.api.custom_objects_api import CustomObjectsApi  # noqa: E501
from kubernetes.client.rest import ApiException


class TestCustomObjectsApi(unittest.TestCase):
    """CustomObjectsApi unit test stubs"""

    def setUp(self):
        self.api = client.api.custom_objects_api.CustomObjectsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_cluster_custom_object(self):
        """Test case for create_cluster_custom_object

        """
        pass

    def test_create_namespaced_custom_object(self):
        """Test case for create_namespaced_custom_object

        """
        pass

    def test_delete_cluster_custom_object(self):
        """Test case for delete_cluster_custom_object

        """
        pass

    def test_delete_namespaced_custom_object(self):
        """Test case for delete_namespaced_custom_object

        """
        pass

    def test_get_cluster_custom_object(self):
        """Test case for get_cluster_custom_object

        """
        pass

    def test_get_namespaced_custom_object(self):
        """Test case for get_namespaced_custom_object

        """
        pass

    def test_list_cluster_custom_object(self):
        """Test case for list_cluster_custom_object

        """
        pass

    def test_list_namespaced_custom_object(self):
        """Test case for list_namespaced_custom_object

        """
        pass

    def test_replace_cluster_custom_object(self):
        """Test case for replace_cluster_custom_object

        """
        pass

    def test_replace_namespaced_custom_object(self):
        """Test case for replace_namespaced_custom_object

        """
        pass


if __name__ == '__main__':
    unittest.main()