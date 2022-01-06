# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class UserInvitationDataAttributes(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "created_at": (datetime,),
            "expires_at": (datetime,),
            "invite_type": (str,),
            "uuid": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "expires_at": "expires_at",
        "invite_type": "invite_type",
        "uuid": "uuid",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """UserInvitationDataAttributes - a model defined in OpenAPI

        Keyword Args:
            created_at (datetime): [optional] Creation time of the user invitation.
            expires_at (datetime): [optional] Time of invitation expiration.
            invite_type (str): [optional] Type of invitation.
            uuid (str): [optional] UUID of the user invitation.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UserInvitationDataAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
