# coding: utf-8

"""
    Idomoo API



    OpenAPI spec version: 2.0
    Contact: dev.support@idomoo.com

"""


import pprint
import re

import six

from idomoo.models.accessibility_output import AccessibilityOutput
from idomoo.models.gif_output import GIFOutput
from idomoo.models.jpg_output import JPGOutput
from idomoo.models.video_output import VideoOutput


class Output(object):
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
        'video': 'list[VideoOutput]',
        'gif': 'list[GIFOutput]',
        'jpg': 'list[JPGOutput]',
        'accessibility': 'AccessibilityOutput'
    }

    attribute_map = {
        'video': 'video',
        'gif': 'gif',
        'jpg': 'jpg',
        'accessibility': 'accessibility'
    }

    def __init__(self, video=None, gif=None, jpg=None, accessibility=None):
        """Output - a model defined in Swagger"""

        self._video = None
        self._gif = None
        self._jpg = None
        self._accessibility = None
        self.discriminator = None

        if video is not None:
            self.video = video
        if gif is not None:
            self.gif = gif
        if jpg is not None:
            self.jpg = jpg
        if accessibility is not None:
            self.accessibility = accessibility

    @property
    def video(self):
        """Gets the video of this Output.

        Specify your video outputs.

        :return: The video of this Output.
        :rtype: list[VideoOutput]
        """
        return self._video

    @video.setter
    def video(self, video):
        """Sets the video of this Output.

        Specify your video outputs.

        :param video: The video of this Output.
        :type: list[VideoOutput]
        """

        self._video = video

    @property
    def gif(self):
        """Gets the gif of this Output.

        Specify your animated gif outputs. Usually used for thumbnails.

        :return: The gif of this Output.
        :rtype: list[GIFOutput]
        """
        return self._gif

    @gif.setter
    def gif(self, gif):
        """Sets the gif of this Output.

        Specify your animated gif outputs. Usually used for thumbnails.

        :param gif: The gif of this Output.
        :type: list[GIFOutput]
        """

        self._gif = gif

    @property
    def jpg(self):
        """Gets the jpg of this Output.

        Specify your jpg outputs. Usually used for thumbnails.

        :return: The jpg of this Output.
        :rtype: list[JPGOutput]
        """
        return self._jpg

    @jpg.setter
    def jpg(self, jpg):
        """Sets the jpg of this Output.

        Specify your jpg outputs. Usually used for thumbnails.

        :param jpg: The jpg of this Output.
        :type: list[JPGOutput]
        """

        self._jpg = jpg

    @property
    def accessibility(self):
        """Gets the accessibility of this Output.


        :return: The accessibility of this Output.
        :rtype: AccessibilityOutput
        """
        return self._accessibility

    @accessibility.setter
    def accessibility(self, accessibility):
        """Sets the accessibility of this Output.


        :param accessibility: The accessibility of this Output.
        :type: AccessibilityOutput
        """

        self._accessibility = accessibility

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
        if not isinstance(other, Output):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
