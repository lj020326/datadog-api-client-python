# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.slo_history_metrics_series import SLOHistoryMetricsSeries

    globals()["SLOHistoryMetricsSeries"] = SLOHistoryMetricsSeries


class SLOHistoryMetrics(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "denominator": (SLOHistoryMetricsSeries,),
            "interval": (int,),
            "message": (str,),
            "numerator": (SLOHistoryMetricsSeries,),
            "query": (str,),
            "res_type": (str,),
            "resp_version": (int,),
            "times": ([float],),
        }

    attribute_map = {
        "denominator": "denominator",
        "interval": "interval",
        "numerator": "numerator",
        "query": "query",
        "res_type": "res_type",
        "resp_version": "resp_version",
        "times": "times",
        "message": "message",
    }

    read_only_vars = {}

    def __init__(self, denominator, interval, numerator, query, res_type, resp_version, times, *args, **kwargs):
        """SLOHistoryMetrics - a model defined in OpenAPI

        Args:
            denominator (SLOHistoryMetricsSeries):
            interval (int): The aggregated query interval for the series data. It's implicit based on the query time window.
            numerator (SLOHistoryMetricsSeries):
            query (str): The combined numerator and denominator query CSV.
            res_type (str): The series result type. This mimics `batch_query` response type.
            resp_version (int): The series response version type. This mimics `batch_query` response type.
            times ([float]): An array of query timestamps in EPOCH milliseconds

        Keyword Args:
            message (str): [optional] Optional message if there are specific query issues/warnings.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.denominator = denominator
        self.interval = interval
        self.numerator = numerator
        self.query = query
        self.res_type = res_type
        self.resp_version = resp_version
        self.times = times

    @classmethod
    def _from_openapi_data(
        cls, denominator, interval, numerator, query, res_type, resp_version, times, *args, **kwargs
    ):
        """Helper creating a new instance from a response."""

        self = super(SLOHistoryMetrics, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.denominator = denominator
        self.interval = interval
        self.numerator = numerator
        self.query = query
        self.res_type = res_type
        self.resp_version = resp_version
        self.times = times
        return self
