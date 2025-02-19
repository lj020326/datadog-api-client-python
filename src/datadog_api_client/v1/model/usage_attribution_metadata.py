# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.usage_attribution_aggregates_body import UsageAttributionAggregatesBody
    from datadog_api_client.v1.model.usage_attribution_pagination import UsageAttributionPagination


class UsageAttributionMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.usage_attribution_aggregates_body import UsageAttributionAggregatesBody
        from datadog_api_client.v1.model.usage_attribution_pagination import UsageAttributionPagination

        return {
            "aggregates": ([UsageAttributionAggregatesBody],),
            "pagination": (UsageAttributionPagination,),
        }

    attribute_map = {
        "aggregates": "aggregates",
        "pagination": "pagination",
    }

    def __init__(
        self_,
        aggregates: Union[List[UsageAttributionAggregatesBody], UnsetType] = unset,
        pagination: Union[UsageAttributionPagination, UnsetType] = unset,
        **kwargs,
    ):
        """
        The object containing document metadata.

        :param aggregates: An array of available aggregates.
        :type aggregates: [UsageAttributionAggregatesBody], optional

        :param pagination: The metadata for the current pagination.
        :type pagination: UsageAttributionPagination, optional
        """
        if aggregates is not unset:
            kwargs["aggregates"] = aggregates
        if pagination is not unset:
            kwargs["pagination"] = pagination
        super().__init__(kwargs)
