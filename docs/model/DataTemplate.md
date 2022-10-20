# DataTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identifier of the template | 
**name** | **str** | Name of the template | 
**text** | **str** | Text of the template | 
**channel** | **str** | Channel for wich the template can be used | 
**type** | **str, none_type** |  | 
**rich_media** | [**RichMedia**](RichMedia.md) |  | 
**created_at** | **str** |  | 
**approved** | **bool** | Approval status of the template (for channel &#x60;sms&#x60; this variable is always &#x60;true&#x60;) | 
**locked** | **bool** | If a Viber or Whatsapp template is approved it cannot be edited, so this parameter will be **true** | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


