# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.security_filter_exclusion_filter import SecurityFilterExclusionFilter
    from datadog_api_client.v2.model.security_filter_filtered_data_type import SecurityFilterFilteredDataType

    globals()["SecurityFilterExclusionFilter"] = SecurityFilterExclusionFilter
    globals()["SecurityFilterFilteredDataType"] = SecurityFilterFilteredDataType


class SecurityFilterCreateAttributes(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "exclusion_filters": ([SecurityFilterExclusionFilter],),
            "filtered_data_type": (SecurityFilterFilteredDataType,),
            "is_enabled": (bool,),
            "name": (str,),
            "query": (str,),
        }

    attribute_map = {
        "exclusion_filters": "exclusion_filters",
        "filtered_data_type": "filtered_data_type",
        "is_enabled": "is_enabled",
        "name": "name",
        "query": "query",
    }

    read_only_vars = {}

    def __init__(self, exclusion_filters, filtered_data_type, is_enabled, name, query, *args, **kwargs):
        """SecurityFilterCreateAttributes - a model defined in OpenAPI

        Args:
            exclusion_filters ([SecurityFilterExclusionFilter]): Exclusion filters to exclude some logs from the security filter.
            filtered_data_type (SecurityFilterFilteredDataType):
            is_enabled (bool): Whether the security filter is enabled.
            name (str): The name of the security filter.
            query (str): The query of the security filter.

        Keyword Args:
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.exclusion_filters = exclusion_filters
        self.filtered_data_type = filtered_data_type
        self.is_enabled = is_enabled
        self.name = name
        self.query = query

    @classmethod
    def _from_openapi_data(cls, exclusion_filters, filtered_data_type, is_enabled, name, query, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityFilterCreateAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.exclusion_filters = exclusion_filters
        self.filtered_data_type = filtered_data_type
        self.is_enabled = is_enabled
        self.name = name
        self.query = query
        return self
