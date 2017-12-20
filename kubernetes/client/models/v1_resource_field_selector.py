# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.8.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1ResourceFieldSelector(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'container_name': 'str',
        'divisor': 'str',
        'resource': 'str'
    }

    attribute_map = {
        'container_name': 'containerName',
        'divisor': 'divisor',
        'resource': 'resource'
    }

    def __init__(self, container_name=None, divisor=None, resource=None):  # noqa: E501
        """V1ResourceFieldSelector - a model defined in Swagger"""  # noqa: E501

        self._container_name = None
        self._divisor = None
        self._resource = None
        self.discriminator = None

        if container_name is not None:
            self.container_name = container_name
        if divisor is not None:
            self.divisor = divisor
        self.resource = resource

    @property
    def container_name(self):
        """Gets the container_name of this V1ResourceFieldSelector.  # noqa: E501

        Container name: required for volumes, optional for env vars  # noqa: E501

        :return: The container_name of this V1ResourceFieldSelector.  # noqa: E501
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """Sets the container_name of this V1ResourceFieldSelector.

        Container name: required for volumes, optional for env vars  # noqa: E501

        :param container_name: The container_name of this V1ResourceFieldSelector.  # noqa: E501
        :type: str
        """

        self._container_name = container_name

    @property
    def divisor(self):
        """Gets the divisor of this V1ResourceFieldSelector.  # noqa: E501

        Specifies the output format of the exposed resources, defaults to \"1\"  # noqa: E501

        :return: The divisor of this V1ResourceFieldSelector.  # noqa: E501
        :rtype: str
        """
        return self._divisor

    @divisor.setter
    def divisor(self, divisor):
        """Sets the divisor of this V1ResourceFieldSelector.

        Specifies the output format of the exposed resources, defaults to \"1\"  # noqa: E501

        :param divisor: The divisor of this V1ResourceFieldSelector.  # noqa: E501
        :type: str
        """

        self._divisor = divisor

    @property
    def resource(self):
        """Gets the resource of this V1ResourceFieldSelector.  # noqa: E501

        Required: resource to select  # noqa: E501

        :return: The resource of this V1ResourceFieldSelector.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this V1ResourceFieldSelector.

        Required: resource to select  # noqa: E501

        :param resource: The resource of this V1ResourceFieldSelector.  # noqa: E501
        :type: str
        """
        if resource is None:
            raise ValueError("Invalid value for `resource`, must not be `None`")  # noqa: E501

        self._resource = resource

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1ResourceFieldSelector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
