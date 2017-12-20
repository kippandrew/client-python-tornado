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

from kubernetes.client.models.v1_load_balancer_status import V1LoadBalancerStatus  # noqa: F401,E501


class V1beta1IngressStatus(object):
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
        'load_balancer': 'V1LoadBalancerStatus'
    }

    attribute_map = {
        'load_balancer': 'loadBalancer'
    }

    def __init__(self, load_balancer=None):  # noqa: E501
        """V1beta1IngressStatus - a model defined in Swagger"""  # noqa: E501

        self._load_balancer = None
        self.discriminator = None

        if load_balancer is not None:
            self.load_balancer = load_balancer

    @property
    def load_balancer(self):
        """Gets the load_balancer of this V1beta1IngressStatus.  # noqa: E501

        LoadBalancer contains the current status of the load-balancer.  # noqa: E501

        :return: The load_balancer of this V1beta1IngressStatus.  # noqa: E501
        :rtype: V1LoadBalancerStatus
        """
        return self._load_balancer

    @load_balancer.setter
    def load_balancer(self, load_balancer):
        """Sets the load_balancer of this V1beta1IngressStatus.

        LoadBalancer contains the current status of the load-balancer.  # noqa: E501

        :param load_balancer: The load_balancer of this V1beta1IngressStatus.  # noqa: E501
        :type: V1LoadBalancerStatus
        """

        self._load_balancer = load_balancer

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
        if not isinstance(other, V1beta1IngressStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
