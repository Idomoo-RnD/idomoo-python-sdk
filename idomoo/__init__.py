# coding: utf-8

# flake8: noqa

"""
    Idomoo API

    OpenAPI spec version: 2.0
    Contact: dev.support@idomoo.com

"""

from __future__ import absolute_import

# import apis into sdk package
from idomoo.api.account_api import AccountApi
from idomoo.api.library_api import LibraryApi
from idomoo.api.scene_api import SceneApi
from idomoo.api.storyboard_api import StoryboardApi

# import ApiClient
from idomoo.api_client import ApiClient
from idomoo.configuration import Configuration

# import models into sdk package
from idomoo.models.accessibility_output import AccessibilityOutput
from idomoo.models.accessibility_response import AccessibilityResponse
from idomoo.models.accessibility_response_caption_links import AccessibilityResponseCaptionLinks
from idomoo.models.accessibility_response_transcript_links import AccessibilityResponseTranscriptLinks
from idomoo.models.account_metadata import AccountMetadata
from idomoo.models.audio import Audio
from idomoo.models.body import Body
from idomoo.models.error import Error
from idomoo.models.error_response import ErrorResponse
from idomoo.models.gif_output import GIFOutput
from idomoo.models.generation_response import GenerationResponse
from idomoo.models.gif_output_response import GifOutputResponse
from idomoo.models.gif_output_response_links import GifOutputResponseLinks
from idomoo.models.jpg_output import JPGOutput
from idomoo.models.jpg_output_response import JPGOutputResponse
from idomoo.models.libraries_list import LibrariesList
from idomoo.models.library_metadata import LibraryMetadata
from idomoo.models.media import Media
from idomoo.models.output import Output
from idomoo.models.output_response import OutputResponse
from idomoo.models.scene import Scene
from idomoo.models.scene_api_request import SceneAPIRequest
from idomoo.models.scene_metadata import SceneMetadata
from idomoo.models.scene_metadata_audio import SceneMetadataAudio
from idomoo.models.scene_metadata_media import SceneMetadataMedia
from idomoo.models.scene_metadata_text import SceneMetadataText
from idomoo.models.scene_metadata_val import SceneMetadataVal
from idomoo.models.scenes_list import ScenesList
from idomoo.models.soundtrack import Soundtrack
from idomoo.models.storyboard_api_request import StoryboardAPIRequest
from idomoo.models.storyboard_data import StoryboardData
from idomoo.models.storyboard_list import StoryboardList
from idomoo.models.storyboard_metadata import StoryboardMetadata
from idomoo.models.storyboard_metadata_data import StoryboardMetadataData
from idomoo.models.text import Text
from idomoo.models.text_properties import TextProperties
from idomoo.models.timeline import Timeline
from idomoo.models.upload_scene import UploadScene
from idomoo.models.video_output import VideoOutput
from idomoo.models.video_output_response import VideoOutputResponse
from idomoo.models.video_output_response_links import VideoOutputResponseLinks


class IdomooClient(ApiClient):
    def __init__(self, host=None, region=None, configuration=None, header_name=None, header_value=None, cookie=None, **kwargs):
        """

        :param host: SCHEME://HOST[":"PORT][BASE PATH]
        :param header_name:
        :param header_value:
        :param cookie:
        """
        super(IdomooClient, self).__init__(host=host, region=region, configuration=configuration, header_name=header_name,
                                          header_value=header_value, cookie=cookie, **kwargs)
        self.accounts = AccountApi(api_client=self)
        self.libraries = LibraryApi(api_client=self)
        self.scenes = SceneApi(api_client=self)
        self.storyboards = StoryboardApi(api_client=self)
