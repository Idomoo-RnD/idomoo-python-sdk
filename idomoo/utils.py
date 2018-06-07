#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author talm

Description:

"""

VALID_COLOR_REGEX = '^rgb\\(\s*(\\d{1,3})\s*,\s*(\\d{1,3})\s*,\s*(\\d{1,3})\s*\\)'
VALID_ASSET_PATH_REGEX = '^(http|ual|pal)'
VALID_MEDIA_ASSET_PATH_REGEX = '^(http|ual|pal|rgb\\(\s*(\\d{1,3})\s*,\s*(\\d{1,3})\s*,\s*(\\d{1,3})\s*\\))'
VALID_VIDEO_NAME_REGEX = '^[A-Za-z0-9_]+$'


def remove_nulls(d):
    """
    remove nulls from dict
    :param d:
    :return:
    """
    return {k: v for k, v in d.items() if v is not None}


def merge_dict(data, *override):
    """
    Merges any number of dictionaries together, and returns a single dictionary
    """
    result = {}
    for current_dict in (data,) + override:
        result.update(current_dict)
    return result
