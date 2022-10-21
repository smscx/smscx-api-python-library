# Transliteration

Convert special characters from Unicode to GSM 03.38 charset, or replace them if no GSM equivalent.   Eg. `Привет` = `privet` (cyrillic), `cześć` = `czesc` (polish), `edilmiş` = `edilmis` (turkish), `bună` = `buna` (romanian)  If this parameter is set, it will overwrite the settings from [Admin Dashboard > HTTP API > Oauth2 > Application settings](#)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alphabet** | **str** | Set the alphabet for which the transliteration will be done. If &#x60;NON_GSM&#x60; is set then all characters that are not in the GSM-7 alphabet will be mapped to a similar character in the GSM alphabet. Characters that have no equivalent  in the GSM alphabet will be replaced by a question mark &#x60;?&#x60; | 
**remove_emojis** | **bool** | This is optional and defaults to &#x60;false&#x60;. If set to &#x60;true&#x60; all Emojis found in the text will be removed | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


