# CustomFields

An object with **key-value** pairs, where the key is the name of the custom field.  An actual JSON object described by this might look like this:  ```json {     \"customFields\": {         \"height\": \"1.78m\",         \"orderNumber\": \"441\",         \"my_custom_field\": \"My Custom Value\"     } }   ``` The data stored in the custom fields will be inserted in the text message template by replacing the placeholder `{{<KEY>}}`. Eg. `{{height}}`, `{{orderNumber}}`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_field_name** | **{str: (str,)}** | The name of the custom field | 


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


