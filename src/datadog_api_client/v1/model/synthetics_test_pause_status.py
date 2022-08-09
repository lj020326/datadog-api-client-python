# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SyntheticsTestPauseStatus(ModelSimple):
    """
    Define whether you want to start (`live`) or pause (`paused`) a
        Synthetic test.

    :param value: Must be one of ["live", "paused"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "LIVE": "live",
            "PAUSED": "paused",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
