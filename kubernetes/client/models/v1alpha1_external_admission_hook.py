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

from kubernetes.client.models.v1alpha1_admission_hook_client_config import V1alpha1AdmissionHookClientConfig  # noqa: F401,E501
from kubernetes.client.models.v1alpha1_rule_with_operations import V1alpha1RuleWithOperations  # noqa: F401,E501


class V1alpha1ExternalAdmissionHook(object):
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
        'client_config': 'V1alpha1AdmissionHookClientConfig',
        'failure_policy': 'str',
        'name': 'str',
        'rules': 'list[V1alpha1RuleWithOperations]'
    }

    attribute_map = {
        'client_config': 'clientConfig',
        'failure_policy': 'failurePolicy',
        'name': 'name',
        'rules': 'rules'
    }

    def __init__(self, client_config=None, failure_policy=None, name=None, rules=None):  # noqa: E501
        """V1alpha1ExternalAdmissionHook - a model defined in Swagger"""  # noqa: E501

        self._client_config = None
        self._failure_policy = None
        self._name = None
        self._rules = None
        self.discriminator = None

        self.client_config = client_config
        if failure_policy is not None:
            self.failure_policy = failure_policy
        self.name = name
        if rules is not None:
            self.rules = rules

    @property
    def client_config(self):
        """Gets the client_config of this V1alpha1ExternalAdmissionHook.  # noqa: E501

        ClientConfig defines how to communicate with the hook. Required  # noqa: E501

        :return: The client_config of this V1alpha1ExternalAdmissionHook.  # noqa: E501
        :rtype: V1alpha1AdmissionHookClientConfig
        """
        return self._client_config

    @client_config.setter
    def client_config(self, client_config):
        """Sets the client_config of this V1alpha1ExternalAdmissionHook.

        ClientConfig defines how to communicate with the hook. Required  # noqa: E501

        :param client_config: The client_config of this V1alpha1ExternalAdmissionHook.  # noqa: E501
        :type: V1alpha1AdmissionHookClientConfig
        """
        if client_config is None:
            raise ValueError("Invalid value for `client_config`, must not be `None`")  # noqa: E501

        self._client_config = client_config

    @property
    def failure_policy(self):
        """Gets the failure_policy of this V1alpha1ExternalAdmissionHook.  # noqa: E501

        FailurePolicy defines how unrecognized errors from the admission endpoint are handled - allowed values are Ignore or Fail. Defaults to Ignore.  # noqa: E501

        :return: The failure_policy of this V1alpha1ExternalAdmissionHook.  # noqa: E501
        :rtype: str
        """
        return self._failure_policy

    @failure_policy.setter
    def failure_policy(self, failure_policy):
        """Sets the failure_policy of this V1alpha1ExternalAdmissionHook.

        FailurePolicy defines how unrecognized errors from the admission endpoint are handled - allowed values are Ignore or Fail. Defaults to Ignore.  # noqa: E501

        :param failure_policy: The failure_policy of this V1alpha1ExternalAdmissionHook.  # noqa: E501
        :type: str
        """

        self._failure_policy = failure_policy

    @property
    def name(self):
        """Gets the name of this V1alpha1ExternalAdmissionHook.  # noqa: E501

        The name of the external admission webhook. Name should be fully qualified, e.g., imagepolicy.kubernetes.io, where \"imagepolicy\" is the name of the webhook, and kubernetes.io is the name of the organization. Required.  # noqa: E501

        :return: The name of this V1alpha1ExternalAdmissionHook.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1ExternalAdmissionHook.

        The name of the external admission webhook. Name should be fully qualified, e.g., imagepolicy.kubernetes.io, where \"imagepolicy\" is the name of the webhook, and kubernetes.io is the name of the organization. Required.  # noqa: E501

        :param name: The name of this V1alpha1ExternalAdmissionHook.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def rules(self):
        """Gets the rules of this V1alpha1ExternalAdmissionHook.  # noqa: E501

        Rules describes what operations on what resources/subresources the webhook cares about. The webhook cares about an operation if it matches _any_ Rule.  # noqa: E501

        :return: The rules of this V1alpha1ExternalAdmissionHook.  # noqa: E501
        :rtype: list[V1alpha1RuleWithOperations]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this V1alpha1ExternalAdmissionHook.

        Rules describes what operations on what resources/subresources the webhook cares about. The webhook cares about an operation if it matches _any_ Rule.  # noqa: E501

        :param rules: The rules of this V1alpha1ExternalAdmissionHook.  # noqa: E501
        :type: list[V1alpha1RuleWithOperations]
        """

        self._rules = rules

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
        if not isinstance(other, V1alpha1ExternalAdmissionHook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
