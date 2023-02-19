# SendWhatsappMessageRequestEstimate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **[str]** | A string with single phone number or an array of phone numbers in international E.164 format or national format. If national format is provided, for better validation you must use the parameter &#x60;countryIso&#x60; to provide the country code of the destination phone number. | 
**_from** | **str** | The originator (sender name) of the text message (min 3, max 15 characters). If the originator used in this value is not approved, it will be overwritten by a default system originator (eg. InfoText). Read more about [sender names](#) | 
**template_id** | **int** | Identifier of the approved Viber template | 
**custom_fields** | [**CustomFields**](CustomFields.md) |  | [optional] 
**country_iso** | **str** | Country ISO (two-letter) of the destination phone numbers (if provided in national format). Please note that if an international E.164 phone number format is provided in the &#x60;to&#x60; parameter, the **countryIso** will be ignored. Eg. **FR** for France, **GB** for United Kingdom. Note: It is \&quot;GB\&quot;, not \&quot;UK\&quot;, as per the ISO-3166 alpha 2. | [optional] 
**allow_invalid** | **bool** | By default an error will be thrown if any invalid numbers are detected in the &#x60;to&#x60; parameter. Set this parameter to &#x60;true&#x60; if you want to process the request even if invalid numbers are detected. The response will contain in the &#x60;info&#x60; object the property &#x60;invalid&#x60;, wich is an array with the detected invalid phone numbers | [optional]  if omitted the server will use the default value of False
**scheduled_date** | **datetime** | If you want to schedule the Whatsapp message at a later date. The date provided must be in format **YYYY-MM-DD HH:MM:SS** (Eg. 2021-06-23 14:26:10). By default, the date and time in this parameter is treated as &#x60;UTC&#x60;. So if you want to schedule a Whatsapp message to a french phone number at 16:00 (France is UTC+2), then you should set the parameter at 2021-06-23 14:00 (UTC). If you don&#39;t want to make the calculations, you can set this parameter as the date time of the destination (eg. 2021-06-23 16:00) and set the parameter &#x60;isUtc&#x60; to &#x60;false&#x60;. In this way, the API will automatically make the conversion from the destination timezone to UTC and set the scheduledDate accordingly | [optional] 
**is_utc** | **bool** | If set to &#x60;false&#x60; it will indicate that the &#x60;scheduledDate&#x60; parameter is not a date in UTC time, but the date relative to the timezone of the destination phone number. The API will calculate the offset and convert the date to UTC.   | [optional]  if omitted the server will use the default value of True
**dlr_callback_url** | **str** | A valid URL to receive the delivery report update for the sent Whatsapp message. If this parameter is set, it will overwrite the setting from [Admin Dashboard &gt; HTTP API &gt; Oauth2 &gt; Application settings](#) | [optional] 
**track_data** | **str** | Allows to track messages a client provided ID. The &#x60;trackData&#x60; value will be passed back with the response and in all callbacks (webhooks). If the value is not a valid UUID (v1-v5) the API will not return an error but will discard this parameter | [optional] 
**short_response** | **bool** | If set to &#x60;true&#x60;, it will return the full &#x60;info&#x60; object and empty &#x60;data&#x60; object. For situations when you don&#39;t need the information in the &#x60;data&#x60; object and want to save bandwith | [optional]  if omitted the server will use the default value of False
**no_text_details** | **bool** | The response will not have the parameters &#x60;data.text&#x60; and &#x60;data.textAnalysis&#x60;. For situations when you send to large lists of phone numbers and don&#39;t need all response parameters (save bandwith) | [optional]  if omitted the server will use the default value of False
**show_timezone** | **bool** | Shows the parameter &#x60;timezone&#x60; in the response, for each phone number | [optional]  if omitted the server will use the default value of False


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


