# coding: utf-8

"""
    Idomoo API



    OpenAPI spec version: 2.0
    Contact: dev.support@idomoo.com

"""


import pprint

import six


class AccountMetadata(object):
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
        'account_id': 'float',
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'company': 'str',
        'max_concurrency_allowed': 'float',
        'credits': 'float'
    }

    attribute_map = {
        'account_id': 'account_id',
        'email': 'email',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'company': 'company',
        'max_concurrency_allowed': 'max_concurrency_allowed',
        'credits': 'credits'
    }

    def __init__(self, account_id=None, email=None, first_name=None, last_name=None, company=None, max_concurrency_allowed=None, credits=None):
        """AccountMetadata - a model defined in Swagger"""

        self._account_id = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self._company = None
        self._max_concurrency_allowed = None
        self._credits = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if company is not None:
            self.company = company
        if max_concurrency_allowed is not None:
            self.max_concurrency_allowed = max_concurrency_allowed
        if credits is not None:
            self.credits = credits

    @property
    def account_id(self):
        """Gets the account_id of this AccountMetadata.


        :return: The account_id of this AccountMetadata.
        :rtype: float
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountMetadata.


        :param account_id: The account_id of this AccountMetadata.
        :type: float
        """

        self._account_id = account_id

    @property
    def email(self):
        """Gets the email of this AccountMetadata.


        :return: The email of this AccountMetadata.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AccountMetadata.


        :param email: The email of this AccountMetadata.
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this AccountMetadata.


        :return: The first_name of this AccountMetadata.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this AccountMetadata.


        :param first_name: The first_name of this AccountMetadata.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this AccountMetadata.


        :return: The last_name of this AccountMetadata.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this AccountMetadata.


        :param last_name: The last_name of this AccountMetadata.
        :type: str
        """

        self._last_name = last_name

    @property
    def company(self):
        """Gets the company of this AccountMetadata.


        :return: The company of this AccountMetadata.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this AccountMetadata.


        :param company: The company of this AccountMetadata.
        :type: str
        """

        self._company = company

    @property
    def max_concurrency_allowed(self):
        """Gets the max_concurrency_allowed of this AccountMetadata.


        :return: The max_concurrency_allowed of this AccountMetadata.
        :rtype: float
        """
        return self._max_concurrency_allowed

    @max_concurrency_allowed.setter
    def max_concurrency_allowed(self, max_concurrency_allowed):
        """Sets the max_concurrency_allowed of this AccountMetadata.


        :param max_concurrency_allowed: The max_concurrency_allowed of this AccountMetadata.
        :type: float
        """

        self._max_concurrency_allowed = max_concurrency_allowed

    @property
    def credits(self):
        """Gets the credits of this AccountMetadata.


        :return: The credits of this AccountMetadata.
        :rtype: float
        """
        return self._credits

    @credits.setter
    def credits(self, credits):
        """Sets the credits of this AccountMetadata.


        :param credits: The credits of this AccountMetadata.
        :type: float
        """

        self._credits = credits

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
        if not isinstance(other, AccountMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
