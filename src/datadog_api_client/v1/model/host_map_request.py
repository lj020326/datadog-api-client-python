# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.log_query_definition import LogQueryDefinition
    from datadog_api_client.v1.model.process_query_definition import ProcessQueryDefinition

    globals()["LogQueryDefinition"] = LogQueryDefinition
    globals()["ProcessQueryDefinition"] = ProcessQueryDefinition


class HostMapRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "apm_query": (LogQueryDefinition,),
            "event_query": (LogQueryDefinition,),
            "log_query": (LogQueryDefinition,),
            "network_query": (LogQueryDefinition,),
            "process_query": (ProcessQueryDefinition,),
            "profile_metrics_query": (LogQueryDefinition,),
            "q": (str,),
            "rum_query": (LogQueryDefinition,),
            "security_query": (LogQueryDefinition,),
        }

    attribute_map = {
        "apm_query": "apm_query",
        "event_query": "event_query",
        "log_query": "log_query",
        "network_query": "network_query",
        "process_query": "process_query",
        "profile_metrics_query": "profile_metrics_query",
        "q": "q",
        "rum_query": "rum_query",
        "security_query": "security_query",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """HostMapRequest - a model defined in OpenAPI

        Keyword Args:
            apm_query (LogQueryDefinition): [optional]
            event_query (LogQueryDefinition): [optional]
            log_query (LogQueryDefinition): [optional]
            network_query (LogQueryDefinition): [optional]
            process_query (ProcessQueryDefinition): [optional]
            profile_metrics_query (LogQueryDefinition): [optional]
            q (str): [optional] Query definition.
            rum_query (LogQueryDefinition): [optional]
            security_query (LogQueryDefinition): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(HostMapRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
