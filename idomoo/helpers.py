#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author talm

Description:

"""
from idomoo import VideoOutput, Output, GIFOutput, JPGOutput


def MP4(height=720):
    """
      Creates an MP4 output object
      :param height:
      :type height int
      :return: Output
    """
    video_output = VideoOutput(video_type='mp4', height=height)  # set Defaults
    outputs = Output(video=[video_output])
    return outputs


def HLS(height=720):
    """
      Creates an MP4 output object
      :param height:
      :type height int
      :return: Output
    """
    video_output = VideoOutput(video_type='hls', height=height)  # set Defaults
    outputs = Output(video=[video_output])
    return outputs


def GIF(height=720):
    """
      Creates an MP4 output object
      :param height:
      :type height int
      :return: Output
    """
    video_output = GIFOutput(height=height)  # set Defaults
    outputs = Output(video=[video_output])
    return outputs


def JPG(time, height=720):
    """
      Creates an MP4 output object
      :param height:
      :type height int
      :param time:
      :type time float
      :return: Output
    """
    jpeg_output = JPGOutput(height=height, time=time)  # set Defaults
    outputs = Output(video=[jpeg_output])
    return outputs


def MP4_and_Thumbnail(time, height=720):
    """
      Creates an MP4 output object
      :param height:
      :type height int
      :param time:
      :type time float
      :return: Output
    """
    video_output = VideoOutput(video_type='mp4', height=height)  # set Defaults
    jpeg_output = JPGOutput(height=height, time=time)  # set Defaults
    outputs = Output(video=[video_output], jpg=[jpeg_output])
    return outputs
