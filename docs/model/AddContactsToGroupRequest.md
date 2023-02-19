# AddContactsToGroupRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_invalid** | **bool** | Set value &#x60;true&#x60; to not throw an error if invalid numbers are detected | [optional]  if omitted the server will use the default value of False
**country_iso** | **str** | Two-letter country ISO of the phone number you want to validate. If an international E.164 phone number format is provided the **countryIso** will be ignored | [optional] 
**phone_numbers** | [**[GroupAdd]**](GroupAdd.md) | An array of objects if you want to add custom fields data to your contacts | [optional] 


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


