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


class V1AzureFileVolumeSource(object):
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
        'read_only': 'bool',
        'secret_name': 'str',
        'share_name': 'str'
    }

    attribute_map = {
        'read_only': 'readOnly',
        'secret_name': 'secretName',
        'share_name': 'shareName'
    }

    def __init__(self, read_only=None, secret_name=None, share_name=None):  # noqa: E501
        """V1AzureFileVolumeSource - a model defined in Swagger"""  # noqa: E501

        self._read_only = None
        self._secret_name = None
        self._share_name = None
        self.discriminator = None

        if read_only is not None:
            self.read_only = read_only
        self.secret_name = secret_name
        self.share_name = share_name

    @property
    def read_only(self):
        """Gets the read_only of this V1AzureFileVolumeSource.  # noqa: E501

        Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.  # noqa: E501

        :return: The read_only of this V1AzureFileVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this V1AzureFileVolumeSource.

        Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.  # noqa: E501

        :param read_only: The read_only of this V1AzureFileVolumeSource.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def secret_name(self):
        """Gets the secret_name of this V1AzureFileVolumeSource.  # noqa: E501

        the name of secret that contains Azure Storage Account Name and Key  # noqa: E501

        :return: The secret_name of this V1AzureFileVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        """Sets the secret_name of this V1AzureFileVolumeSource.

        the name of secret that contains Azure Storage Account Name and Key  # noqa: E501

        :param secret_name: The secret_name of this V1AzureFileVolumeSource.  # noqa: E501
        :type: str
        """
        if secret_name is None:
            raise ValueError("Invalid value for `secret_name`, must not be `None`")  # noqa: E501

        self._secret_name = secret_name

    @property
    def share_name(self):
        """Gets the share_name of this V1AzureFileVolumeSource.  # noqa: E501

        Share Name  # noqa: E501

        :return: The share_name of this V1AzureFileVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._share_name

    @share_name.setter
    def share_name(self, share_name):
        """Sets the share_name of this V1AzureFileVolumeSource.

        Share Name  # noqa: E501

        :param share_name: The share_name of this V1AzureFileVolumeSource.  # noqa: E501
        :type: str
        """
        if share_name is None:
            raise ValueError("Invalid value for `share_name`, must not be `None`")  # noqa: E501

        self._share_name = share_name

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
        if not isinstance(other, V1AzureFileVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
