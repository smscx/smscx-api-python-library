# DataAvailableNumbersRent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_id** | **str** | Unique identifier of phone number | 
**phone_number** | **str, none_type** | Phone number in international E.164 format. In some cases this value might be null as the phone number will be selected random from a pool of numbers | 
**country_iso** | **str** | Two-letter country ISO of the phone number | 
**network_operator** | **str** | Network operator of the phone number | 
**sms** | **[str]** | SMS features that the phone number supports (inbound or outbound SMS) | 
**voice** | **[str]** | Voice features that the phone number supports | 
**min_rent** | **str, none_type** | Minimum period that this phone number must be rented (in days) | 
**max_rent** | **str, none_type** | Maximum period that this phone number can be rented (in days) | 
**setup_cost** | **float** | One time setup fee for the rented phone number (if applicable) | 
**rental_cost** | [**RentalCost**](RentalCost.md) |  | 
**inbound_sms_cost** | **float** | Cost for receiving a SMS on this phone number (most of the time receiving is free, meaning this is has value 0) | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


