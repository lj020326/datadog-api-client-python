# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SecurityMonitoringSignalIncidentsUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "incident_ids": ([int],),
            "version": (int,),
        }

    attribute_map = {
        "incident_ids": "incident_ids",
        "version": "version",
    }

    def __init__(self_, incident_ids: List[int], version: Union[int, UnsetType] = unset, **kwargs):
        """
        Attributes describing the new list of related signals for a security signal.

        :param incident_ids: Array of incidents that are associated with this signal.
        :type incident_ids: [int]

        :param version: Version of the updated signal. If server side version is higher, update will be rejected.
        :type version: int, optional
        """
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.incident_ids = incident_ids
