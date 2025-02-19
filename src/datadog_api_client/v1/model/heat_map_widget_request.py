# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.log_query_definition import LogQueryDefinition
    from datadog_api_client.v1.model.event_query_definition import EventQueryDefinition
    from datadog_api_client.v1.model.process_query_definition import ProcessQueryDefinition
    from datadog_api_client.v1.model.widget_style import WidgetStyle


class HeatMapWidgetRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.log_query_definition import LogQueryDefinition
        from datadog_api_client.v1.model.event_query_definition import EventQueryDefinition
        from datadog_api_client.v1.model.process_query_definition import ProcessQueryDefinition
        from datadog_api_client.v1.model.widget_style import WidgetStyle

        return {
            "apm_query": (LogQueryDefinition,),
            "event_query": (EventQueryDefinition,),
            "log_query": (LogQueryDefinition,),
            "network_query": (LogQueryDefinition,),
            "process_query": (ProcessQueryDefinition,),
            "profile_metrics_query": (LogQueryDefinition,),
            "q": (str,),
            "rum_query": (LogQueryDefinition,),
            "security_query": (LogQueryDefinition,),
            "style": (WidgetStyle,),
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
        "style": "style",
    }

    def __init__(
        self_,
        apm_query: Union[LogQueryDefinition, UnsetType] = unset,
        event_query: Union[EventQueryDefinition, UnsetType] = unset,
        log_query: Union[LogQueryDefinition, UnsetType] = unset,
        network_query: Union[LogQueryDefinition, UnsetType] = unset,
        process_query: Union[ProcessQueryDefinition, UnsetType] = unset,
        profile_metrics_query: Union[LogQueryDefinition, UnsetType] = unset,
        q: Union[str, UnsetType] = unset,
        rum_query: Union[LogQueryDefinition, UnsetType] = unset,
        security_query: Union[LogQueryDefinition, UnsetType] = unset,
        style: Union[WidgetStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Updated heat map widget.

        :param apm_query: The log query.
        :type apm_query: LogQueryDefinition, optional

        :param event_query: The event query.
        :type event_query: EventQueryDefinition, optional

        :param log_query: The log query.
        :type log_query: LogQueryDefinition, optional

        :param network_query: The log query.
        :type network_query: LogQueryDefinition, optional

        :param process_query: The process query to use in the widget.
        :type process_query: ProcessQueryDefinition, optional

        :param profile_metrics_query: The log query.
        :type profile_metrics_query: LogQueryDefinition, optional

        :param q: Widget query.
        :type q: str, optional

        :param rum_query: The log query.
        :type rum_query: LogQueryDefinition, optional

        :param security_query: The log query.
        :type security_query: LogQueryDefinition, optional

        :param style: Widget style definition.
        :type style: WidgetStyle, optional
        """
        if apm_query is not unset:
            kwargs["apm_query"] = apm_query
        if event_query is not unset:
            kwargs["event_query"] = event_query
        if log_query is not unset:
            kwargs["log_query"] = log_query
        if network_query is not unset:
            kwargs["network_query"] = network_query
        if process_query is not unset:
            kwargs["process_query"] = process_query
        if profile_metrics_query is not unset:
            kwargs["profile_metrics_query"] = profile_metrics_query
        if q is not unset:
            kwargs["q"] = q
        if rum_query is not unset:
            kwargs["rum_query"] = rum_query
        if security_query is not unset:
            kwargs["security_query"] = security_query
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)
