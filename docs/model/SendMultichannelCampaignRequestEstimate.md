# SendMultichannelCampaignRequestEstimate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **[int]** | An array of identifiers for groups of contacts | 
**_from** | **str** | The originator (sender name) of the text message (min 3, max 11 characters). If the originator used in this value is not approved, it will be overwritten by a default system originator (eg. InfoText). Read more about [sender names](#) | 
**strategy** | [**[Strategy]**](Strategy.md) | An array of objects, in the order of sending. The API will try sending the message with the first channel in the strategy. If the delivery failed (Eg. Viber not installed, &#x60;ttl&#x60; has expired), then it will trigger the sending with the next channel in the strategy object. The last failover object must be always &#x60;sms&#x60;. Possible values for &#x60;strategy.channel&#x60;: &#x60;viber&#x60;, &#x60;whatsapp&#x60;, &#x60;sms&#x60;. Objects with channel &#x60;viber&#x60; and &#x60;whatsapp&#x60; have element &#x60;templateId&#x60; (the ID of the approved text template), and failover object with channel &#x60;sms&#x60; have the element &#x60;text&#x60; | 
**ttl** | **int** | The time to live (ttl) defines the time in seconds that a channel has to deliver the message to the destination. After the time to live has expired and no &#x60;Delivered&#x60; report received, the next channel in the strategy will be triggered. This procedure is repeated until the last failover channel (&#x60;sms&#x60;) is triggered. Default &#x60;ttl&#x60; is 300 seconds (5 minutes). Max value 1209600 seconds (14 days) | [optional]  if omitted the server will use the default value of 300
**scheduled_date** | **datetime** | If you want to schedule the Multichannel message at a later date. The date provided must be in format **YYYY-MM-DD HH:MM:SS** (Eg. 2021-06-23 14:26:10). By default, the date and time in this parameter is treated as &#x60;UTC&#x60;. So if you want to schedule a Multichannel message to a french phone number at 16:00 (France is UTC+2), then you should set the parameter at 2021-06-23 14:00 (UTC). If you don&#39;t want to make the calculations, you can set this parameter as the date time of the destination (eg. 2021-06-23 16:00) and set the parameter &#x60;isUtc&#x60; to &#x60;false&#x60;. In this way, the API will automatically make the conversion from the destination timezone to UTC and set the scheduledDate accordingly | [optional] 
**is_utc** | **bool** | If set to &#x60;false&#x60; it will indicate that the &#x60;scheduledDate&#x60; parameter is not a date in UTC time, but the date relative to the timezone of the destination phone number. The API will calculate the offset and convert the date to UTC.   | [optional]  if omitted the server will use the default value of True
**dlr_callback_url** | **str** | A valid URL to receive the delivery report update for the sent Multichannel message. If this parameter is set, it will overwrite the setting from [Admin Dashboard &gt; HTTP API &gt; Oauth2 &gt; Application settings](#) | [optional] 
**short_response** | **bool** | If set to &#x60;true&#x60;, it will return the full &#x60;info&#x60; object and empty &#x60;data&#x60; object. For situations when you don&#39;t need the information in the &#x60;data&#x60; object and want to save bandwith | [optional]  if omitted the server will use the default value of False
**no_text_details** | **bool** | The response will not have the parameters &#x60;data.text&#x60; and &#x60;data.textAnalysis&#x60;. For situations when you send to large lists of phone numbers and don&#39;t need all response parameters (save bandwith) | [optional]  if omitted the server will use the default value of False
**show_timezone** | **bool** | Shows the parameter &#x60;timezone&#x60; in the response, for each phone number | [optional]  if omitted the server will use the default value of False


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


