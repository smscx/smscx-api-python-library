# GroupAddCustomFields

The `customFields` parameter is an object with key-value pairs, where the key is the name of the custom field. Eg. you can add a customField `height`. You can add up to 20 custom fields. The data stored in the custom fields can be used in the text of the message by using the placeholder `{{<KEY>}}`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_field_name** | **{str: (str,)}** | The name of the custom field | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


