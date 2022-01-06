# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class UsageDBMHour(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "dbm_host_count": (int,),
            "dbm_queries_count": (int,),
            "hour": (datetime,),
            "org_name": (str,),
            "public_id": (str,),
        }

    attribute_map = {
        "dbm_host_count": "dbm_host_count",
        "dbm_queries_count": "dbm_queries_count",
        "hour": "hour",
        "org_name": "org_name",
        "public_id": "public_id",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """UsageDBMHour - a model defined in OpenAPI

        Keyword Args:
            dbm_host_count (int): [optional] The total number of Database Monitoring host hours from the start of the given hour’s month until the given hour.
            dbm_queries_count (int): [optional] The total number of normalized Database Monitoring queries from the start of the given hour’s month until the given hour.
            hour (datetime): [optional] The hour for the usage.
            org_name (str): [optional] The organization name.
            public_id (str): [optional] The organization public ID.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageDBMHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
