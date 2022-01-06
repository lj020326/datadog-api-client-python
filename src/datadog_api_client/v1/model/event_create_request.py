# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.event_alert_type import EventAlertType
    from datadog_api_client.v1.model.event_priority import EventPriority

    globals()["EventAlertType"] = EventAlertType
    globals()["EventPriority"] = EventPriority


class EventCreateRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {
        "aggregation_key": {
            "max_length": 100,
        },
        "text": {
            "max_length": 4000,
        },
    }

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "aggregation_key": (str,),
            "alert_type": (EventAlertType,),
            "date_happened": (int,),
            "device_name": (str,),
            "host": (str,),
            "id": (int,),
            "payload": (str,),
            "priority": (EventPriority,),
            "related_event_id": (int,),
            "source_type_name": (str,),
            "tags": ([str],),
            "text": (str,),
            "title": (str,),
            "url": (str,),
        }

    attribute_map = {
        "text": "text",
        "title": "title",
        "aggregation_key": "aggregation_key",
        "alert_type": "alert_type",
        "date_happened": "date_happened",
        "device_name": "device_name",
        "host": "host",
        "id": "id",
        "payload": "payload",
        "priority": "priority",
        "related_event_id": "related_event_id",
        "source_type_name": "source_type_name",
        "tags": "tags",
        "url": "url",
    }

    read_only_vars = {
        "id",
        "payload",
        "url",
    }

    def __init__(self, text, title, *args, **kwargs):
        """EventCreateRequest - a model defined in OpenAPI

        Args:
            text (str): The body of the event. Limited to 4000 characters. The text supports markdown. To use markdown in the event text, start the text block with `%%% \\n` and end the text block with `\\n %%%`. Use `msg_text` with the Datadog Ruby library.
            title (str): The event title.

        Keyword Args:
            aggregation_key (str): [optional] An arbitrary string to use for aggregation. Limited to 100 characters. If you specify a key, all events using that key are grouped together in the Event Stream.
            alert_type (EventAlertType): [optional]
            date_happened (int): [optional] POSIX timestamp of the event. Must be sent as an integer (that is no quotes). Limited to events no older than 7 days.
            device_name (str): [optional] A device name.
            host (str): [optional] Host name to associate with the event. Any tags associated with the host are also applied to this event.
            id (int): [optional] Integer ID of the event.
            payload (str): [optional] Payload of the event.
            priority (EventPriority): [optional]
            related_event_id (int): [optional] ID of the parent event. Must be sent as an integer (that is no quotes).
            source_type_name (str): [optional] The type of event being posted. Option examples include nagios, hudson, jenkins, my_apps, chef, puppet, git, bitbucket, etc. A complete list of source attribute values [available here](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value).
            tags ([str]): [optional] A list of tags to apply to the event.
            url (str): [optional] URL of the event.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.text = text
        self.title = title

    @classmethod
    def _from_openapi_data(cls, text, title, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(EventCreateRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.text = text
        self.title = title
        return self
