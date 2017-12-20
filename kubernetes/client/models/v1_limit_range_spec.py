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

from kubernetes.client.models.v1_limit_range_item import V1LimitRangeItem  # noqa: F401,E501


class V1LimitRangeSpec(object):
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
        'limits': 'list[V1LimitRangeItem]'
    }

    attribute_map = {
        'limits': 'limits'
    }

    def __init__(self, limits=None):  # noqa: E501
        """V1LimitRangeSpec - a model defined in Swagger"""  # noqa: E501

        self._limits = None
        self.discriminator = None

        self.limits = limits

    @property
    def limits(self):
        """Gets the limits of this V1LimitRangeSpec.  # noqa: E501

        Limits is the list of LimitRangeItem objects that are enforced.  # noqa: E501

        :return: The limits of this V1LimitRangeSpec.  # noqa: E501
        :rtype: list[V1LimitRangeItem]
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this V1LimitRangeSpec.

        Limits is the list of LimitRangeItem objects that are enforced.  # noqa: E501

        :param limits: The limits of this V1LimitRangeSpec.  # noqa: E501
        :type: list[V1LimitRangeItem]
        """
        if limits is None:
            raise ValueError("Invalid value for `limits`, must not be `None`")  # noqa: E501

        self._limits = limits

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
        if not isinstance(other, V1LimitRangeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
