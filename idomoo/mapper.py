#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author talm

Description:
This module has utility functions to deserialize json to Idomoo's models

"""
import datetime
import json
import os
import re
import tempfile

import six

from idomoo import models

PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
NATIVE_TYPES_MAPPING = {
    'int': int,
    'long': int if six.PY3 else long,  # noqa: F821
    'float': float,
    'str': str,
    'bool': bool,
    'date': datetime.date,
    'datetime': datetime.datetime,
    'object': object,
}


class ApiException(Exception):

    def __init__(self, status=None, reason=None, http_resp=None):
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n" \
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message

    def error_response(self):
        return deserialize(self.body, 'ErrorResponse')


def deserialize(response, response_type):
    """Deserializes response into an object.

    :param response: RESTResponse object to be deserialized.
    :param response_type: class literal for
        deserialized object, or string of class name.

    :return: deserialized object.
    """

    # handle file downloading
    # save response body into a tmp file and return the instance
    if response_type == "file":
        return __deserialize_file(response)

    # handle file downloading
    # save response body into a tmp file and return the instance
    try:
        data = json.loads(response.data)
    except ValueError:
        data = response.data

    return __deserialize(data, response_type)


def __deserialize(data, klass):
    """Deserializes dict, list, str into an object.

    :param data: dict, list or str.
    :param klass: class literal, or string of class name.

    :return: object.
    """
    if data is None:
        return None

    if type(klass) == str:
        if klass.startswith('list['):
            sub_kls = re.match('list\[(.*)\]', klass).group(1)
            return [__deserialize(sub_data, sub_kls)
                    for sub_data in data]

        if klass.startswith('dict('):
            sub_kls = re.match('dict\(([^,]*), (.*)\)', klass).group(2)
            return {k: __deserialize(v, sub_kls)
                    for k, v in six.iteritems(data)}

        # convert str to class
        if klass in NATIVE_TYPES_MAPPING:
            klass = NATIVE_TYPES_MAPPING[klass]
        else:
            klass = getattr(models, klass)

    if klass in PRIMITIVE_TYPES:
        return __deserialize_primitive(data, klass)
    elif klass == object:
        return __deserialize_object(data)
    elif klass == datetime.date:
        return __deserialize_date(data)
    elif klass == datetime.datetime:
        return __deserialize_datatime(data)
    else:
        return __deserialize_model(data, klass)


def __deserialize_file(response):
    """Deserializes body to file

    Saves response body into a file in a temporary folder,
    using the filename from the `Content-Disposition` header if provided.

    :param response:  RESTResponse.
    :return: file path.
    """
    fd, path = tempfile.mkstemp(dir=response.temp_folder_path)
    os.close(fd)
    os.remove(path)

    content_disposition = response.getheader("Content-Disposition")
    if content_disposition:
        filename = re.search(r'filename=[\'"]?([^\'"\s]+)[\'"]?',
                             content_disposition).group(1)
        path = os.path.join(os.path.dirname(path), filename)

    with open(path, "wb") as f:
        f.write(response.data)

    return path


def __deserialize_primitive(data, klass):
    """Deserializes string to primitive type.

    :param data: str.
    :param klass: class literal.

    :return: int, long, float, str, bool.
    """
    try:
        return klass(data)
    except UnicodeEncodeError:
        return six.u(data)
    except TypeError:
        return data


def __deserialize_object(value):
    """Return a original value.

    :return: object.
    """
    return value


def __deserialize_date(string):
    """Deserializes string to date.

    :param string: str.
    :return: date.
    """
    try:
        from dateutil.parser import parse
        return parse(string).date()
    except ImportError:
        return string
    except ValueError:
        raise ApiException(
            status=0,
            reason="Failed to parse `{0}` as date object".format(string)
        )


def __deserialize_datatime(string):
    """Deserializes string to datetime.

    The string should be in iso8601 datetime format.

    :param string: str.
    :return: datetime.
    """
    try:
        from dateutil.parser import parse
        return parse(string)
    except ImportError:
        return string
    except ValueError:
        raise ApiException(
            status=0,
            reason=(
                "Failed to parse `{0}` as datetime object".format(string)
            )
        )


def __deserialize_model(data, klass):
    """Deserializes list or dict to model.

    :param data: dict, list.
    :param klass: class literal.
    :return: model object.
    """

    if not klass.swagger_types and not hasattr(klass, 'get_real_child_model'):
        return data

    kwargs = {}
    if klass.swagger_types is not None:
        for attr, attr_type in six.iteritems(klass.swagger_types):
            if (data is not None and
                    klass.attribute_map[attr] in data and
                    isinstance(data, (list, dict))):
                value = data[klass.attribute_map[attr]]
                kwargs[attr] = __deserialize(value, attr_type)

    instance = klass(**kwargs)

    if hasattr(instance, 'get_real_child_model'):
        klass_name = instance.get_real_child_model(data)
        if klass_name:
            instance = __deserialize(data, klass_name)
    return instance
