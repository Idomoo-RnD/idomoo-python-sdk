# coding: utf-8

"""
    Idomoo API



    OpenAPI spec version: 2.0
    Contact: dev.support@idomoo.com

"""


import pprint
import re

import six


class GIFOutput(object):
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
        'gif_fps': 'float',
        'color_depth': 'float',
        'gif_loop': 'int',
        'height': 'float',
        'start': 'float',
        'duration': 'float',
        'suffix': 'str',
        'overlay': 'str',
        'overlay_alignment': 'list[str]',
        'overlay_scale': 'str',
        'label': 'str'
    }

    attribute_map = {
        'gif_fps': 'gif_fps',
        'color_depth': 'color_depth',
        'gif_loop': 'gif_loop',
        'height': 'height',
        'start': 'start',
        'duration': 'duration',
        'suffix': 'suffix',
        'overlay': 'overlay',
        'overlay_alignment': 'overlay_alignment',
        'overlay_scale': 'overlay_scale',
        'label': 'label'
    }

    def __init__(self, gif_fps=None, color_depth=None, gif_loop=None, height=None, start=None, duration=None, suffix=None, overlay=None, overlay_alignment=None, overlay_scale='fit', label=None):
        """GIFOutput - a model defined in Swagger"""

        self._gif_fps = None
        self._color_depth = None
        self._gif_loop = None
        self._height = None
        self._start = None
        self._duration = None
        self._suffix = None
        self._overlay = None
        self._overlay_alignment = None
        self._overlay_scale = None
        self._label = None
        self.discriminator = None

        if gif_fps is not None:
            self.gif_fps = gif_fps
        if color_depth is not None:
            self.color_depth = color_depth
        if gif_loop is not None:
            self.gif_loop = gif_loop
        self.height = height
        self.start = start
        if duration is not None:
            self.duration = duration
        if suffix is not None:
            self.suffix = suffix
        if overlay is not None:
            self.overlay = overlay
        if overlay_alignment is not None:
            self.overlay_alignment = overlay_alignment
        if overlay_scale is not None:
            self.overlay_scale = overlay_scale
        if label is not None:
            self.label = label

    @property
    def gif_fps(self):
        """Gets the gif_fps of this GIFOutput.

        The frame rate of the GIF. Default is the Video frame rate

        :return: The gif_fps of this GIFOutput.
        :rtype: float
        """
        return self._gif_fps

    @gif_fps.setter
    def gif_fps(self, gif_fps):
        """Sets the gif_fps of this GIFOutput.

        The frame rate of the GIF. Default is the Video frame rate

        :param gif_fps: The gif_fps of this GIFOutput.
        :type: float
        """
        if gif_fps is not None and gif_fps > 30:
            raise ValueError("Invalid value for `gif_fps`, must be a value less than or equal to `30`")

        self._gif_fps = gif_fps

    @property
    def color_depth(self):
        """Gets the color_depth of this GIFOutput.

        Amount of colors in palette

        :return: The color_depth of this GIFOutput.
        :rtype: float
        """
        return self._color_depth

    @color_depth.setter
    def color_depth(self, color_depth):
        """Sets the color_depth of this GIFOutput.

        Amount of colors in palette

        :param color_depth: The color_depth of this GIFOutput.
        :type: float
        """

        self._color_depth = color_depth

    @property
    def gif_loop(self):
        """Gets the gif_loop of this GIFOutput.

        If to loop the GIF. -1 is no loop, 0 is infinite loops, and other numbers are number of loops.

        :return: The gif_loop of this GIFOutput.
        :rtype: int
        """
        return self._gif_loop

    @gif_loop.setter
    def gif_loop(self, gif_loop):
        """Sets the gif_loop of this GIFOutput.

        If to loop the GIF. -1 is no loop, 0 is infinite loops, and other numbers are number of loops.

        :param gif_loop: The gif_loop of this GIFOutput.
        :type: int
        """
        if gif_loop is not None and gif_loop < -1:
            raise ValueError("Invalid value for `gif_loop`, must be a value greater than or equal to `-1`")

        self._gif_loop = gif_loop

    @property
    def height(self):
        """Gets the height of this GIFOutput.

        Height of the media to be rendered, in pixels. Should be the height of your scenes unless a smaller resolution is needed. Resolution higher than the scene resolution reduces quality. The width is automatically calculated to keep the aspect ratio.

        :return: The height of this GIFOutput.
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this GIFOutput.

        Height of the media to be rendered, in pixels. Should be the height of your scenes unless a smaller resolution is needed. Resolution higher than the scene resolution reduces quality. The width is automatically calculated to keep the aspect ratio.

        :param height: The height of this GIFOutput.
        :type: float
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")

        self._height = height

    @property
    def start(self):
        """Gets the start of this GIFOutput.

        What second of the storyboard timeline to start the GIF.

        :return: The start of this GIFOutput.
        :rtype: float
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this GIFOutput.

        What second of the storyboard timeline to start the GIF.

        :param start: The start of this GIFOutput.
        :type: float
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")

        self._start = start

    @property
    def duration(self):
        """Gets the duration of this GIFOutput.

        Seconds for the duration of the GIF. Can't be longer than the video.

        :return: The duration of this GIFOutput.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this GIFOutput.

        Seconds for the duration of the GIF. Can't be longer than the video.

        :param duration: The duration of this GIFOutput.
        :type: float
        """

        self._duration = duration

    @property
    def suffix(self):
        """Gets the suffix of this GIFOutput.

        Unique ending of the file name so several outputs can be created then identified. Required if there is more then 1 video output.

        :return: The suffix of this GIFOutput.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """Sets the suffix of this GIFOutput.

        Unique ending of the file name so several outputs can be created then identified. Required if there is more then 1 video output.

        :param suffix: The suffix of this GIFOutput.
        :type: str
        """

        self._suffix = suffix

    @property
    def overlay(self):
        """Gets the overlay of this GIFOutput.

        Path to overlay image, such as: play button or watermark.

        :return: The overlay of this GIFOutput.
        :rtype: str
        """
        return self._overlay

    @overlay.setter
    def overlay(self, overlay):
        """Sets the overlay of this GIFOutput.

        Path to overlay image, such as: play button or watermark.

        :param overlay: The overlay of this GIFOutput.
        :type: str
        """

        self._overlay = overlay

    @property
    def overlay_alignment(self):
        """Gets the overlay_alignment of this GIFOutput.

        Alignment for overlay image in case the image doesn't fit the video perfectly. The first item in the array is X. The second is Y.

        :return: The overlay_alignment of this GIFOutput.
        :rtype: list[str]
        """
        return self._overlay_alignment

    @overlay_alignment.setter
    def overlay_alignment(self, overlay_alignment):
        """Sets the overlay_alignment of this GIFOutput.

        Alignment for overlay image in case the image doesn't fit the video perfectly. The first item in the array is X. The second is Y.

        :param overlay_alignment: The overlay_alignment of this GIFOutput.
        :type: list[str]
        """
        allowed_values = ["left", "center", "right", "top", "middle", "bottom"]
        if not set(overlay_alignment).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `overlay_alignment` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(overlay_alignment) - set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._overlay_alignment = overlay_alignment

    @property
    def overlay_scale(self):
        """Gets the overlay_scale of this GIFOutput.

        Scale the overlay image if it's not the same size as the video. * Fit: scale the image up or down so it's completely visible in the video's resolution. If not the same aspect ratio, transparency is added around the image according to the alignment settings. * Fill: scale the image up or down so it completely fills the video. If not the same aspect ratio, the image is cropped according to the alignment settings.  * None: don't resize the overlay image.

        :return: The overlay_scale of this GIFOutput.
        :rtype: str
        """
        return self._overlay_scale

    @overlay_scale.setter
    def overlay_scale(self, overlay_scale):
        """Sets the overlay_scale of this GIFOutput.

        Scale the overlay image if it's not the same size as the video. * Fit: scale the image up or down so it's completely visible in the video's resolution. If not the same aspect ratio, transparency is added around the image according to the alignment settings. * Fill: scale the image up or down so it completely fills the video. If not the same aspect ratio, the image is cropped according to the alignment settings.  * None: don't resize the overlay image.

        :param overlay_scale: The overlay_scale of this GIFOutput.
        :type: str
        """
        allowed_values = ["fit", "fill", "none"]
        if overlay_scale not in allowed_values:
            raise ValueError(
                "Invalid value for `overlay_scale` ({0}), must be one of {1}"
                .format(overlay_scale, allowed_values)
            )

        self._overlay_scale = overlay_scale

    @property
    def label(self):
        """Gets the label of this GIFOutput.

        This label is another way to identify this specific output. The label is returned in the response, but does not appear in the file name.

        :return: The label of this GIFOutput.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this GIFOutput.

        This label is another way to identify this specific output. The label is returned in the response, but does not appear in the file name.

        :param label: The label of this GIFOutput.
        :type: str
        """

        self._label = label

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
        if not isinstance(other, GIFOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
