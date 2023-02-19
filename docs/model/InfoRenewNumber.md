# InfoRenewNumber


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rent_id** | **str** | Unique identifier of the rent operation | 
**number_id** | **str** | Unique identifier of phone number | 
**phone_number** | **str** | Rented phone number in international E.164 format | 
**country_iso** | **str** | Two-letter country code in ISO-3166 alpha 2 standard. Eg. &#x60;DE&#x60;, &#x60;FR&#x60;, &#x60;IT&#x60; | 
**rent_start** | **datetime** | Start date and time of the rent period (UTC) | 
**rent_end** | **datetime** | End date and time of the rent period (UTC) | 
**rent_cost** | **float** | Cost of renting the phone number | 
**auto_renew** | **bool** | Automatically renews the rent for the number with the same period as the current subscription | 
**callback_url** | **str, none_type** | Callback URL (or webhook) to get the SMS that is received on the rented phone number (inbound SMS) | 
**datetime** | **datetime** |  | 

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


