# DataReceiveSms


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msg_id** | **str** | Identifier of the received message | 
**_from** | **str** | The phone number that sent the SMS, in international E.164 format | 
**country_iso** | **str** | Two-letter country ISO of the phone number that sent the SMS | 
**to** | **str** | The short code or virtual phone number that received the SMS | 
**text** | **str** | The text of the received SMS | 
**cost** | **float** | The cost of receiving the SMS. It is usually free to receive SMS, but in some countries some charges may apply  | 
**received_at** | **datetime** | Date and time of receiving the text message | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


