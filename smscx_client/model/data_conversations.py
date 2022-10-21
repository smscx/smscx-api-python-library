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



class DataConversations(ModelNormal):


    allowed_values = {
    }

    validations = {
        ('conversation_id',): {
            'max_length': 36,
            'min_length': 36,
            'regex': {
                'pattern': r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',  # noqa: E501
            },
        },
        ('country_iso',): {
            'max_length': 2,
            'min_length': 2,
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
            'conversation_id': (str,),  # noqa: E501
            'phone_number': (str,),  # noqa: E501
            'country_iso': (str,),  # noqa: E501
            'first_name': (str, none_type,),  # noqa: E501
            'last_name': (str,),  # noqa: E501
            'unread_messages': (int,),  # noqa: E501
            'last_reply': (str,),  # noqa: E501
            'last_update': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'conversation_id': 'conversationId',  # noqa: E501
        'phone_number': 'phoneNumber',  # noqa: E501
        'country_iso': 'countryIso',  # noqa: E501
        'first_name': 'firstName',  # noqa: E501
        'last_name': 'lastName',  # noqa: E501
        'unread_messages': 'unreadMessages',  # noqa: E501
        'last_reply': 'lastReply',  # noqa: E501
        'last_update': 'lastUpdate',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_api_data(cls, conversation_id, phone_number, country_iso, first_name, last_name, unread_messages, last_reply, last_update, *args, **kwargs):  # noqa: E501
        """DataConversations - a model

        Args:
            conversation_id (str): Unique identifier of the conversation
            phone_number (str): Phone number in international E.164 format
            country_iso (str): Two-letter country ISO of the phone number
            first_name (str, none_type): First name of the contact
            last_name (str): Last name of the contact
            unread_messages (int): New messages in this conversation that were not read
            last_reply (str): Preview of the last message in the converstion
            last_update (str): Date and time of last reply from the contact to this conversation


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

        self.conversation_id = conversation_id
        self.phone_number = phone_number
        self.country_iso = country_iso
        self.first_name = first_name
        self.last_name = last_name
        self.unread_messages = unread_messages
        self.last_reply = last_reply
        self.last_update = last_update
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
    def __init__(self, conversation_id, phone_number, country_iso, first_name, last_name, unread_messages, last_reply, last_update, *args, **kwargs):  # noqa: E501
        """DataConversations - a model

        Args:
            conversation_id (str): Unique identifier of the conversation
            phone_number (str): Phone number in international E.164 format
            country_iso (str): Two-letter country ISO of the phone number
            first_name (str, none_type): First name of the contact
            last_name (str): Last name of the contact
            unread_messages (int): New messages in this conversation that were not read
            last_reply (str): Preview of the last message in the converstion
            last_update (str): Date and time of last reply from the contact to this conversation


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

        self.conversation_id = conversation_id
        self.phone_number = phone_number
        self.country_iso = country_iso
        self.first_name = first_name
        self.last_name = last_name
        self.unread_messages = unread_messages
        self.last_reply = last_reply
        self.last_update = last_update
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
