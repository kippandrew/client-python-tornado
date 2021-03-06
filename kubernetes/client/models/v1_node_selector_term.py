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

from kubernetes.client.models.v1_node_selector_requirement import V1NodeSelectorRequirement  # noqa: F401,E501


class V1NodeSelectorTerm(object):
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
        'match_expressions': 'list[V1NodeSelectorRequirement]'
    }

    attribute_map = {
        'match_expressions': 'matchExpressions'
    }

    def __init__(self, match_expressions=None):  # noqa: E501
        """V1NodeSelectorTerm - a model defined in Swagger"""  # noqa: E501

        self._match_expressions = None
        self.discriminator = None

        self.match_expressions = match_expressions

    @property
    def match_expressions(self):
        """Gets the match_expressions of this V1NodeSelectorTerm.  # noqa: E501

        Required. A list of node selector requirements. The requirements are ANDed.  # noqa: E501

        :return: The match_expressions of this V1NodeSelectorTerm.  # noqa: E501
        :rtype: list[V1NodeSelectorRequirement]
        """
        return self._match_expressions

    @match_expressions.setter
    def match_expressions(self, match_expressions):
        """Sets the match_expressions of this V1NodeSelectorTerm.

        Required. A list of node selector requirements. The requirements are ANDed.  # noqa: E501

        :param match_expressions: The match_expressions of this V1NodeSelectorTerm.  # noqa: E501
        :type: list[V1NodeSelectorRequirement]
        """
        if match_expressions is None:
            raise ValueError("Invalid value for `match_expressions`, must not be `None`")  # noqa: E501

        self._match_expressions = match_expressions

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
        if not isinstance(other, V1NodeSelectorTerm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
