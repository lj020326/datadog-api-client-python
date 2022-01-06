# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_assertion import SyntheticsAssertion
    from datadog_api_client.v1.model.synthetics_browser_variable import SyntheticsBrowserVariable
    from datadog_api_client.v1.model.synthetics_config_variable import SyntheticsConfigVariable
    from datadog_api_client.v1.model.synthetics_test_request import SyntheticsTestRequest

    globals()["SyntheticsAssertion"] = SyntheticsAssertion
    globals()["SyntheticsBrowserVariable"] = SyntheticsBrowserVariable
    globals()["SyntheticsConfigVariable"] = SyntheticsConfigVariable
    globals()["SyntheticsTestRequest"] = SyntheticsTestRequest


class SyntheticsTestConfig(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "assertions": ([SyntheticsAssertion],),
            "config_variables": ([SyntheticsConfigVariable],),
            "request": (SyntheticsTestRequest,),
            "variables": ([SyntheticsBrowserVariable],),
        }

    attribute_map = {
        "assertions": "assertions",
        "config_variables": "configVariables",
        "request": "request",
        "variables": "variables",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """SyntheticsTestConfig - a model defined in OpenAPI

        Keyword Args:
            assertions ([SyntheticsAssertion]): [optional] Array of assertions used for the test. Required for single API tests. If omitted the server will use the default value of [].
            config_variables ([SyntheticsConfigVariable]): [optional] Array of variables used for the test.
            request (SyntheticsTestRequest): [optional]
            variables ([SyntheticsBrowserVariable]): [optional] Browser tests only - array of variables used for the test steps.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsTestConfig, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
