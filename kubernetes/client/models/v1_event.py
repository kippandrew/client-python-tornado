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

from kubernetes.client.models.v1_event_source import V1EventSource  # noqa: F401,E501
from kubernetes.client.models.v1_object_meta import V1ObjectMeta  # noqa: F401,E501
from kubernetes.client.models.v1_object_reference import V1ObjectReference  # noqa: F401,E501


class V1Event(object):
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
        'api_version': 'str',
        'count': 'int',
        'first_timestamp': 'datetime',
        'involved_object': 'V1ObjectReference',
        'kind': 'str',
        'last_timestamp': 'datetime',
        'message': 'str',
        'metadata': 'V1ObjectMeta',
        'reason': 'str',
        'source': 'V1EventSource',
        'type': 'str'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'count': 'count',
        'first_timestamp': 'firstTimestamp',
        'involved_object': 'involvedObject',
        'kind': 'kind',
        'last_timestamp': 'lastTimestamp',
        'message': 'message',
        'metadata': 'metadata',
        'reason': 'reason',
        'source': 'source',
        'type': 'type'
    }

    def __init__(self, api_version=None, count=None, first_timestamp=None, involved_object=None, kind=None, last_timestamp=None, message=None, metadata=None, reason=None, source=None, type=None):  # noqa: E501
        """V1Event - a model defined in Swagger"""  # noqa: E501

        self._api_version = None
        self._count = None
        self._first_timestamp = None
        self._involved_object = None
        self._kind = None
        self._last_timestamp = None
        self._message = None
        self._metadata = None
        self._reason = None
        self._source = None
        self._type = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if count is not None:
            self.count = count
        if first_timestamp is not None:
            self.first_timestamp = first_timestamp
        self.involved_object = involved_object
        if kind is not None:
            self.kind = kind
        if last_timestamp is not None:
            self.last_timestamp = last_timestamp
        if message is not None:
            self.message = message
        self.metadata = metadata
        if reason is not None:
            self.reason = reason
        if source is not None:
            self.source = source
        if type is not None:
            self.type = type

    @property
    def api_version(self):
        """Gets the api_version of this V1Event.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this V1Event.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1Event.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this V1Event.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def count(self):
        """Gets the count of this V1Event.  # noqa: E501

        The number of times this event has occurred.  # noqa: E501

        :return: The count of this V1Event.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this V1Event.

        The number of times this event has occurred.  # noqa: E501

        :param count: The count of this V1Event.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def first_timestamp(self):
        """Gets the first_timestamp of this V1Event.  # noqa: E501

        The time at which the event was first recorded. (Time of server receipt is in TypeMeta.)  # noqa: E501

        :return: The first_timestamp of this V1Event.  # noqa: E501
        :rtype: datetime
        """
        return self._first_timestamp

    @first_timestamp.setter
    def first_timestamp(self, first_timestamp):
        """Sets the first_timestamp of this V1Event.

        The time at which the event was first recorded. (Time of server receipt is in TypeMeta.)  # noqa: E501

        :param first_timestamp: The first_timestamp of this V1Event.  # noqa: E501
        :type: datetime
        """

        self._first_timestamp = first_timestamp

    @property
    def involved_object(self):
        """Gets the involved_object of this V1Event.  # noqa: E501

        The object that this event is about.  # noqa: E501

        :return: The involved_object of this V1Event.  # noqa: E501
        :rtype: V1ObjectReference
        """
        return self._involved_object

    @involved_object.setter
    def involved_object(self, involved_object):
        """Sets the involved_object of this V1Event.

        The object that this event is about.  # noqa: E501

        :param involved_object: The involved_object of this V1Event.  # noqa: E501
        :type: V1ObjectReference
        """
        if involved_object is None:
            raise ValueError("Invalid value for `involved_object`, must not be `None`")  # noqa: E501

        self._involved_object = involved_object

    @property
    def kind(self):
        """Gets the kind of this V1Event.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this V1Event.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1Event.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this V1Event.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def last_timestamp(self):
        """Gets the last_timestamp of this V1Event.  # noqa: E501

        The time at which the most recent occurrence of this event was recorded.  # noqa: E501

        :return: The last_timestamp of this V1Event.  # noqa: E501
        :rtype: datetime
        """
        return self._last_timestamp

    @last_timestamp.setter
    def last_timestamp(self, last_timestamp):
        """Sets the last_timestamp of this V1Event.

        The time at which the most recent occurrence of this event was recorded.  # noqa: E501

        :param last_timestamp: The last_timestamp of this V1Event.  # noqa: E501
        :type: datetime
        """

        self._last_timestamp = last_timestamp

    @property
    def message(self):
        """Gets the message of this V1Event.  # noqa: E501

        A human-readable description of the status of this operation.  # noqa: E501

        :return: The message of this V1Event.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V1Event.

        A human-readable description of the status of this operation.  # noqa: E501

        :param message: The message of this V1Event.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def metadata(self):
        """Gets the metadata of this V1Event.  # noqa: E501

        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata  # noqa: E501

        :return: The metadata of this V1Event.  # noqa: E501
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1Event.

        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata  # noqa: E501

        :param metadata: The metadata of this V1Event.  # noqa: E501
        :type: V1ObjectMeta
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def reason(self):
        """Gets the reason of this V1Event.  # noqa: E501

        This should be a short, machine understandable string that gives the reason for the transition into the object's current status.  # noqa: E501

        :return: The reason of this V1Event.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this V1Event.

        This should be a short, machine understandable string that gives the reason for the transition into the object's current status.  # noqa: E501

        :param reason: The reason of this V1Event.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def source(self):
        """Gets the source of this V1Event.  # noqa: E501

        The component reporting this event. Should be a short machine understandable string.  # noqa: E501

        :return: The source of this V1Event.  # noqa: E501
        :rtype: V1EventSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this V1Event.

        The component reporting this event. Should be a short machine understandable string.  # noqa: E501

        :param source: The source of this V1Event.  # noqa: E501
        :type: V1EventSource
        """

        self._source = source

    @property
    def type(self):
        """Gets the type of this V1Event.  # noqa: E501

        Type of this event (Normal, Warning), new types could be added in the future  # noqa: E501

        :return: The type of this V1Event.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1Event.

        Type of this event (Normal, Warning), new types could be added in the future  # noqa: E501

        :param type: The type of this V1Event.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, V1Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other