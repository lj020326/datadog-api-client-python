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


class MetricBulkTagConfigStatusAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "emails": ([str],),
            "status": (str,),
            "tags": ([str],),
        }

    attribute_map = {
        "emails": "emails",
        "status": "status",
        "tags": "tags",
    }

    def __init__(
        self_,
        emails: Union[List[str], UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Optional attributes for the status of a bulk tag configuration request.

        :param emails: A list of account emails to notify when the configuration is applied.
        :type emails: [str], optional

        :param status: The status of the request.
        :type status: str, optional

        :param tags: A list of tag names to apply to the configuration.
        :type tags: [str], optional
        """
        if emails is not unset:
            kwargs["emails"] = emails
        if status is not unset:
            kwargs["status"] = status
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
