# TwoWay

If this originator is activated for two-way messaging, this object will contain details about country, type of two-way number, subscription expiry date. It will be empty object otherwise

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of number to send and receive SMS: VLN (Virtual Local Number), Short code, 10DLC (10 Digits Long Code) | 
**country_iso** | **str** | Two-letter country code (ISO-3166 alpha 2) of the destination where two-way messaging will be used | 
**expire_date** | **datetime** | The date in UTC when the two-way messaging number subscription will expire | 


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


