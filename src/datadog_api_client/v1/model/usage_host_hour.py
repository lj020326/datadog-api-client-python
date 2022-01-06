# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class UsageHostHour(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "agent_host_count": (int,),
            "alibaba_host_count": (int,),
            "apm_azure_app_service_host_count": (int,),
            "apm_host_count": (int,),
            "aws_host_count": (int,),
            "azure_host_count": (int,),
            "container_count": (int,),
            "gcp_host_count": (int,),
            "heroku_host_count": (int,),
            "host_count": (int,),
            "hour": (datetime,),
            "infra_azure_app_service": (int,),
            "opentelemetry_host_count": (int,),
            "vsphere_host_count": (int,),
        }

    attribute_map = {
        "agent_host_count": "agent_host_count",
        "alibaba_host_count": "alibaba_host_count",
        "apm_azure_app_service_host_count": "apm_azure_app_service_host_count",
        "apm_host_count": "apm_host_count",
        "aws_host_count": "aws_host_count",
        "azure_host_count": "azure_host_count",
        "container_count": "container_count",
        "gcp_host_count": "gcp_host_count",
        "heroku_host_count": "heroku_host_count",
        "host_count": "host_count",
        "hour": "hour",
        "infra_azure_app_service": "infra_azure_app_service",
        "opentelemetry_host_count": "opentelemetry_host_count",
        "vsphere_host_count": "vsphere_host_count",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """UsageHostHour - a model defined in OpenAPI

        Keyword Args:
            agent_host_count (int): [optional] Contains the total number of infrastructure hosts reporting during a given hour that were running the Datadog Agent.
            alibaba_host_count (int): [optional] Contains the total number of hosts that reported through Alibaba integration (and were NOT running the Datadog Agent).
            apm_azure_app_service_host_count (int): [optional] Contains the total number of Azure App Services hosts using APM.
            apm_host_count (int): [optional] Shows the total number of hosts using APM during the hour, these are counted as billable (except during trial periods).
            aws_host_count (int): [optional] Contains the total number of hosts that reported through the AWS integration (and were NOT running the Datadog Agent).
            azure_host_count (int): [optional] Contains the total number of hosts that reported through Azure integration (and were NOT running the Datadog Agent).
            container_count (int): [optional] Shows the total number of containers reported by the Docker integration during the hour.
            gcp_host_count (int): [optional] Contains the total number of hosts that reported through the Google Cloud integration (and were NOT running the Datadog Agent).
            heroku_host_count (int): [optional] Contains the total number of Heroku dynos reported by the Datadog Agent.
            host_count (int): [optional] Contains the total number of billable infrastructure hosts reporting during a given hour. This is the sum of `agent_host_count`, `aws_host_count`, and `gcp_host_count`.
            hour (datetime): [optional] The hour for the usage.
            infra_azure_app_service (int): [optional] Contains the total number of hosts that reported through the Azure App Services integration (and were NOT running the Datadog Agent).
            opentelemetry_host_count (int): [optional] Contains the total number of hosts reported by Datadog exporter for the OpenTelemetry Collector.
            vsphere_host_count (int): [optional] Contains the total number of hosts that reported through vSphere integration (and were NOT running the Datadog Agent).
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageHostHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
