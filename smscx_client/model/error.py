import re  # noqa: F401
import sys  # noqa: F401

from smscx_client.model_utils import (  # noqa: F401
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
    none_type,
    validate_get_composed_info,
    ApiModel
)
from smscx_client.exceptions import ApiAttributeError



class Error(ModelNormal):


    allowed_values = {
        ('type',): {
            'ACCESS_DENIED': "access_denied",
            'DUPLICATE_ID': "duplicate_id",
            'DUPLICATE_VALUE': "duplicate_value",
            'INSUFFICIENT_CREDIT': "insufficient_credit",
            'INSUFFICIENT_SCOPE': "insufficient_scope",
            'INVALID_API_KEY': "invalid_api_key",
            'INVALID_BODY': "invalid_body",
            'INVALID_CLIENT': "invalid_client",
            'INVALID_METHOD': "invalid_method",
            'INVALID_PARAM': "invalid_param",
            'INVALID_REQUEST': "invalid_request",
            'INVALID_SCOPE': "invalid_scope",
            'NO_COVERAGE': "no_coverage",
            'NOT_FOUND': "not_found",
            'RATE_LIMIT': "rate_limit",
            'SERVER_ERROR': "server_error",
            'UNSUPPORTED_GRANT_TYPE': "unsupported_grant_type",
            'INVALID_PIN': "invalid_pin",
            'OTP_EXPIRED': "otp_expired",
            'OTP_FAILED': "otp_failed",
            'OTP_CANCELLED': "otp_cancelled",
            'OTP_VERIFIED': "otp_verified",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def api_types():
        """
        Returns
            api_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'type': (str,),  # noqa: E501
            'message': (str,),  # noqa: E501
            'uri': (str,),  # noqa: E501
            'code': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'type': 'type',  # noqa: E501
        'message': 'message',  # noqa: E501
        'uri': 'uri',  # noqa: E501
        'code': 'code',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_api_data(cls, type, message, uri, code, *args, **kwargs):  # noqa: E501
        """Error - a model

        Args:
            type (str): The type of error returned
            message (str): Short, human-readable description of the error
            uri (str): URI reference in the documentation that provides further information
            code (int): An internal code of the error


        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(ApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
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

        self.type = type
        self.message = message
        self.uri = uri
        self.code = code
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, type, message, uri, code, *args, **kwargs):  # noqa: E501
        """Error - a model

        Args:
            type (str): The type of error returned
            message (str): Short, human-readable description of the error
            uri (str): URI reference in the documentation that provides further information
            code (int): An internal code of the error


        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
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

        self.type = type
        self.message = message
        self.uri = uri
        self.code = code
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_api_data` to instantiate "
                                     f"class with read only attributes.")
