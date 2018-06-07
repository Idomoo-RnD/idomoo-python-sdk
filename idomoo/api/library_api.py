# coding: utf-8

"""
    Idomoo API



    OpenAPI spec version: 2.0
    Contact: dev.support@idomoo.com

"""


from __future__ import absolute_import

# python 2 and python 3 compatibility library
import six

from idomoo.api_client import ApiClient


class LibraryApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_scene_library(self, body, **kwargs):
        """Create Scene Library

        Use this function to create a new Scene Library.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = client.create_scene_library(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param Body body: (required)
        :return: LibraryMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_scene_library_with_http_info(body, **kwargs)
        else:
            (data) = self.create_scene_library_with_http_info(body, **kwargs)
            return data

    def create_scene_library_with_http_info(self, body, **kwargs):
        """Create Scene Library

        Use this function to create a new Scene Library.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = client.create_scene_library_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param Body body: (required)
        :return: LibraryMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'async', '_return_http_data_only', '_preload_content', '_request_timeout']

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_scene_library" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_scene_library`")

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # Authentication setting
        auth_settings = ['Basic authentication']

        return self.api_client.call_api(
            '/libraries/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LibraryMetadata',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_scene_libraries(self, **kwargs):
        """List Scene Libraries

        This function lists all scene libraries available to the authenticated user.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = client.get_scene_libraries(async=True)
        >>> result = thread.get()

        :param async bool
        :param str fields: Choose which fields should return. `GET /libraries?fields=id,name,description`
        :param bool desc: Allow ascending and descending sorting. `GET /libraries?desc=true`
        :param int limit: Set limit of results `GET /libraries?limit=5`
        :param int offset: To get a different set of items, you can use the offset and limit parameters in the GET request’s query string  `GET /libraries?offset=5&limit=5`  Returns scenes 6…10.
        :return: LibrariesList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_scene_libraries_with_http_info(**kwargs)
        else:
            (data) = self.get_scene_libraries_with_http_info(**kwargs)
            return data

    def get_scene_libraries_with_http_info(self, **kwargs):
        """List Scene Libraries

        This function lists all scene libraries available to the authenticated user.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = client.get_scene_libraries_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str fields: Choose which fields should return. `GET /libraries?fields=id,name,description`
        :param bool desc: Allow ascending and descending sorting. `GET /libraries?desc=true`
        :param int limit: Set limit of results `GET /libraries?limit=5`
        :param int offset: To get a different set of items, you can use the offset and limit parameters in the GET request’s query string  `GET /libraries?offset=5&limit=5`  Returns scenes 6…10.
        :return: LibrariesList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields', 'desc', 'limit', 'offset', 'async', '_return_http_data_only', '_preload_content',
                      '_request_timeout']

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scene_libraries" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))
        if 'desc' in params:
            query_params.append(('desc', params['desc']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['Basic authentication']

        return self.api_client.call_api(
            '/libraries/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LibrariesList',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_scene_library(self, lib_id, **kwargs):
        """Return Specific Scene Library

        Return Specific Scene Library by specifying its library ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = client.get_scene_library(lib_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str lib_id: (required)
        :param str fields: Choose which fields should return. `GET /libraries/?fields=fps,scene_id,scene_width,scene_height`
        :return: LibraryMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_scene_library_with_http_info(lib_id, **kwargs)
        else:
            (data) = self.get_scene_library_with_http_info(lib_id, **kwargs)
            return data

    def get_scene_library_with_http_info(self, lib_id, **kwargs):
        """Return Specific Scene Library

        Return Specific Scene Library by specifying its library ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = client.get_scene_library_with_http_info(lib_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str lib_id: (required)
        :param str fields: Choose which fields should return. `GET /libraries/?fields=fps,scene_id,scene_width,scene_height`
        :return: LibraryMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['lib_id', 'fields', 'async', '_return_http_data_only', '_preload_content', '_request_timeout']

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scene_library" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'lib_id' is set
        if ('lib_id' not in params or
                params['lib_id'] is None):
            raise ValueError("Missing the required parameter `lib_id` when calling `get_scene_library`")

        collection_formats = {}

        path_params = {}
        if 'lib_id' in params:
            path_params['libId'] = params['lib_id']

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['Basic authentication']

        return self.api_client.call_api(
            '/libraries/{libId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LibraryMetadata',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_scenes_from_library(self, lib_id, **kwargs):
        """Return Scenes from Library

        Return an array of all the Scenes and their metadata held in a specific Scene Library.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = client.get_scenes_from_library(lib_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str lib_id: (required)
        :param str fields: Choose which fields should return. `GET /libraries/{libId}/scenes/?fields=id,name,description`
        :return: ScenesList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_scenes_from_library_with_http_info(lib_id, **kwargs)
        else:
            (data) = self.get_scenes_from_library_with_http_info(lib_id, **kwargs)
            return data

    def get_scenes_from_library_with_http_info(self, lib_id, **kwargs):
        """Return Scenes from Library

        Return an array of all the Scenes and their metadata held in a specific Scene Library.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = client.get_scenes_from_library_with_http_info(lib_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str lib_id: (required)
        :param str fields: Choose which fields should return. `GET /libraries/{libId}/scenes/?fields=id,name,description`
        :return: ScenesList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['lib_id', 'fields', 'async', '_return_http_data_only', '_preload_content', '_request_timeout']

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scenes_from_library" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'lib_id' is set
        if ('lib_id' not in params or
                params['lib_id'] is None):
            raise ValueError("Missing the required parameter `lib_id` when calling `get_scenes_from_library`")

        collection_formats = {}

        path_params = {}
        if 'lib_id' in params:
            path_params['libId'] = params['lib_id']

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['Basic authentication']

        return self.api_client.call_api(
            '/libraries/{libId}/scenes/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ScenesList',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
