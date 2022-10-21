# DataDlrUpdate

Event data, grouped in multiple objects (up to 200 in a request)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **str** | Identifier of the sent campaign | 
**msg_id** | **str** | Identifier of the sent message | 
**status_code** | **int** | Numeric value of the delivery report | 
**status** | **str** | Delivery report of the sent SMS | 
**error_code** | **int, none_type** | A code that give detailed information about a failed delivery. See the [list of error codes](#error-codes) for more details. A non-null value indicates that the message could not be delivered. | 
**datetime** | **str** |  | 
**track_data** | **str, none_type** | Identifier of the message ID provided by client for tracking purposes | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


