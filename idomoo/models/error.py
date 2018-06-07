# coding: utf-8

"""
    Idomoo API



    OpenAPI spec version: 2.0
    Contact: dev.support@idomoo.com

"""


import pprint

import six


class Error(object):
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
        'error_code': 'int',
        'error_message': 'str',
        'error_description': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_message': 'error_message',
        'error_description': 'error_description'
    }

    def __init__(self, error_code=None, error_message=None, error_description=None):
        """Error - a model defined in Swagger"""

        self._error_code = None
        self._error_message = None
        self._error_description = None
        self.discriminator = None

        self.error_code = error_code
        self.error_message = error_message
        self.error_description = error_description

    @property
    def error_code(self):
        """Gets the error_code of this Error.

        A code for the error.

        :return: The error_code of this Error.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this Error.

        A code for the error.

        :param error_code: The error_code of this Error.
        :type: int
        """
        if error_code is None:
            raise ValueError("Invalid value for `error_code`, must not be `None`")

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this Error.

        A title message about the error.

        :return: The error_message of this Error.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this Error.

        A title message about the error.

        :param error_message: The error_message of this Error.
        :type: str
        """
        if error_message is None:
            raise ValueError("Invalid value for `error_message`, must not be `None`")

        self._error_message = error_message

    @property
    def error_description(self):
        """Gets the error_description of this Error.

        A more detailed explanation regarding what went wrong.

        :return: The error_description of this Error.
        :rtype: str
        """
        return self._error_description

    @error_description.setter
    def error_description(self, error_description):
        """Sets the error_description of this Error.

        A more detailed explanation regarding what went wrong.

        :param error_description: The error_description of this Error.
        :type: str
        """
        if error_description is None:
            raise ValueError("Invalid value for `error_description`, must not be `None`")

        self._error_description = error_description

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
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
