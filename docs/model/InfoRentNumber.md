# InfoRentNumber


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
**setup_cost** | **float** | The one time setup fee charged at the initial rent of the phone number (if applicable) | 
**auto_renew** | **bool** | Automatically renews the rent for the number with the same period as the current subscription | 
**callback_url** | **str, none_type** | Callback URL (or webhook) to get the SMS that is received on the rented phone number (inbound SMS) | 
**approved** | **bool** | If the phone number requires registration, this parameter indicates if the phone number was approved. Value &#x60;true&#x60; means number approved, &#x60;false&#x60; means processing | 
**datetime** | **datetime** |  | 

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


