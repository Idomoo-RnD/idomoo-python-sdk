# coding: utf-8

"""
    Idomoo API



    OpenAPI spec version: 2.0
    Contact: dev.support@idomoo.com

"""


from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six

from idomoo.api_client import ApiClient


class AccountApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_account(self, **kwargs):
        """Get Account Informaion

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_account(async=True)
        >>> result = thread.get()

        :param async bool
        :param str fields: Choose which fields should return. `GET /account/?fields=company,email`
        :return: AccountMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_account_with_http_info(**kwargs)
        else:
            (data) = self.get_account_with_http_info(**kwargs)
            return data

    def get_account_with_http_info(self, **kwargs):
        """Get Account Informaion

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_account_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str fields: Choose which fields should return. `GET /account/?fields=company,email`
        :return: AccountMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/accounts/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountMetadata',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
