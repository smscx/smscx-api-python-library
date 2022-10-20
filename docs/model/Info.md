# Info


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **str** | Unique identifier of the campaign | 
**total_phone_numbers** | **int** | Total phone numbers submitted for processing | 
**total_valid** | **int** | Total valid phone numbers after validation | 
**total_invalid** | **int** | Total invalid phone numbers after validation | 
**total_cost** | **float** | Total cost of sending the message | 
**total_parts** | **int** | Total message parts | 
**dlr_callback_url** | **str, none_type** | Callback URL for receiving the delivery report | 
**phone_numbers_by_country** | [**PhoneNumbersByCountry**](PhoneNumbersByCountry.md) |  | 
**scheduled** | **bool** | Confirmation that the message/campaign was scheduled at a later date | 
**transliteration_analysis** | [**TransliterationAnalysis**](TransliterationAnalysis.md) |  | [optional] 
**total_in_quiet_hours** | **int** | Total phone numbers that were detected to be inside the interval of quiet hours | [optional] 
**invalid** | **[str]** | An array with numbers that were detected to be invalid | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


