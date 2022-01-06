# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.apm_stats_query_definition import ApmStatsQueryDefinition
    from datadog_api_client.v1.model.formula_and_function_query_definition import FormulaAndFunctionQueryDefinition
    from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat
    from datadog_api_client.v1.model.log_query_definition import LogQueryDefinition
    from datadog_api_client.v1.model.process_query_definition import ProcessQueryDefinition
    from datadog_api_client.v1.model.table_widget_cell_display_mode import TableWidgetCellDisplayMode
    from datadog_api_client.v1.model.widget_aggregator import WidgetAggregator
    from datadog_api_client.v1.model.widget_conditional_format import WidgetConditionalFormat
    from datadog_api_client.v1.model.widget_formula import WidgetFormula
    from datadog_api_client.v1.model.widget_sort import WidgetSort

    globals()["ApmStatsQueryDefinition"] = ApmStatsQueryDefinition
    globals()["FormulaAndFunctionQueryDefinition"] = FormulaAndFunctionQueryDefinition
    globals()["FormulaAndFunctionResponseFormat"] = FormulaAndFunctionResponseFormat
    globals()["LogQueryDefinition"] = LogQueryDefinition
    globals()["ProcessQueryDefinition"] = ProcessQueryDefinition
    globals()["TableWidgetCellDisplayMode"] = TableWidgetCellDisplayMode
    globals()["WidgetAggregator"] = WidgetAggregator
    globals()["WidgetConditionalFormat"] = WidgetConditionalFormat
    globals()["WidgetFormula"] = WidgetFormula
    globals()["WidgetSort"] = WidgetSort


class TableWidgetRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "aggregator": (WidgetAggregator,),
            "alias": (str,),
            "apm_query": (LogQueryDefinition,),
            "apm_stats_query": (ApmStatsQueryDefinition,),
            "cell_display_mode": ([TableWidgetCellDisplayMode],),
            "conditional_formats": ([WidgetConditionalFormat],),
            "event_query": (LogQueryDefinition,),
            "formulas": ([WidgetFormula],),
            "limit": (int,),
            "log_query": (LogQueryDefinition,),
            "network_query": (LogQueryDefinition,),
            "order": (WidgetSort,),
            "process_query": (ProcessQueryDefinition,),
            "profile_metrics_query": (LogQueryDefinition,),
            "q": (str,),
            "queries": ([FormulaAndFunctionQueryDefinition],),
            "response_format": (FormulaAndFunctionResponseFormat,),
            "rum_query": (LogQueryDefinition,),
            "security_query": (LogQueryDefinition,),
        }

    attribute_map = {
        "aggregator": "aggregator",
        "alias": "alias",
        "apm_query": "apm_query",
        "apm_stats_query": "apm_stats_query",
        "cell_display_mode": "cell_display_mode",
        "conditional_formats": "conditional_formats",
        "event_query": "event_query",
        "formulas": "formulas",
        "limit": "limit",
        "log_query": "log_query",
        "network_query": "network_query",
        "order": "order",
        "process_query": "process_query",
        "profile_metrics_query": "profile_metrics_query",
        "q": "q",
        "queries": "queries",
        "response_format": "response_format",
        "rum_query": "rum_query",
        "security_query": "security_query",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """TableWidgetRequest - a model defined in OpenAPI

        Keyword Args:
            aggregator (WidgetAggregator): [optional]
            alias (str): [optional] The column name (defaults to the metric name).
            apm_query (LogQueryDefinition): [optional]
            apm_stats_query (ApmStatsQueryDefinition): [optional]
            cell_display_mode ([TableWidgetCellDisplayMode]): [optional] A list of display modes for each table cell.
            conditional_formats ([WidgetConditionalFormat]): [optional] List of conditional formats.
            event_query (LogQueryDefinition): [optional]
            formulas ([WidgetFormula]): [optional] List of formulas that operate on queries. **This feature is currently in beta.**
            limit (int): [optional] For metric queries, the number of lines to show in the table. Only one request should have this property.
            log_query (LogQueryDefinition): [optional]
            network_query (LogQueryDefinition): [optional]
            order (WidgetSort): [optional]
            process_query (ProcessQueryDefinition): [optional]
            profile_metrics_query (LogQueryDefinition): [optional]
            q (str): [optional] Query definition.
            queries ([FormulaAndFunctionQueryDefinition]): [optional] List of queries that can be returned directly or used in formulas. **This feature is currently in beta.**
            response_format (FormulaAndFunctionResponseFormat): [optional]
            rum_query (LogQueryDefinition): [optional]
            security_query (LogQueryDefinition): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(TableWidgetRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
