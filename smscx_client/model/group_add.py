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


def lazy_import():
    from smscx_client.model.group_add_custom_fields import GroupAddCustomFields
    globals()['GroupAddCustomFields'] = GroupAddCustomFields


class GroupAdd(ModelNormal):


    allowed_values = {
    }

    validations = {
        ('country_iso',): {
            'max_length': 2,
            'min_length': 2,
        },
    }

    @cached_property
    def additional_properties_type():
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def api_types():
        """
        Returns
            api_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'phone_number': (str,),  # noqa: E501
            'first_name': (str,),  # noqa: E501
            'last_name': (str,),  # noqa: E501
            'email': (str,),  # noqa: E501
            'field1': (str,),  # noqa: E501
            'field2': (str,),  # noqa: E501
            'field3': (str,),  # noqa: E501
            'field4': (str,),  # noqa: E501
            'field5': (str,),  # noqa: E501
            'country_iso': (str,),  # noqa: E501
            'custom_fields': (GroupAddCustomFields,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'phone_number': 'phoneNumber',  # noqa: E501
        'first_name': 'firstName',  # noqa: E501
        'last_name': 'lastName',  # noqa: E501
        'email': 'email',  # noqa: E501
        'field1': 'field1',  # noqa: E501
        'field2': 'field2',  # noqa: E501
        'field3': 'field3',  # noqa: E501
        'field4': 'field4',  # noqa: E501
        'field5': 'field5',  # noqa: E501
        'country_iso': 'countryIso',  # noqa: E501
        'custom_fields': 'customFields',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_api_data(cls, phone_number, *args, **kwargs):  # noqa: E501
        """GroupAdd - a model

        Args:
            phone_number (str): Phone number in international E.164 format or national format. If national format is provided, for better validation you must use the parameter `countryIso` to provide the country code of the destination phone number    


            first_name (str): Data field for first name of the contact. Use placeholder **{{firstName}}** in text message for data replacement. [optional]  # noqa: E501
            last_name (str): Data field for last name of the contact. Use placeholder **{{lastName}}** in text message for data replacement. [optional]  # noqa: E501
            email (str): Data field for email of the contact. Use placeholder **{{email}}** in text message for data replacement. [optional]  # noqa: E501
            field1 (str): Data field for extra information of the contact. Use placeholder **{{field1}}** in text message for data replacement. [optional]  # noqa: E501
            field2 (str): Data field for extra information of the contact. Use placeholder **{{field2}}** in text message for data replacement. [optional]  # noqa: E501
            field3 (str): Data field for extra information of the contact. Use placeholder **{{field3}}** in text message for data replacement. [optional]  # noqa: E501
            field4 (str): Data field for extra information of the contact. Use placeholder **{{field4}}** in text message for data replacement. [optional]  # noqa: E501
            field5 (str): Data field for extra information of the contact. Use placeholder **{{field5}}** in text message for data replacement. [optional]  # noqa: E501
            country_iso (str): Two-letter country ISO of the phone number you want to validate. Please note that if an international E.164 phone number format is provided, the **countryIso** will be ignored. [optional]  # noqa: E501
            custom_fields (GroupAddCustomFields): [optional]  # noqa: E501
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

        self.phone_number = phone_number
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
    def __init__(self, phone_number, *args, **kwargs):  # noqa: E501
        """GroupAdd - a model

        Args:
            phone_number (str): Phone number in international E.164 format or national format. If national format is provided, for better validation you must use the parameter `countryIso` to provide the country code of the destination phone number    


            first_name (str): Data field for first name of the contact. Use placeholder **{{firstName}}** in text message for data replacement. [optional]  # noqa: E501
            last_name (str): Data field for last name of the contact. Use placeholder **{{lastName}}** in text message for data replacement. [optional]  # noqa: E501
            email (str): Data field for email of the contact. Use placeholder **{{email}}** in text message for data replacement. [optional]  # noqa: E501
            field1 (str): Data field for extra information of the contact. Use placeholder **{{field1}}** in text message for data replacement. [optional]  # noqa: E501
            field2 (str): Data field for extra information of the contact. Use placeholder **{{field2}}** in text message for data replacement. [optional]  # noqa: E501
            field3 (str): Data field for extra information of the contact. Use placeholder **{{field3}}** in text message for data replacement. [optional]  # noqa: E501
            field4 (str): Data field for extra information of the contact. Use placeholder **{{field4}}** in text message for data replacement. [optional]  # noqa: E501
            field5 (str): Data field for extra information of the contact. Use placeholder **{{field5}}** in text message for data replacement. [optional]  # noqa: E501
            country_iso (str): Two-letter country ISO of the phone number you want to validate. Please note that if an international E.164 phone number format is provided, the **countryIso** will be ignored. [optional]  # noqa: E501
            custom_fields (GroupAddCustomFields): [optional]  # noqa: E501
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

        self.phone_number = phone_number
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
