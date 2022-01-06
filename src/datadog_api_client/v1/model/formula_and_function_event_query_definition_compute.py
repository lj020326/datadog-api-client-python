# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.formula_and_function_event_aggregation import FormulaAndFunctionEventAggregation

    globals()["FormulaAndFunctionEventAggregation"] = FormulaAndFunctionEventAggregation


class FormulaAndFunctionEventQueryDefinitionCompute(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "aggregation": (FormulaAndFunctionEventAggregation,),
            "interval": (int,),
            "metric": (str,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "interval": "interval",
        "metric": "metric",
    }

    read_only_vars = {}

    def __init__(self, aggregation, *args, **kwargs):
        """FormulaAndFunctionEventQueryDefinitionCompute - a model defined in OpenAPI

        Args:
            aggregation (FormulaAndFunctionEventAggregation):

        Keyword Args:
            interval (int): [optional] A time interval in milliseconds.
            metric (str): [optional] Measurable attribute to compute.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.aggregation = aggregation

    @classmethod
    def _from_openapi_data(cls, aggregation, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(FormulaAndFunctionEventQueryDefinitionCompute, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.aggregation = aggregation
        return self
