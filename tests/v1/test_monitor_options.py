# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import monitor_device_id
except ImportError:
    monitor_device_id = sys.modules[
        'datadog_api_client.v1.model.monitor_device_id']
try:
    from datadog_api_client.v1.model import monitor_options_aggregation
except ImportError:
    monitor_options_aggregation = sys.modules[
        'datadog_api_client.v1.model.monitor_options_aggregation']
try:
    from datadog_api_client.v1.model import monitor_threshold_window_options
except ImportError:
    monitor_threshold_window_options = sys.modules[
        'datadog_api_client.v1.model.monitor_threshold_window_options']
try:
    from datadog_api_client.v1.model import monitor_thresholds
except ImportError:
    monitor_thresholds = sys.modules[
        'datadog_api_client.v1.model.monitor_thresholds']
from datadog_api_client.v1.model.monitor_options import MonitorOptions


class TestMonitorOptions(unittest.TestCase):
    """MonitorOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonitorOptions(self):
        """Test MonitorOptions"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MonitorOptions()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
