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
    from datadog_api_client.v2.model.sensitive_data_scanner_get_config_response_data import (
        SensitiveDataScannerGetConfigResponseData,
    )
    from datadog_api_client.v2.model.sensitive_data_scanner_get_config_included_item import (
        SensitiveDataScannerGetConfigIncludedItem,
    )
    from datadog_api_client.v2.model.sensitive_data_scanner_meta import SensitiveDataScannerMeta
    from datadog_api_client.v2.model.sensitive_data_scanner_rule_included_item import (
        SensitiveDataScannerRuleIncludedItem,
    )
    from datadog_api_client.v2.model.sensitive_data_scanner_group_included_item import (
        SensitiveDataScannerGroupIncludedItem,
    )


class SensitiveDataScannerGetConfigResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sensitive_data_scanner_get_config_response_data import (
            SensitiveDataScannerGetConfigResponseData,
        )
        from datadog_api_client.v2.model.sensitive_data_scanner_get_config_included_item import (
            SensitiveDataScannerGetConfigIncludedItem,
        )
        from datadog_api_client.v2.model.sensitive_data_scanner_meta import SensitiveDataScannerMeta

        return {
            "data": (SensitiveDataScannerGetConfigResponseData,),
            "included": ([SensitiveDataScannerGetConfigIncludedItem],),
            "meta": (SensitiveDataScannerMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[SensitiveDataScannerGetConfigResponseData, UnsetType] = unset,
        included: Union[
            List[
                Union[
                    SensitiveDataScannerGetConfigIncludedItem,
                    SensitiveDataScannerRuleIncludedItem,
                    SensitiveDataScannerGroupIncludedItem,
                ]
            ],
            UnsetType,
        ] = unset,
        meta: Union[SensitiveDataScannerMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Get all groups response.

        :param data: Response data related to the scanning groups.
        :type data: SensitiveDataScannerGetConfigResponseData, optional

        :param included: Included objects from relationships.
        :type included: [SensitiveDataScannerGetConfigIncludedItem], optional

        :param meta: Meta response containing information about the API.
        :type meta: SensitiveDataScannerMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
