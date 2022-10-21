# RentNumberRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_id** | **str** | Unique identifier of the phone number from the available rental list | 
**rent_period** | **int** | Rental period of the phone number (in days) | 
**auto_renew** | **bool** | Auto renew the rental of the phone number at the end of the rental period | [optional]  if omitted the server will use the default value of False
**callback_url** | **str, none_type** | Callback URL (or webhook) to get the received SMS on the rented phone number | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


