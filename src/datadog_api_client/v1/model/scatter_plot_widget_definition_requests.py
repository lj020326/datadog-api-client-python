# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.scatter_plot_request import ScatterPlotRequest
    from datadog_api_client.v1.model.scatterplot_table_request import ScatterplotTableRequest

    globals()["ScatterPlotRequest"] = ScatterPlotRequest
    globals()["ScatterplotTableRequest"] = ScatterplotTableRequest


class ScatterPlotWidgetDefinitionRequests(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "table": (ScatterplotTableRequest,),
            "x": (ScatterPlotRequest,),
            "y": (ScatterPlotRequest,),
        }

    attribute_map = {
        "table": "table",
        "x": "x",
        "y": "y",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """ScatterPlotWidgetDefinitionRequests - a model defined in OpenAPI

        Keyword Args:
            table (ScatterplotTableRequest): [optional]
            x (ScatterPlotRequest): [optional]
            y (ScatterPlotRequest): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ScatterPlotWidgetDefinitionRequests, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
