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


class MetricBulkTagConfigDeleteAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "emails": ([str],),
        }

    attribute_map = {
        "emails": "emails",
    }

    def __init__(self_, emails: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Optional parameters for bulk deleting metric tag configurations.

        :param emails: A list of account emails to notify when the configuration is applied.
        :type emails: [str], optional
        """
        if emails is not unset:
            kwargs["emails"] = emails
        super().__init__(kwargs)
