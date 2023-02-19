# DataSms


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msg_id** | **str** | Unique message identifier needed to track the delivery report | 
**status** | **str** | Possible status of the message at request time:  * &#x60;ACCEPTED&#x60; - Message has been accepted for delivery  * &#x60;SCHEDULED&#x60; - Message has been scheduled at the date time specified  * &#x60;REJECTED&#x60; - Message was rejected because the number has opted out from receiving messages (no balance deduction, cost zero)  * &#x60;NO COVERAGE&#x60; - There is no coverage for this destination or no pricing is set (no balance deduction, cost zero)   The final delivery report (DELIVERED, FAILED) will be sent to the URL provided in the &#x60;dlrCallbackUrl&#x60; parameter or you can query the status at the resource GET &#x60;/reports/single/{msgId}&#x60;  | 
**status_code** | **int** | Status code for the delivery report  | 
**error_code** | **int, none_type** | Status code for the failed delivery report  | 
**created_at** | **datetime** | Date and time of sending the message | 
**in_quiet_hours** | **bool** | If the date of send or the schedule date of a message is detected to be in the quiet hours of the destination phone number, this parameter will be set to &#x60;true&#x60;. This parameter is &#x60;false&#x60; if no quiet hours detected | 
**cost** | **float** | The cost of sending a message, in the currency of the account (**eur** or **usd**). It is calculated as ***cost per message part x parts***. Eg. 3 x 0.041 &#x3D; 0.123  &lt;br&gt;This parameter has value zero (0) if the status of the message is &#x60;REJECTED&#x60; or &#x60;NO COVERAGE&#x60;  | 
**to** | **str** | Destination phone number in E.164 format  | 
**country_iso** | **str** | Two-letter country code in ISO-3166 alpha 2 standard of the destinations. Eg. DE, FR, IT | 
**_from** | **str** | Originator (sender name) of the message  | 
**text** | **str** | The text message sent with all the fields/variables replaced (if any). | 
**parts** | **int** | Message parts | 
**text_analysis** | [**TextAnalysis**](TextAnalysis.md) |  | 
**track_data** | **str** | Client own UUID (v1-v5) provided to track messages | [optional] 
**scheduled_at** | **datetime** | Date and time when the message was scheduled. If the date and time of sending or scheduling is detected to be in the quiet hours interval, the API will schedule the sending of the SMS at the end of the quiet hours. Eg. If quiet hours is defined between 21:30 and 09:30 and the message sending is at 21:55, then the API will schedule the message the next day at 09:31 | [optional] 


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


