#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author talm

Description:

"""

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
