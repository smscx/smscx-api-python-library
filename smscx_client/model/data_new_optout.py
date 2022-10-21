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



class DataNewOptout(ModelNormal):


    allowed_values = {
        ('optout_type',): {
            'ADMIN': "admin",
            'LINK': "link",
        },
    }

    validations = {
        ('campaign_id',): {
            'max_length': 36,
            'min_length': 36,
            'regex': {
                'pattern': r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',  # noqa: E501
            },
        },
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
            'hit_id': (int,),  # noqa: E501
            'optout_id': (str,),  # noqa: E501
            'optout_url': (str,),  # noqa: E501
            'optout_type': (str,),  # noqa: E501
            'country_iso': (str,),  # noqa: E501
            'datetime': (str,),  # noqa: E501
            'phone_number': (str,),  # noqa: E501
            'campaign_id': (str, none_type,),  # noqa: E501
            'group_id': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'hit_id': 'hitId',  # noqa: E501
        'optout_id': 'optoutId',  # noqa: E501
        'optout_url': 'optoutUrl',  # noqa: E501
        'optout_type': 'optoutType',  # noqa: E501
        'country_iso': 'countryIso',  # noqa: E501
        'datetime': 'datetime',  # noqa: E501
        'phone_number': 'phoneNumber',  # noqa: E501
        'campaign_id': 'campaignId',  # noqa: E501
        'group_id': 'groupId',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_api_data(cls, hit_id, optout_id, optout_url, optout_type, country_iso, datetime, *args, **kwargs):  # noqa: E501
        """DataNewOptout - a model

        Args:
            hit_id (int):
            optout_id (str): ID of the optout link
            optout_url (str): URL of the optout link
            optout_type (str): The method by which the contact has unsubscribed. Value `link` means he clicked on the optout link and submitted the form and value `admin` it means that the client was added to the optout list by you
            country_iso (str): Two-letter country ISO of the phone number that unsubscribed.
            datetime (str):


            phone_number (str): Phone number that choose to opt out. . [optional]  # noqa: E501
            campaign_id (str, none_type): Identifier of the campaign from which the contact has unsubscribed. If optout tracking was enabled, this parameter will not be null.. [optional]  # noqa: E501
            group_id (str, none_type): Identifier of the group the contact was in. If optout tracking was enabled, this parameter will not be null.. [optional]  # noqa: E501
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

        self.hit_id = hit_id
        self.optout_id = optout_id
        self.optout_url = optout_url
        self.optout_type = optout_type
        self.country_iso = country_iso
        self.datetime = datetime
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
    def __init__(self, hit_id, optout_id, optout_url, optout_type, country_iso, datetime, *args, **kwargs):  # noqa: E501
        """DataNewOptout - a model

        Args:
            hit_id (int):
            optout_id (str): ID of the optout link
            optout_url (str): URL of the optout link
            optout_type (str): The method by which the contact has unsubscribed. Value `link` means he clicked on the optout link and submitted the form and value `admin` it means that the client was added to the optout list by you
            country_iso (str): Two-letter country ISO of the phone number that unsubscribed.
            datetime (str):


            phone_number (str): Phone number that choose to opt out. . [optional]  # noqa: E501
            campaign_id (str, none_type): Identifier of the campaign from which the contact has unsubscribed. If optout tracking was enabled, this parameter will not be null.. [optional]  # noqa: E501
            group_id (str, none_type): Identifier of the group the contact was in. If optout tracking was enabled, this parameter will not be null.. [optional]  # noqa: E501
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

        self.hit_id = hit_id
        self.optout_id = optout_id
        self.optout_url = optout_url
        self.optout_type = optout_type
        self.country_iso = country_iso
        self.datetime = datetime
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
