# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import re  # noqa: F401
import sys  # noqa: F401

from datadog_api_client.v1.api_client import ApiClient, Endpoint
from datadog_api_client.v1.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from datadog_api_client.v1.model.api_error_response import APIErrorResponse
from datadog_api_client.v1.model.graph_snapshot import GraphSnapshot


class SnapshotsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_graph_snapshot(
            self,
            start,
            end,
            **kwargs
        ):
            """Take graph snapshots  # noqa: E501

            Take graph snapshots. **Note**: When a snapshot is created, there is some delay before it is available.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_graph_snapshot(start, end, async_req=True)
            >>> result = thread.get()

            Args:
                start (int): The POSIX timestamp of the start of the query.
                end (int): The POSIX timestamp of the end of the query.

            Keyword Args:
                metric_query (str): The metric query.. [optional]
                event_query (str): A query that adds event bands to the graph.. [optional]
                graph_def (str): A JSON document defining the graph. &#x60;graph_def&#x60; can be used instead of &#x60;metric_query&#x60;. The JSON document uses the [grammar defined here](https://docs.datadoghq.com/graphing/graphing_json/#grammar) and should be formatted to a single line then URL encoded.. [optional]
                title (str): A title for the graph. If no title is specified, the graph does not have a title.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                GraphSnapshot
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['start'] = \
                start
            kwargs['end'] = \
                end
            return self.call_with_http_info(**kwargs)

        self.get_graph_snapshot = Endpoint(
            settings={
                'response_type': (GraphSnapshot,),
                'auth': [
                    'apiKeyAuth',
                    'appKeyAuth'
                ],
                'endpoint_path': '/api/v1/graph/snapshot',
                'operation_id': 'get_graph_snapshot',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'start',
                    'end',
                    'metric_query',
                    'event_query',
                    'graph_def',
                    'title',
                ],
                'required': [
                    'start',
                    'end',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'start':
                        (int,),
                    'end':
                        (int,),
                    'metric_query':
                        (str,),
                    'event_query':
                        (str,),
                    'graph_def':
                        (str,),
                    'title':
                        (str,),
                },
                'attribute_map': {
                    'start': 'start',
                    'end': 'end',
                    'metric_query': 'metric_query',
                    'event_query': 'event_query',
                    'graph_def': 'graph_def',
                    'title': 'title',
                },
                'location_map': {
                    'start': 'query',
                    'end': 'query',
                    'metric_query': 'query',
                    'event_query': 'query',
                    'graph_def': 'query',
                    'title': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_graph_snapshot
        )
