# coding: utf-8

"""
    Idomoo API



    OpenAPI spec version: 2.0
    Contact: dev.support@idomoo.com

"""

import pprint

import six

from idomoo.models.scene import Scene
from idomoo.models.soundtrack import Soundtrack


class Timeline(object):
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
        'scene_order': 'str',
        'soundtrack': 'Soundtrack',
        'scenes': 'list[Scene]'
    }

    attribute_map = {
        'scene_order': 'scene_order',
        'soundtrack': 'soundtrack',
        'scenes': 'scenes'
    }

    def __init__(self, scene_order='linear', soundtrack=None, scenes=None):
        """Timeline - a model defined in Swagger"""

        self._scene_order = None
        self._soundtrack = None
        self._scenes = None
        self.discriminator = None

        if scene_order is not None:
            self.scene_order = scene_order
        if soundtrack is not None:
            self.soundtrack = soundtrack
        self.scenes = scenes

    @property
    def scene_order(self):
        """Gets the scene_order of this Timeline.

        How to order the scene on the timeline: * Linear scene ordering simply places the scenes in the order you
        specify, one after the other. * Non-linear scene ordering leaves the start timing of each scene up to you.

        :return: The scene_order of this Timeline.
        :rtype: str
        """
        return self._scene_order

    @scene_order.setter
    def scene_order(self, scene_order):
        """Sets the scene_order of this Timeline.

        How to order the scene on the timeline: * Linear scene ordering simply places the scenes in the order you
        specify, one after the other. * Non-linear scene ordering leaves the start timing of each scene up to you.

        :param scene_order: The scene_order of this Timeline.
        :type: str
        """
        allowed_values = ["linear", "non-linear"]
        if scene_order not in allowed_values:
            raise ValueError(
                "Invalid value for `scene_order` ({0}), must be one of {1}"
                    .format(scene_order, allowed_values)
            )

        self._scene_order = scene_order

    @property
    def soundtrack(self):
        """Gets the soundtrack of this Timeline.


        :return: The soundtrack of this Timeline.
        :rtype: Soundtrack
        """
        return self._soundtrack

    @soundtrack.setter
    def soundtrack(self, soundtrack):
        """Sets the soundtrack of this Timeline.


        :param soundtrack: The soundtrack of this Timeline.
        :type: Soundtrack
        """

        self._soundtrack = soundtrack

    @property
    def scenes(self):
        """Gets the scenes of this Timeline.

        Array of scenes to render. The order matters if Scene Order is set to linear. Otherwise, there is no
        significance to order.

        :return: The scenes of this Timeline.
        :rtype: list[Scene]
        """
        return self._scenes

    @scenes.setter
    def scenes(self, scenes):
        """Sets the scenes of this Timeline.

        Array of scenes to render. The order matters if Scene Order is set to linear. Otherwise, there is no
        significance to order.

        :param scenes: The scenes of this Timeline.
        :type: list[Scene]
        """
        if scenes is None:
            scenes = list()

        self._scenes = scenes

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
        if not isinstance(other, Timeline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
