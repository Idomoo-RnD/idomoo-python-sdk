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
from idomoo.models.text_properties import TextProperties


class Text(object):
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
        'key': 'str',
        'val': 'list[TextProperties]',
        'asset_path': 'str',
        'font_size': 'float',
        'text_color': 'str',
        'alignment': 'list[str]',
        'wrapping_shrink': 'bool',
        'wrapping_breakline': 'bool',
        'wrapping_minimum': 'int',
        'wrapping_truncate': 'bool',
        'wrapping_truncate_string': 'str',
        'right_to_left': 'bool',
        'vertical': 'bool',
        'is_hidden': 'bool'
    }

    attribute_map = {
        'key': 'key',
        'val': 'val',
        'asset_path': 'asset_path',
        'font_size': 'font_size',
        'text_color': 'text_color',
        'alignment': 'alignment',
        'wrapping_shrink': 'wrapping_shrink',
        'wrapping_breakline': 'wrapping_breakline',
        'wrapping_minimum': 'wrapping_minimum',
        'wrapping_truncate': 'wrapping_truncate',
        'wrapping_truncate_string': 'wrapping_truncate_string',
        'right_to_left': 'right_to_left',
        'vertical': 'vertical',
        'is_hidden': 'is_hidden'
    }

    def __init__(self, key=None, val=None, asset_path=None, font_size=None, text_color=None, alignment=None,
                 wrapping_shrink=None, wrapping_breakline=None, wrapping_minimum=None, wrapping_truncate=False,
                 wrapping_truncate_string='…', right_to_left=False, vertical=False, is_hidden=False):
        """Text - a model defined in Swagger"""

        self._key = None
        self._val = None
        self._asset_path = None
        self._font_size = None
        self._text_color = None
        self._alignment = None
        self._wrapping_shrink = None
        self._wrapping_breakline = None
        self._wrapping_minimum = None
        self._wrapping_truncate = None
        self._wrapping_truncate_string = None
        self._right_to_left = None
        self._vertical = None
        self._is_hidden = None
        self.discriminator = None

        self.key = key
        self.val = val
        if asset_path is not None:
            self.asset_path = asset_path
        if font_size is not None:
            self.font_size = font_size
        if text_color is not None:
            self.text_color = text_color
        if alignment is not None:
            self.alignment = alignment
        if wrapping_shrink is not None:
            self.wrapping_shrink = wrapping_shrink
        if wrapping_breakline is not None:
            self.wrapping_breakline = wrapping_breakline
        if wrapping_minimum is not None:
            self.wrapping_minimum = wrapping_minimum
        if wrapping_truncate is not None:
            self.wrapping_truncate = wrapping_truncate
        if wrapping_truncate_string is not None:
            self.wrapping_truncate_string = wrapping_truncate_string
        if right_to_left is not None:
            self.right_to_left = right_to_left
        if vertical is not None:
            self.vertical = vertical
        if is_hidden is not None:
            self.is_hidden = is_hidden

    @property
    def key(self):
        """Gets the key of this Text.

        Name of placeholder from After Effects as it appears in the scene.

        :return: The key of this Text.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Text.

        Name of placeholder from After Effects as it appears in the scene.

        :param key: The key of this Text.
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def val(self):
        """Gets the val of this Text.


        :return: The val of this Text.
        :rtype: list[TextProperties]
        """
        return self._val

    @val.setter
    def val(self, val):
        """Sets the val of this Text.


        :param val: The val of this Text.
        :type: list[TextProperties]
        """
        if val is None:
            val = list()

        self._val = val

    @property
    def asset_path(self):
        """Gets the asset_path of this Text.

        Path to the default font to use. This can be overwritten in `Text Properties`. However this is the font to be
        used for calculating the location of the baseline.  The default font is the one packaged with the scene.

        :return: The asset_path of this Text.
        :rtype: str
        """
        return self._asset_path

    @asset_path.setter
    def asset_path(self, asset_path):
        """Sets the asset_path of this Text.

        Path to the default font to use. This can be overwritten in `Text Properties`. However this is the font to be
        used for calculating the location of the baseline.  The default font is the one packaged with the scene.

        :param asset_path: The asset_path of this Text.
        :type: str
        """
        # if asset_path is not None and not re.search(utils.VALID_ASSET_PATH_REGEX, asset_path):
        #     raise ValueError("Invalid value for `asset_path`, must be a follow pattern or equal to `%s`"
        #                      % utils.VALID_ASSET_PATH_REGEX)

        self._asset_path = asset_path

    @property
    def font_size(self):
        """Gets the font_size of this Text.

        Size of text in pixels. Default is the size of the text packaged with the scene.

        :return: The font_size of this Text.
        :rtype: float
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """Sets the font_size of this Text.

        Size of text in pixels. Default is the size of the text packaged with the scene.

        :param font_size: The font_size of this Text.
        :type: float
        """

        self._font_size = font_size

    @property
    def text_color(self):
        """Gets the text_color of this Text.

        The color of the text. This can be overwritten by `Text Properties`. Default is the color of the text packaged with the scene.  Use this syntax: `\"rgb(###, ###, ###)\"`. Use 8bit color ranging from `0-255`.

        :return: The text_color of this Text.
        :rtype: str
        """
        return self._text_color

    @text_color.setter
    def text_color(self, text_color):
        """Sets the text_color of this Text.

        The color of the text. This can be overwritten by `Text Properties`. Default is the color of the text
        packaged with the scene.  Use this syntax: `\"rgb(###, ###, ###)\"`. Use 8bit color ranging from `0-255`.

        :param text_color: The text_color of this Text.
        :type: str
        """
        if text_color is not None and not re.search(utils.VALID_COLOR_REGEX, text_color):
            raise ValueError("Invalid value for `text_color`, must be a follow pattern or equal to `%s`" % utils.VALID_COLOR_REGEX)

        self._text_color = text_color

    @property
    def alignment(self):
        """Gets the alignment of this Text.

        How to align the text in the bounding box. The first item in the array is X. The second is Y.  X defaults to
        what was packaged in the scene. Y defaults to top for placeholders generated with After Effects paragraph
        text layers, and bottom for placeholders generated with After Effects point text layers.

        :return: The alignment of this Text.
        :rtype: list[str]
        """
        return self._alignment

    @alignment.setter
    def alignment(self, alignment):
        """Sets the alignment of this Text.

        How to align the text in the bounding box. The first item in the array is X. The second is Y.  X defaults to
        what was packaged in the scene. Y defaults to top for placeholders generated with After Effects paragraph
        text layers, and bottom for placeholders generated with After Effects point text layers.

        :param alignment: The alignment of this Text.
        :type: list[str]
        """
        allowed_values = ["left", "center", "right", "top", "middle", "bottom"]
        if not set(alignment).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `alignment` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(alignment) - set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._alignment = alignment

    @property
    def wrapping_shrink(self):
        """Gets the wrapping_shrink of this Text.

        If `\"wrapping_breakline\"` is false, this shrinks the font size when the width of the bounding box is
        reached.  If `\"wrapping_brealline\"` is true, this shrinks the font size when the height of the bounding box
        is reached.  The default depends on the type of text layer used in After Effects: * For point text layers:
        `\"true\"`. * For paragraph text layers: `\"false\"`.

        :return: The wrapping_shrink of this Text.
        :rtype: bool
        """
        return self._wrapping_shrink

    @wrapping_shrink.setter
    def wrapping_shrink(self, wrapping_shrink):
        """Sets the wrapping_shrink of this Text.

        If `\"wrapping_breakline\"` is false, this shrinks the font size when the width of the bounding box is
        reached.  If `\"wrapping_brealline\"` is true, this shrinks the font size when the height of the bounding box
        is reached.  The default depends on the type of text layer used in After Effects: * For point text layers:
        `\"true\"`. * For paragraph text layers: `\"false\"`.

        :param wrapping_shrink: The wrapping_shrink of this Text.
        :type: bool
        """

        self._wrapping_shrink = wrapping_shrink

    @property
    def wrapping_breakline(self):
        """Gets the wrapping_breakline of this Text.

        The text automatically breaks into more lines when the width of the bounding box is reached. Newline
        characters in the text are still used.  The default depends on the type of text layer used in After Effects:
        * For point text layers: `\"false\"`. * For paragraph text layers: `\"true\"`.

        :return: The wrapping_breakline of this Text.
        :rtype: bool
        """
        return self._wrapping_breakline

    @wrapping_breakline.setter
    def wrapping_breakline(self, wrapping_breakline):
        """Sets the wrapping_breakline of this Text.

        The text automatically breaks into more lines when the width of the bounding box is reached. Newline
        characters in the text are still used.  The default depends on the type of text layer used in After Effects:
        * For point text layers: `\"false\"`. * For paragraph text layers: `\"true\"`.

        :param wrapping_breakline: The wrapping_breakline of this Text.
        :type: bool
        """

        self._wrapping_breakline = wrapping_breakline

    @property
    def wrapping_minimum(self):
        """Gets the wrapping_minimum of this Text.

        Used with `\"wrapping_shrink\"`. The text will not drop below this number.

        :return: The wrapping_minimum of this Text.
        :rtype: int
        """
        return self._wrapping_minimum

    @wrapping_minimum.setter
    def wrapping_minimum(self, wrapping_minimum):
        """Sets the wrapping_minimum of this Text.

        Used with `\"wrapping_shrink\"`. The text will not drop below this number.

        :param wrapping_minimum: The wrapping_minimum of this Text.
        :type: int
        """

        self._wrapping_minimum = wrapping_minimum

    @property
    def wrapping_truncate(self):
        """Gets the wrapping_truncate of this Text.

        Text can be drawn outside the bounding box. With this parameter true, the text is truncated at the last
        whitespace inside the bounding box and replaced with `\"wrapping_truncate_string\"`. The default string is an
        ellipsis (…).

        :return: The wrapping_truncate of this Text.
        :rtype: bool
        """
        return self._wrapping_truncate

    @wrapping_truncate.setter
    def wrapping_truncate(self, wrapping_truncate):
        """Sets the wrapping_truncate of this Text.

        Text can be drawn outside the bounding box. With this parameter true, the text is truncated at the last
        whitespace inside the bounding box and replaced with `\"wrapping_truncate_string\"`. The default string is an
        ellipsis (…).

        :param wrapping_truncate: The wrapping_truncate of this Text.
        :type: bool
        """

        self._wrapping_truncate = wrapping_truncate

    @property
    def wrapping_truncate_string(self):
        """Gets the wrapping_truncate_string of this Text.

        When truncating a string using `\"wrapping_truncate\"`, replace the last visible whitespace with this string.

        :return: The wrapping_truncate_string of this Text.
        :rtype: str
        """
        return self._wrapping_truncate_string

    @wrapping_truncate_string.setter
    def wrapping_truncate_string(self, wrapping_truncate_string):
        """Sets the wrapping_truncate_string of this Text.

        When truncating a string using `\"wrapping_truncate\"`, replace the last visible whitespace with this string.

        :param wrapping_truncate_string: The wrapping_truncate_string of this Text.
        :type: str
        """

        self._wrapping_truncate_string = wrapping_truncate_string

    @property
    def right_to_left(self):
        """Gets the right_to_left of this Text.

        When true, the paragraph is to run from right to left. This is to support right to left languages such as
        Arabic and Hebrew.

        :return: The right_to_left of this Text.
        :rtype: bool
        """
        return self._right_to_left

    @right_to_left.setter
    def right_to_left(self, right_to_left):
        """Sets the right_to_left of this Text.

        When true, the paragraph is to run from right to left. This is to support right to left languages such as
        Arabic and Hebrew.

        :param right_to_left: The right_to_left of this Text.
        :type: bool
        """

        self._right_to_left = right_to_left

    @property
    def vertical(self):
        """Gets the vertical of this Text.

        Denoted the text to run from top to bottom.

        :return: The vertical of this Text.
        :rtype: bool
        """
        return self._vertical

    @vertical.setter
    def vertical(self, vertical):
        """Sets the vertical of this Text.

        Denoted the text to run from top to bottom.

        :param vertical: The vertical of this Text.
        :type: bool
        """

        self._vertical = vertical

    @property
    def is_hidden(self):
        """Gets the is_hidden of this Text.

        Hide a placeholder so it’s not processed and shown by using this parameter.

        :return: The is_hidden of this Text.
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """Sets the is_hidden of this Text.

        Hide a placeholder so it’s not processed and shown by using this parameter.

        :param is_hidden: The is_hidden of this Text.
        :type: bool
        """

        self._is_hidden = is_hidden

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
        if not isinstance(other, Text):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
