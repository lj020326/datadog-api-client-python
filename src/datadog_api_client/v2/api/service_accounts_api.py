# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v2.model.application_key_create_request import ApplicationKeyCreateRequest
from datadog_api_client.v2.model.application_key_response import ApplicationKeyResponse
from datadog_api_client.v2.model.application_key_update_request import ApplicationKeyUpdateRequest
from datadog_api_client.v2.model.application_keys_sort import ApplicationKeysSort
from datadog_api_client.v2.model.list_application_keys_response import ListApplicationKeysResponse
from datadog_api_client.v2.model.partial_application_key_response import PartialApplicationKeyResponse


class ServiceAccountsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_service_account_application_key_endpoint = _Endpoint(
            settings={
                "response_type": (ApplicationKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/service_accounts/{service_account_id}/application_keys",
                "operation_id": "create_service_account_application_key",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "service_account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "service_account_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ApplicationKeyCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_service_account_application_key_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}",
                "operation_id": "delete_service_account_application_key",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "service_account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "service_account_id",
                    "location": "path",
                },
                "app_key_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_key_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_service_account_application_key_endpoint = _Endpoint(
            settings={
                "response_type": (PartialApplicationKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}",
                "operation_id": "get_service_account_application_key",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "service_account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "service_account_id",
                    "location": "path",
                },
                "app_key_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_key_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_service_account_application_keys_endpoint = _Endpoint(
            settings={
                "response_type": (ListApplicationKeysResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/service_accounts/{service_account_id}/application_keys",
                "operation_id": "list_service_account_application_keys",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "service_account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "service_account_id",
                    "location": "path",
                },
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (ApplicationKeysSort,),
                    "attribute": "sort",
                    "location": "query",
                },
                "filter": {
                    "openapi_types": (str,),
                    "attribute": "filter",
                    "location": "query",
                },
                "filter_created_at_start": {
                    "openapi_types": (str,),
                    "attribute": "filter[created_at][start]",
                    "location": "query",
                },
                "filter_created_at_end": {
                    "openapi_types": (str,),
                    "attribute": "filter[created_at][end]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_service_account_application_key_endpoint = _Endpoint(
            settings={
                "response_type": (PartialApplicationKeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/service_accounts/{service_account_id}/application_keys/{app_key_id}",
                "operation_id": "update_service_account_application_key",
                "http_method": "PATCH",
                "servers": None,
            },
            params_map={
                "service_account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "service_account_id",
                    "location": "path",
                },
                "app_key_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_key_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ApplicationKeyUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_service_account_application_key(self, service_account_id, body, **kwargs):
        """Create an application key for this service account

        Create an application key for this service account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_service_account_application_key(service_account_id, body, async_req=True)
        >>> result = thread.get()

        Args:
            service_account_id (str): The ID of the service account.
            body (ApplicationKeyCreateRequest):

        Keyword Args:
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
            ApplicationKeyResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._create_service_account_application_key_endpoint.default_arguments(kwargs)
        kwargs["service_account_id"] = service_account_id
        kwargs["body"] = body
        return self._create_service_account_application_key_endpoint.call_with_http_info(**kwargs)

    def delete_service_account_application_key(self, service_account_id, app_key_id, **kwargs):
        """Delete an application key for this service account

        Delete an application key owned by this service account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_service_account_application_key(service_account_id, app_key_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_account_id (str): The ID of the service account.
            app_key_id (str): The ID of the application key.

        Keyword Args:
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
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._delete_service_account_application_key_endpoint.default_arguments(kwargs)
        kwargs["service_account_id"] = service_account_id
        kwargs["app_key_id"] = app_key_id
        return self._delete_service_account_application_key_endpoint.call_with_http_info(**kwargs)

    def get_service_account_application_key(self, service_account_id, app_key_id, **kwargs):
        """Get one application key for this service account

        Get an application key owned by this service account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_service_account_application_key(service_account_id, app_key_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_account_id (str): The ID of the service account.
            app_key_id (str): The ID of the application key.

        Keyword Args:
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
            PartialApplicationKeyResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._get_service_account_application_key_endpoint.default_arguments(kwargs)
        kwargs["service_account_id"] = service_account_id
        kwargs["app_key_id"] = app_key_id
        return self._get_service_account_application_key_endpoint.call_with_http_info(**kwargs)

    def list_service_account_application_keys(self, service_account_id, **kwargs):
        """List application keys for this service account

        List all application keys available for this service account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_service_account_application_keys(service_account_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_account_id (str): The ID of the service account.

        Keyword Args:
            page_size (int): [optional] Size for a given page. If omitted the server will use the default value of 10.
            page_number (int): [optional] Specific page number to return. If omitted the server will use the default value of 0.
            sort (ApplicationKeysSort): [optional] Application key attribute used to sort results. Sort order is ascending by default. In order to specify a descending sort, prefix the attribute with a minus sign.
            filter (str): [optional] Filter application keys by the specified string.
            filter_created_at_start (str): [optional] Only include application keys created on or after the specified date.
            filter_created_at_end (str): [optional] Only include application keys created on or before the specified date.
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
            ListApplicationKeysResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._list_service_account_application_keys_endpoint.default_arguments(kwargs)
        kwargs["service_account_id"] = service_account_id
        return self._list_service_account_application_keys_endpoint.call_with_http_info(**kwargs)

    def update_service_account_application_key(self, service_account_id, app_key_id, body, **kwargs):
        """Edit an application key for this service account

        Edit an application key owned by this service account.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_service_account_application_key(service_account_id, app_key_id, body, async_req=True)
        >>> result = thread.get()

        Args:
            service_account_id (str): The ID of the service account.
            app_key_id (str): The ID of the application key.
            body (ApplicationKeyUpdateRequest):

        Keyword Args:
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
            PartialApplicationKeyResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._update_service_account_application_key_endpoint.default_arguments(kwargs)
        kwargs["service_account_id"] = service_account_id
        kwargs["app_key_id"] = app_key_id
        kwargs["body"] = body
        return self._update_service_account_application_key_endpoint.call_with_http_info(**kwargs)
