# NumbersLookupRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_numbers** | **[str]** | Array of phone numbers in international E.164 format or national format. If national format is provided, for better validation/lookup you must use the parameter &#x60;countryIso&#x60; to provide the country code of the destination phone number. | 
**country_iso** | **str** | Two-letter country ISO of the phone number you want to lookup. If an international E.164 phone number format is provided the **countryIso** will be ignored | [optional] 
**lookup_callback_url** | **str** | A valid URL to receive results for the phone number lookup.   Note: If this parameter is set, it will overwrite the setting from [Admin Dashboard &gt; HTTP API &gt; Oauth2 &gt; Application settings](#) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


