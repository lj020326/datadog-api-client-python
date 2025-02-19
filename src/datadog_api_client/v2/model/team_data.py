# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.team_attributes import TeamAttributes
    from datadog_api_client.v2.model.team_type import TeamType


class TeamData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_attributes import TeamAttributes
        from datadog_api_client.v2.model.team_type import TeamType

        return {
            "attributes": (TeamAttributes,),
            "id": (str,),
            "type": (TeamType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: TeamAttributes, id: str, type: TeamType, **kwargs):
        """
        A team

        :param attributes: Team attributes
        :type attributes: TeamAttributes

        :param id: The team's identifier
        :type id: str

        :param type: Team type
        :type type: TeamType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
