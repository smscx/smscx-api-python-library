# DataReportsCampaigns


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the campaign | 
**name** | **str** | Name of the sent campaign | 
**_from** | **str** | Originator (sender name) of the message  | 
**groups** | [**[Group]**](Group.md) |  | 
**total_phone_numers** | **int** | Total recipients of the sent campaign | 
**parts** | **int** | Total parts of the sent campaign | 
**cost** | **float** | Total cost of the sent campaign  | 
**text** | **str** | Content of the message | 
**source** | **str** | Source of the message sending | 
**channel** | **str** | Channel that sent the message | 
**datetime_added** | **datetime** |  | 
**datetime_scheduled** | **datetime, none_type** |  | 
**status** | [**Status**](Status.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


