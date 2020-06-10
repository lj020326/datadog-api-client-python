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
    from datadog_api_client.v1.model import creator
except ImportError:
    creator = sys.modules[
        'datadog_api_client.v1.model.creator']
try:
    from datadog_api_client.v1.model import service_level_objective_query
except ImportError:
    service_level_objective_query = sys.modules[
        'datadog_api_client.v1.model.service_level_objective_query']
try:
    from datadog_api_client.v1.model import slo_threshold
except ImportError:
    slo_threshold = sys.modules[
        'datadog_api_client.v1.model.slo_threshold']
try:
    from datadog_api_client.v1.model import slo_type
except ImportError:
    slo_type = sys.modules[
        'datadog_api_client.v1.model.slo_type']


class ServiceLevelObjective(ModelNormal):
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
            'name': (str,),  # noqa: E501
            'thresholds': ([slo_threshold.SLOThreshold],),  # noqa: E501
            'type': (slo_type.SLOType,),  # noqa: E501
            'created_at': (int,),  # noqa: E501
            'creator': (creator.Creator,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'groups': ([str],),  # noqa: E501
            'id': (str,),  # noqa: E501
            'modified_at': (int,),  # noqa: E501
            'monitor_ids': ([int],),  # noqa: E501
            'monitor_tags': ([str],),  # noqa: E501
            'query': (service_level_objective_query.ServiceLevelObjectiveQuery,),  # noqa: E501
            'tags': ([str],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        'name': 'name',  # noqa: E501
        'thresholds': 'thresholds',  # noqa: E501
        'type': 'type',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'creator': 'creator',  # noqa: E501
        'description': 'description',  # noqa: E501
        'groups': 'groups',  # noqa: E501
        'id': 'id',  # noqa: E501
        'modified_at': 'modified_at',  # noqa: E501
        'monitor_ids': 'monitor_ids',  # noqa: E501
        'monitor_tags': 'monitor_tags',  # noqa: E501
        'query': 'query',  # noqa: E501
        'tags': 'tags',  # noqa: E501
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
    def __init__(self, name, thresholds, type, *args, **kwargs):  # noqa: E501
        """service_level_objective.ServiceLevelObjective - a model defined in OpenAPI

        Args:
            name (str): The name of the service level objective object.
            thresholds ([slo_threshold.SLOThreshold]): The thresholds (timeframes and associated targets) for this service level objective object.
            type (slo_type.SLOType):

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
            created_at (int): Creation timestamp (UNIX time in seconds)  Always included in service level objective responses.. [optional]  # noqa: E501
            creator (creator.Creator): [optional]  # noqa: E501
            description (str, none_type): A user-defined description of the service level objective.  Always included in service level objective responses (but may be &#x60;null&#x60;). Optional in create/update requests.. [optional]  # noqa: E501
            groups ([str]): A list of (up to 20) monitor groups that narrow the scope of a monitor service level objective.  Included in service level objective responses if it is not empty. Optional in create/update requests for monitor service level objectives, but may only be used when then length of the &#x60;monitor_ids&#x60; field is one.. [optional]  # noqa: E501
            id (str): A unique identifier for the service level objective object.  Always included in service level objective responses.. [optional]  # noqa: E501
            modified_at (int): Modification timestamp (UNIX time in seconds)  Always included in service level objective responses.. [optional]  # noqa: E501
            monitor_ids ([int]): A list of monitor ids that defines the scope of a monitor service level objective. **Required if type is &#x60;monitor&#x60;**.. [optional]  # noqa: E501
            monitor_tags ([str]): The union of monitor tags for all monitors referenced by the &#x60;monitor_ids&#x60; field. Always included in service level objective responses for monitor service level objectives (but may be empty). Ignored in create/update requests. Does not affect which monitors are included in the service level objective (that is determined entirely by the &#x60;monitor_ids&#x60; field).. [optional]  # noqa: E501
            query (service_level_objective_query.ServiceLevelObjectiveQuery): [optional]  # noqa: E501
            tags ([str]): A list of tags associated with this service level objective. Always included in service level objective responses (but may be empty). Optional in create/update requests.. [optional]  # noqa: E501
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

        self.name = name
        self.thresholds = thresholds
        self.type = type
        for var_name, var_value in six.iteritems(kwargs):
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
