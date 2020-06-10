# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import re  # noqa: F401
import sys  # noqa: F401

import six  # noqa: F401
import nulltype  # noqa: F401

from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    int,
    none_type,
    str,
    validate_get_composed_info,
)
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


class MonitorOptions(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('min_failure_duration',): {
            'inclusive_maximum': 7200,
            'inclusive_minimum': 0,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a class method so a model may have properties that are
        of type self, this ensures that we don't create a cyclic import

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'aggregation': (monitor_options_aggregation.MonitorOptionsAggregation,),  # noqa: E501
            'device_ids': ([monitor_device_id.MonitorDeviceID],),  # noqa: E501
            'enable_logs_sample': (bool,),  # noqa: E501
            'escalation_message': (str,),  # noqa: E501
            'evaluation_delay': (int, none_type,),  # noqa: E501
            'include_tags': (bool,),  # noqa: E501
            'locked': (bool,),  # noqa: E501
            'min_failure_duration': (int, none_type,),  # noqa: E501
            'min_location_failed': (int, none_type,),  # noqa: E501
            'new_host_delay': (int, none_type,),  # noqa: E501
            'no_data_timeframe': (int, none_type,),  # noqa: E501
            'notify_audit': (bool,),  # noqa: E501
            'notify_no_data': (bool,),  # noqa: E501
            'renotify_interval': (int, none_type,),  # noqa: E501
            'require_full_window': (bool,),  # noqa: E501
            'silenced': ({str: (int, none_type)},),  # noqa: E501
            'synthetics_check_id': (int, none_type,),  # noqa: E501
            'threshold_windows': (monitor_threshold_window_options.MonitorThresholdWindowOptions,),  # noqa: E501
            'thresholds': (monitor_thresholds.MonitorThresholds,),  # noqa: E501
            'timeout_h': (int, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        'aggregation': 'aggregation',  # noqa: E501
        'device_ids': 'device_ids',  # noqa: E501
        'enable_logs_sample': 'enable_logs_sample',  # noqa: E501
        'escalation_message': 'escalation_message',  # noqa: E501
        'evaluation_delay': 'evaluation_delay',  # noqa: E501
        'include_tags': 'include_tags',  # noqa: E501
        'locked': 'locked',  # noqa: E501
        'min_failure_duration': 'min_failure_duration',  # noqa: E501
        'min_location_failed': 'min_location_failed',  # noqa: E501
        'new_host_delay': 'new_host_delay',  # noqa: E501
        'no_data_timeframe': 'no_data_timeframe',  # noqa: E501
        'notify_audit': 'notify_audit',  # noqa: E501
        'notify_no_data': 'notify_no_data',  # noqa: E501
        'renotify_interval': 'renotify_interval',  # noqa: E501
        'require_full_window': 'require_full_window',  # noqa: E501
        'silenced': 'silenced',  # noqa: E501
        'synthetics_check_id': 'synthetics_check_id',  # noqa: E501
        'threshold_windows': 'threshold_windows',  # noqa: E501
        'thresholds': 'thresholds',  # noqa: E501
        'timeout_h': 'timeout_h',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """monitor_options.MonitorOptions - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            aggregation (monitor_options_aggregation.MonitorOptionsAggregation): [optional]  # noqa: E501
            device_ids ([monitor_device_id.MonitorDeviceID]): IDs of the device the Synthetics monitor is running on.. [optional]  # noqa: E501
            enable_logs_sample (bool): Whether or not to send a log sample when the log monitor triggers.. [optional]  # noqa: E501
            escalation_message (str): A message to include with a re-notification. Supports the &#x60;@username&#x60; notification we allow elsewhere. Not applicable if &#x60;renotify_interval&#x60; is &#x60;None&#x60;.. [optional] if omitted the server will use the default value of 'none'  # noqa: E501
            evaluation_delay (int, none_type): Time (in seconds) to delay evaluation, as a non-negative integer. For example, if the value is set to &#x60;300&#x60; (5min), the timeframe is set to &#x60;last_5m&#x60; and the time is 7:00, the monitor evaluates data from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled metrics to ensure the monitor always has data during evaluation.. [optional]  # noqa: E501
            include_tags (bool): A Boolean indicating whether notifications from this monitor automatically inserts its triggering tags into the title.  **Examples** - If &#x60;True&#x60;, &#x60;[Triggered on {host:h1}] Monitor Title&#x60; - If &#x60;False&#x60;, &#x60;[Triggered] Monitor Title&#x60;. [optional] if omitted the server will use the default value of True  # noqa: E501
            locked (bool): Whether or not the monitor is locked (only editable by creator and admins).. [optional]  # noqa: E501
            min_failure_duration (int, none_type): How long the test should be in failure before alerting (integer, number of seconds, max 7200).. [optional] if omitted the server will use the default value of 0  # noqa: E501
            min_location_failed (int, none_type): The minimum number of locations in failure at the same time during at least one moment in the &#x60;min_failure_duration&#x60; period (&#x60;min_location_failed&#x60; and &#x60;min_failure_duration&#x60; are part of the advanced alerting rules - integer, &gt;&#x3D; 1).. [optional] if omitted the server will use the default value of 1  # noqa: E501
            new_host_delay (int, none_type): Time (in seconds) to allow a host to boot and applications to fully start before starting the evaluation of monitor results. Should be a non negative integer.. [optional] if omitted the server will use the default value of 300  # noqa: E501
            no_data_timeframe (int, none_type): The number of minutes before a monitor notifies after data stops reporting. Datadog recommends at least 2x the monitor timeframe for metric alerts or 2 minutes for service checks. If omitted, 2x the evaluation timeframe is used for metric alerts, and 24 hours is used for service checks.. [optional]  # noqa: E501
            notify_audit (bool): A Boolean indicating whether tagged users is notified on changes to this monitor.. [optional] if omitted the server will use the default value of False  # noqa: E501
            notify_no_data (bool): A Boolean indicating whether this monitor notifies when data stops reporting.. [optional] if omitted the server will use the default value of False  # noqa: E501
            renotify_interval (int, none_type): The number of minutes after the last notification before a monitor re-notifies on the current status. It only re-notifies if it’s not resolved.. [optional]  # noqa: E501
            require_full_window (bool): A Boolean indicating whether this monitor needs a full window of data before it’s evaluated. We highly recommend you set this to &#x60;false&#x60; for sparse metrics, otherwise some evaluations are skipped. For “on average” “at all times” and “in total” aggregation, default is true. &#x60;False&#x60; otherwise.. [optional] if omitted the server will use the default value of True  # noqa: E501
            silenced ({str: (int, none_type)}): Information about the downtime applied to the monitor.. [optional]  # noqa: E501
            synthetics_check_id (int, none_type): ID of the corresponding Synthetic check.. [optional]  # noqa: E501
            threshold_windows (monitor_threshold_window_options.MonitorThresholdWindowOptions): [optional]  # noqa: E501
            thresholds (monitor_thresholds.MonitorThresholds): [optional]  # noqa: E501
            timeout_h (int, none_type): The number of hours of the monitor not reporting data before it automatically resolves from a triggered state.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in six.iteritems(kwargs):
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
