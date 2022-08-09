# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class AlertGraphWidgetDefinitionType(ModelSimple):
    """
    Type of the alert graph widget.

    :param value: If omitted defaults to "alert_graph". Must be one of ["alert_graph"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "ALERT_GRAPH": "alert_graph",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
