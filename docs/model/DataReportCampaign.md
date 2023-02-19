# DataReportCampaign


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msg_id** | **str** | Unique message identifier | 
**status** | **str** | Delivery report of the message  | 
**status_code** | **int** | Status code for the delivery report  | 
**error_code** | **int, none_type** | Status code for the failed delivery report  | 
**in_quiet_hours** | **bool** | Specified if the sending was between the saved quiet hours  | 
**created_at** | **datetime** | Date and time of sending the message | 
**updated_at** | **datetime, none_type** | Date and time of last delivery report update of the message | 
**cost** | **float** | The cost of sending a message, in the currency of the account (**eur** or **usd**). It is calculated as ***cost per message part x parts***. Eg. 3 x 0.041 &#x3D; 0.123  &lt;br&gt;This parameter has value zero (0) if the status of the message is &#x60;REJECTED&#x60; or &#x60;NO COVERAGE&#x60;  | 
**to** | **str** | Destination phone number in E.164 format  | 
**country_iso** | **str** | Two-letter country code in ISO-3166 alpha 2 standard of the destinations. Eg. DE, FR, IT | 
**_from** | **str** | Originator (sender name) of the message  | 
**text** | **str** | Content of the message | 
**source** | **str** | Source of the message sending | 
**channel** | **str** | Channel that sent the message | 
**text_analysis** | [**TextAnalysis**](TextAnalysis.md) |  | 
**scheduled_at** | **datetime, none_type** | Date and time when the message was scheduled | [optional] 


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


