# InfoRentNumber


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rent_id** | **str** | Unique identifier of the rent operation | 
**rent_cost** | **float** | Cost of renting the phone number for the period chosen | 
**setup_cost** | **float** | One time setup fee for the rented phone number (if applicable) | 
**rent_period** | **int** | Rental period of the phone number (in days) | 
**rent_start** | **datetime** | Start date and time of the rental period (UTC) | 
**rent_end** | **datetime** | End date and time of the rental period (UTC) | 
**phone_number** | **str** | Phone number that is rented in international E.164 format | 
**country_iso** | **str** | Two-letter country code in ISO-3166 alpha 2 standard. Eg. &#x60;DE&#x60;, &#x60;FR&#x60;, &#x60;IT&#x60; | 
**network_operator** | **str** | Network operator of the phone number | 
**auto_renew** | **bool** | Status of the auto renewal setting for this number rental | 
**sms** | **[str]** | SMS features that the phone number supports (inbound or outbound SMS) | 
**voice** | **[str]** | Voice features that the phone number supports | 
**min_rent** | **str, none_type** | Minimum period that this phone number must be rented (in days) | 
**max_rent** | **str, none_type** | Maximum period that this phone number can be rented (in days) | 
**rental_cost** | [**RentalCost**](RentalCost.md) |  | 
**inbound_sms_cost** | **float** | Cost for receiving a SMS on this phone number (most of the time receiving is free, meaning this is has value 0) | 
**callback_url** | **str, none_type** | Callback URL (or webhook) to get the received SMS on the rented phone number | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


