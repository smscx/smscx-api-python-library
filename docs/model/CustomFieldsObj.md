# CustomFieldsObj

An object with **key-value** pairs, where the key is the name of the custom field.  An actual JSON object described by this might look like this:  ```json {     \"customFields\": {         \"height\": \"1.78m\",         \"orderNumber\": \"441\",         \"my_custom_field\": \"My Custom Value\"     } }   ``` Maximum 20 custom fields allowed. The data stored in the custom fields can be used in the text message by using the placeholder `{{<KEY>}}`. Eg. `{{height}}`, `{{orderNumber}}`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_field_name** | **{str: (str,)}** | The name of the custom field | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


