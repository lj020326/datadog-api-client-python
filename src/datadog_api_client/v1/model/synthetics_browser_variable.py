# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_browser_variable_type import SyntheticsBrowserVariableType

    globals()["SyntheticsBrowserVariableType"] = SyntheticsBrowserVariableType


class SyntheticsBrowserVariable(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "example": (str,),
            "id": (str,),
            "name": (str,),
            "pattern": (str,),
            "type": (SyntheticsBrowserVariableType,),
        }

    attribute_map = {
        "name": "name",
        "type": "type",
        "example": "example",
        "id": "id",
        "pattern": "pattern",
    }

    read_only_vars = {}

    def __init__(self, name, type, *args, **kwargs):
        """SyntheticsBrowserVariable - a model defined in OpenAPI

        Args:
            name (str): Name of the variable.
            type (SyntheticsBrowserVariableType):

        Keyword Args:
            example (str): [optional] Example for the variable.
            id (str): [optional] ID for the variable. Global variables require an ID.
            pattern (str): [optional] Pattern of the variable.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.name = name
        self.type = type

    @classmethod
    def _from_openapi_data(cls, name, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsBrowserVariable, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.name = name
        self.type = type
        return self
