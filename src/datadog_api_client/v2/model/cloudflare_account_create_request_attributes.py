# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CloudflareAccountCreateRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "api_key": (str,),
            "email": (str,),
            "name": (str,),
        }

    attribute_map = {
        "api_key": "api_key",
        "email": "email",
        "name": "name",
    }

    def __init__(self_, api_key: str, name: str, email: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes object for creating a Cloudflare account.

        :param api_key: The API key (or token) for the Cloudflare account.
        :type api_key: str

        :param email: The email associated with the Cloudflare account. If an API key is provided (and not a token), this field is also required.
        :type email: str, optional

        :param name: The name of the Cloudflare account.
        :type name: str
        """
        if email is not unset:
            kwargs["email"] = email
        super().__init__(kwargs)

        self_.api_key = api_key
        self_.name = name
