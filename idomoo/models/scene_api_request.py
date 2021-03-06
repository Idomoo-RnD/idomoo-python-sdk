# coding: utf-8

"""
    Idomoo API



    OpenAPI spec version: 2.0
    Contact: dev.support@idomoo.com

"""


import pprint
import re

import six

from idomoo import utils
from idomoo.models.output import Output
from idomoo.models.timeline import Timeline


class SceneAPIRequest(object):
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
        'statistic_id': 'str',
        'video_file_name': 'str',
        'output': 'Output',
        'storage': 'list[int]',
        'timeline': 'Timeline'
    }

    attribute_map = {
        'statistic_id': 'statistic_id',
        'video_file_name': 'video_file_name',
        'output': 'output',
        'storage': 'storage',
        'timeline': 'timeline'
    }

    def __init__(self, statistic_id=None, video_file_name=None, output=None, storage=None, timeline=None):
        """SceneAPIRequest - a model defined in Swagger"""

        self._statistic_id = None
        self._video_file_name = None
        self._output = None
        self._storage = None
        self._timeline = None
        self.discriminator = None

        if statistic_id is not None:
            self.statistic_id = statistic_id
        if video_file_name is not None:
            self.video_file_name = video_file_name
        self.output = output
        if storage is not None:
            self.storage = storage
        self.timeline = timeline

    @property
    def statistic_id(self):
        """Gets the statistic_id of this SceneAPIRequest.

        Use statistic ID to group several renders together for analytics.

        :return: The statistic_id of this SceneAPIRequest.
        :rtype: str
        """
        return self._statistic_id

    @statistic_id.setter
    def statistic_id(self, statistic_id):
        """Sets the statistic_id of this SceneAPIRequest.

        Use statistic ID to group several renders together for analytics.

        :param statistic_id: The statistic_id of this SceneAPIRequest.
        :type: str
        """

        self._statistic_id = statistic_id

    @property
    def video_file_name(self):
        """Gets the video_file_name of this SceneAPIRequest.

        The unique file name for all output types. After the file name, the suffix is added after an underscore. Only
        the following characters are allowed: a-z A-Z 0-9 _

        :return: The video_file_name of this SceneAPIRequest.
        :rtype: str
        """
        return self._video_file_name

    @video_file_name.setter
    def video_file_name(self, video_file_name):
        """Sets the video_file_name of this SceneAPIRequest.

        The unique file name for all output types. After the file name, the suffix is added after an underscore. Only
        the following characters are allowed: a-z A-Z 0-9 _

        :param video_file_name: The video_file_name of this SceneAPIRequest.
        :type: str
        """
        if video_file_name is not None and not re.search(utils.VALID_VIDEO_NAME_REGEX, video_file_name):
            raise ValueError("Invalid value for `video_file_name`, must be a follow pattern or equal to `%s`"
                             % utils.VALID_VIDEO_NAME_REGEX)

        self._video_file_name = video_file_name

    @property
    def output(self):
        """Gets the output of this SceneAPIRequest.


        :return: The output of this SceneAPIRequest.
        :rtype: Output
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this SceneAPIRequest.


        :param output: The output of this SceneAPIRequest.
        :type: Output
        """
        if output is None:
            raise ValueError("Invalid value for `output`, must not be `None`")

        self._output = output

    @property
    def storage(self):
        """Gets the storage of this SceneAPIRequest.

        By default all videos are saved on Idomoo servers. For clients working with professional services,
        storage can be defined so that videos are stored on another storage. Please contact support or your project
        manager to define storage.

        :return: The storage of this SceneAPIRequest.
        :rtype: list[int]
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this SceneAPIRequest.

        By default all videos are saved on Idomoo servers. For clients working with professional services,
        storage can be defined so that videos are stored on another storage. Please contact support or your project
        manager to define storage.

        :param storage: The storage of this SceneAPIRequest.
        :type: list[int]
        """

        self._storage = storage

    @property
    def timeline(self):
        """Gets the timeline of this SceneAPIRequest.


        :return: The timeline of this SceneAPIRequest.
        :rtype: Timeline
        """
        return self._timeline

    @timeline.setter
    def timeline(self, timeline):
        """Sets the timeline of this SceneAPIRequest.


        :param timeline: The timeline of this SceneAPIRequest.
        :type: Timeline
        """
        if timeline is None:
            raise ValueError("Invalid value for `timeline`, must not be `None`")

        self._timeline = timeline

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
        if not isinstance(other, SceneAPIRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
