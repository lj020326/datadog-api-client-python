# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.incident_services_response_meta import IncidentServicesResponseMeta
    from datadog_api_client.v2.model.incident_team_included_items import IncidentTeamIncludedItems
    from datadog_api_client.v2.model.incident_team_response_data import IncidentTeamResponseData

    globals()["IncidentServicesResponseMeta"] = IncidentServicesResponseMeta
    globals()["IncidentTeamIncludedItems"] = IncidentTeamIncludedItems
    globals()["IncidentTeamResponseData"] = IncidentTeamResponseData


class IncidentTeamsResponse(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "data": ([IncidentTeamResponseData],),
            "included": ([IncidentTeamIncludedItems],),
            "meta": (IncidentServicesResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "meta": "meta",
    }

    read_only_vars = {
        "included",
    }

    def __init__(self, data, *args, **kwargs):
        """IncidentTeamsResponse - a model defined in OpenAPI

        Args:
            data ([IncidentTeamResponseData]): An array of incident teams.

        Keyword Args:
            included ([IncidentTeamIncludedItems]): [optional] Included related resources which the user requested.
            meta (IncidentServicesResponseMeta): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.data = data

    @classmethod
    def _from_openapi_data(cls, data, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IncidentTeamsResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.data = data
        return self
