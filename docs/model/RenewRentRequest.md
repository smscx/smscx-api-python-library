# RenewRentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rent_period** | **int** | Rental period of the phone number (in days). This parameter is optional. If not present, the phone number rent will renew with the current rent period. | [optional] 
**auto_renew** | **bool** | Auto renew the rent of the phone number at the end of the rental period | [optional]  if omitted the server will use the default value of False
**callback_url** | **str, none_type** | Callback URL (or webhook) to get the SMS that is received on the rented phone number (inbound SMS) | [optional] 

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


