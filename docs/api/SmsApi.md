# smscx_client.SmsApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_scheduled_sms()**](SmsApi.md#delete_scheduled_sms) | **DELETE** /sms/scheduled/{msgId} | Delete scheduled SMS
[**delete_scheduled_sms_campaign()**](SmsApi.md#delete_scheduled_sms_campaign) | **DELETE** /sms/scheduled/campaign/{campaignId} | Delete scheduled SMS campaign
[**estimate_sms()**](SmsApi.md#estimate_sms) | **POST** /sms/estimate | Estimate new SMS
[**estimate_sms_campaign()**](SmsApi.md#estimate_sms_campaign) | **POST** /sms/campaign/estimate | Estimate SMS campaign
[**send_sms()**](SmsApi.md#send_sms) 💰 | **POST** /sms | Send SMS
[**send_sms_campaign()**](SmsApi.md#send_sms_campaign) 💰 | **POST** /sms/campaign | Send SMS campaign


# **delete_scheduled_sms()**
> DeleteScheduledMsg delete_scheduled_sms(msg_id)

Delete scheduled SMS

Delete a scheduled SMS by providing a valid identifier (`msgId`).    

The cost of the deleted scheduled SMS will be returned to the balance of the account.  

### Errors for DELETE `/sms/scheduled/{msgId}`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  403 | 1118  |  access_denied  |  Only scheduled campaigns/messages can be deleted |  
|  404 | 1100  |  not_found  |  Message ID provided was not found or is not scheduled |  
|  400 | 1115  |  invalid_param  |  Message ID provided is not valid |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import sms_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = sms_api.SmsApi(
    smscx_client.ApiClient(configuration)
)    

# Identifier of a scheduled message
msg_id = "3328fe13-2b99-4282-b62e-d891f5e452a8" 

try:
    # Delete scheduled SMS
    api_response = api_instance.delete_scheduled_sms(msg_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling SmsApi->delete_scheduled_sms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msg_id** | **str**| Identifier of a scheduled message | required

### Return type

[**DeleteScheduledMsg**](../model/DeleteScheduledMsg.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth), [BearerAuth](../../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#available-methods) [[Back to Model list]](../../README.md#models) [[Back to README]](../../README.md)

# **delete_scheduled_sms_campaign()**
> DeleteScheduledCampaign delete_scheduled_sms_campaign(campaign_id)

Delete scheduled SMS campaign

Delete a scheduled SMS campaign by providing a valid identifier (`campaignId`).    

The cost of the deleted scheduled SMS campaign will be returned to the balance of the account.    

If part of the SMS campaign has already started, only scheduled messages will be deleted. Messages already sent cannot be deleted.

### Errors for DELETE `/sms/scheduled/campaign/{campaignId}`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  403 | 1118  |  access_denied  |  Only scheduled campaigns/messages can be deleted |  
|  404 | 1150  |  not_found  |  Campaign ID provided was not found or is not scheduled |  
|  400 | 1155  |  invalid_param  |  Campaign ID provided is not valid |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import sms_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = sms_api.SmsApi(
    smscx_client.ApiClient(configuration)
)    

# Identifier of a scheduled SMS campaign
campaign_id = "cbb72a72-0dfa-4288-b3d0-05fab904f0b2" 

try:
    # Delete scheduled SMS campaign
    api_response = api_instance.delete_scheduled_sms_campaign(campaign_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling SmsApi->delete_scheduled_sms_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Identifier of a scheduled SMS campaign | required

### Return type

[**DeleteScheduledCampaign**](../model/DeleteScheduledCampaign.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth), [BearerAuth](../../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#available-methods) [[Back to Model list]](../../README.md#models) [[Back to README]](../../README.md)

# **estimate_sms()**
> SendSmsMessageResponse estimate_sms(send_sms_request_estimate)

Estimate new SMS

Estimate the cost of sending a SMS message.

### Errors for POST `/sms/estimate`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1104  |  invalid_param  | The parameter `to` is empty or not set |  
|  400 | 1105  |  invalid_param  |  The parameter `from` is empty or not set |  
|  400 | 1106  |  invalid_param  |  The parameter `from` is not valid (min 3, max 15 characters) |  
|  400 | 1107  |  invalid_param  |  The parameter `text` is empty or not set |  
|  400 | 1108  |  invalid_param  |  The parameter `scheduledDate` is not a valid date |  
|  400 | 1109  |  invalid_param  |  The parameter `dlrCallbackUrl` is not a valid URL |  
|  400 | 1112  |  invalid_param  |  The shortlink/attachment ID provided for tracking is invalid or not found |  
|  400 | 1116  |  invalid_param  |  The scheduled date is in the past |  
|  400 | 1103  |  invalid_param  |  The phone numbers array is too big (max. allowed: 25000 numbers) |  
|  400 | 1207  |  invalid_param  | The phone number provided is not valid |  
|  400 | 1210  |  invalid_param  |  The phone numbers provided are invalid |  
|  403 | 1119  |  no_coverage  |  No coverage or restricted destination |  
|  400 | 1113  |  insufficient_credit  |  Insufficient credit |  
|  400 | 1114  |  insufficient_credit  |  Credit limit reached. To increase the credit limit, please contact your account manager |  
| 400 | 1110 | invalid_param | Invalid alphabet. Must be one of: `NONE`, `NON_GSM`, `RUSSIAN_CYRILLIC`, `BULGARIAN_CYRILLIC`, `UKRAINIAN_CYRILLIC`, `MACEDONIAN_CYRILLIC`, `BELARUSIAN_CYRILLIC`, `SERBIAN_CYRILLIC`, `POLISH`, `ROMANIAN`, `TURKISH`, `GREEK` |  
| 400 | 1135 | invalid_param | The parameter \\'transliteration\\' should be an object |   
| 400 | 1503 | invalid_param | The parameter `removeEmojis` is not boolean (true or false) |  
|  400 | 1136  |  invalid_param  |  Invalid number of characters for the placeholder {{numbers}} |  
|  400 | 1136  |  invalid_param  |  Invalid number of characters for the placeholder {{letters}} |  
|  400 | 1136  |  invalid_param  |  Invalid number of characters for the placeholder {{alphanumeric}} |  
|  400 | 1137  |  invalid_param  |  Number of characters for placeholders can be between 1 and 20 |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import sms_api
from smscx_client.model.send_sms_request_estimate import SendSmsRequestEstimate
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = sms_api.SmsApi(
    smscx_client.ApiClient(configuration)
)    
send_sms_request_estimate = SendSmsRequestEstimate(
        to=[
            "+336122464xx",
        ],
        _from="InfoText",
        text="This is test message",
        country_iso="FR",
        allow_invalid=False,
        #scheduled_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        #is_utc=True,
        dlr_callback_url="https://webhook/receive-sms-delivery-reports",
        #track_data="bf325375-e030-fccb-a009-17317c574773",
        #short_response=False,
        #no_text_details=False,
        #show_timezone=False,
        transliteration=Transliteration(
            alphabet="NONE",
            remove_emojis=False,
        ),
    )

try:
    # Estimate new SMS
    api_response = api_instance.estimate_sms(send_sms_request_estimate)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling SmsApi->estimate_sms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_sms_request_estimate** | [**SendSmsRequestEstimate**](../model/SendSmsRequestEstimate.md)|  | required

### Return type

[**SendSmsMessageResponse**](../model/SendSmsMessageResponse.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth), [BearerAuth](../../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-Id -  <br>  * X-Response-Time -  <br>  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#available-methods) [[Back to Model list]](../../README.md#models) [[Back to README]](../../README.md)

# **estimate_sms_campaign()**
> SendSmsCampaignResponse estimate_sms_campaign(send_sms_campaign_request_estimate)

Estimate SMS campaign

Estimate the cost of sending a SMS message to groups of phone numbers.

### Errors for POST `/sms/campaign/estimate`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1101  |  invalid_param  |  The parameter `groups` is empty or not set |  
|  400 | 1140  |  invalid_param  |  Group ID is not a valid group |  
|  400 | 1102  |  invalid_param  |  Group is empty |  
|  400 | 1103  |  invalid_param  |  The phone numbers array is too big (max. allowed: 25000 numbers) |  
|  400 | 1105  |  invalid_param  |  The parameter `from` is empty or not set |  
|  400 | 1106  |  invalid_param  |  The parameter `from` is not valid (min 3, max 15 characters) |  
|  400 | 1107  |  invalid_param  |  The parameter `text` is empty or not set |  
|  400 | 1108  |  invalid_param  |  The parameter `scheduledDate` is not a valid date |  
|  400 | 1109  |  invalid_param  |  The parameter `dlrCallbackUrl` is not a valid URL |  
|  400 | 1112  |  invalid_param  |  The shortlink/attachment ID provided for tracking is invalid or not found |  
|  400 | 1116  |  invalid_param  |  The scheduled date is in the past |  
|  403 | 1119  |  no_coverage  |  No coverage or restricted destination |  
|  400 | 1113  |  insufficient_credit  |  Insufficient credit |  
|  400 | 1114  |  insufficient_credit  |  Credit limit reached. To increase the credit limit, please contact your account manager |  
| 400 | 1110 | invalid_param | Invalid alphabet. Must be one of: `NONE`, `NON_GSM`, `RUSSIAN_CYRILLIC`, `BULGARIAN_CYRILLIC`, `UKRAINIAN_CYRILLIC`, `MACEDONIAN_CYRILLIC`, `BELARUSIAN_CYRILLIC`, `SERBIAN_CYRILLIC`, `POLISH`, `ROMANIAN`, `TURKISH`, `GREEK` |  
| 400 | 1135 | invalid_param | The parameter \\'transliteration\\' should be an object |   
| 400 | 1503 | invalid_param | The parameter `removeEmojis` is not boolean (true or false) |  
|  400 | 1136  |  invalid_param  |  Invalid number of characters for the placeholder {{numbers}} |  
|  400 | 1136  |  invalid_param  |  Invalid number of characters for the placeholder {{letters}} |  
|  400 | 1136  |  invalid_param  |  Invalid number of characters for the placeholder {{alphanumeric}} |  
|  400 | 1137  |  invalid_param  |  Number of characters for placeholders can be between 1 and 20 |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import sms_api
from smscx_client.model.send_sms_campaign_request_estimate import SendSmsCampaignRequestEstimate
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = sms_api.SmsApi(
    smscx_client.ApiClient(configuration)
)    
send_sms_campaign_request_estimate = SendSmsCampaignRequestEstimate(
        groups=[
            1,
        ],
        _from="InfoText",
        text="This is example test",
        #scheduled_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        #is_utc=True,
        dlr_callback_url="https://webhook/receive-sms-delivery-reports",
        #short_response=False,
        #no_text_details=False,
        #show_timezone=False,
        transliteration=Transliteration(
            alphabet="NONE",
            remove_emojis=False,
        ),
    ) # SendSmsCampaignRequestEstimate | 

try:
    # Estimate SMS campaign
    api_response = api_instance.estimate_sms_campaign(send_sms_campaign_request_estimate)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling SmsApi->estimate_sms_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_sms_campaign_request_estimate** | [**SendSmsCampaignRequestEstimate**](../model/SendSmsCampaignRequestEstimate.md)|  | required

### Return type

[**SendSmsCampaignResponse**](../model/SendSmsCampaignResponse.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth), [BearerAuth](../../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-Id -  <br>  * X-Response-Time -  <br>  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#available-methods) [[Back to Model list]](../../README.md#models) [[Back to README]](../../README.md)

# **send_sms()**<span>💰</span>
> SendSmsMessageResponse send_sms(send_sms_message_request)

Send SMS

Sends SMS to a single phone number or to a list of phone numbers.    

This endpoint was designed to handle big data objects (up to 25.000 SMS in one request).    

If you have loops or iterations we recommend building the send object in your application, and make a single request to this endpoint. The time of making the requests will decrease - by doing a single request with multiple send objects vs making requests in a loop -  and you won't have to worry about making concurrent API calls.    

> Note: This endpoint accepts idempotent requests by providing an additional `idempotencyId` parameter in body with a unique value generated by the client of type UUID v1-v5. To confirm that the server understood the request, the response will contain the header `X-Idempotency-Id` with your unique value.  By using idempotency you can retry requests in case of network error or server not responding in time, without accidentally performing the same operation twice and have a guarantee of not being billed twice.   

### Errors for POST `/sms`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1103  |  invalid_param  |  The phone numbers array is too big (max. allowed: 25000 numbers) |  
|  400 | 1104  |  invalid_param  | The parameter `to` is empty or not set |  
|  400 | 1105  |  invalid_param  |  The parameter `from` is empty or not set |  
|  400 | 1106  |  invalid_param  |  The parameter `from` is not valid (min 3, max 15 characters) |  
|  400 | 1107  |  invalid_param  |  The parameter `text` is empty or not set |  
|  400 | 1108  |  invalid_param  |  The parameter `scheduledDate` is not a valid date |  
|  400 | 1109  |  invalid_param  |  The parameter `dlrCallbackUrl` is not a valid URL |  
|  400 | 1111  |  invalid_param  |  Idempotency Id provided is not a valid UUID (v1-v5) |  
|  400 | 1112  |  invalid_param  |  The shortlink/attachment ID provided for tracking is invalid or not found |  
|  400 | 1116  |  invalid_param  |  The scheduled date is in the past |  
|  400 | 1207  |  invalid_param  | The phone number provided is not valid |  
|  400 | 1210  |  invalid_param  |  The phone numbers provided are invalid |  
|  400 | 1113  |  insufficient_credit  |  Insufficient credit |  
|  400 | 1114  |  insufficient_credit  |  Credit limit reached. To increase the credit limit, please contact your account manager |  
| 400 | 1110 | invalid_param | Invalid alphabet. Must be one of: `NONE`, `NON_GSM`, `RUSSIAN_CYRILLIC`, `BULGARIAN_CYRILLIC`, `UKRAINIAN_CYRILLIC`, `MACEDONIAN_CYRILLIC`, `BELARUSIAN_CYRILLIC`, `SERBIAN_CYRILLIC`, `POLISH`, `ROMANIAN`, `TURKISH`, `GREEK` |  
| 400 | 1135 | invalid_param | The parameter \\'transliteration\\' should be an object |   
| 400 | 1503 | invalid_param | The parameter `removeEmojis` is not boolean (true or false) |  
|  400 | 1136  |  invalid_param  |  Invalid number of characters for the placeholder {{numbers}} |  
|  400 | 1136  |  invalid_param  |  Invalid number of characters for the placeholder {{letters}} |  
|  400 | 1136  |  invalid_param  |  Invalid number of characters for the placeholder {{alphanumeric}} |  
|  400 | 1137  |  invalid_param  |  Number of characters for placeholders can be between 1 and 20 |  
|  403 | 1119  |  no_coverage  |  No coverage or restricted destination |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import sms_api
from smscx_client.model.send_sms_message_request import SendSmsMessageRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = sms_api.SmsApi(
    smscx_client.ApiClient(configuration)
)    
send_sms_message_request = SendSmsMessageRequest(
        to=[
            "+359485721xx",
            "+4474006003xx",
            "+417813350xx",
            "+3584129058xx",
            "+3931238638xx",
            "+316122393xx",
            "+3519121547xx",
            "+336125151xx",
            "+791236471xx",
            "+3069121512xx",
            "+301xx",
        ],
        _from="InfoText",
        text="This is text example {{optoutLink}}",
        #country_iso="FR",
        allow_invalid=True,
        #scheduled_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        #is_utc=True,
        dlr_callback_url="https://webhook/receive-sms-delivery-reports",
        #track_data="bf325375-e030-fccb-a009-17317c574773",
        #short_response=False,
        #no_text_details=False,
        #show_timezone=False,
        idempotency_id="bf325375-e030-fccb-a009-17317c574773",
        transliteration=Transliteration(
            alphabet="NONE",
            remove_emojis=False,
        ),
    ) # SendSmsMessageRequest | 

try:
    # Send SMS
    api_response = api_instance.send_sms(send_sms_message_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling SmsApi->send_sms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_sms_message_request** | [**SendSmsMessageRequest**](../model/SendSmsMessageRequest.md)|  | required

### Return type

[**SendSmsMessageResponse**](../model/SendSmsMessageResponse.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth), [BearerAuth](../../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Idempotency-Id -  <br>  * X-Request-Id -  <br>  * X-Response-Time -  <br>  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#available-methods) [[Back to Model list]](../../README.md#models) [[Back to README]](../../README.md)

# **send_sms_campaign()**<span>💰</span>
> SendSmsCampaignResponse send_sms_campaign(send_sms_campaign_request)

Send SMS campaign

Sends SMS to existing group(s) of contacts.    

> Note: This endpoint accepts idempotent requests by providing an additional `idempotencyId` parameter in body with a unique value generated by the client of type UUID v1-v5. To confirm that the server understood the request, the response will contain the header `X-Idempotency-Id` with your unique value.  By using idempotency you can retry requests in case of network error or server not responding in time, without accidentally performing the same operation twice and have a guarantee of not being billed twice.     > We recommend to always use Idempotency ID when sending SMS campaigns    

### Errors for POST `/sms/campaign`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1101  |  invalid_param  |  The parameter `groups` is empty or not set |  
|  400 | 1140  |  invalid_param  |  Group ID is not a valid group |  
|  400 | 1102  |  invalid_param  |  Group is empty |  
|  400 | 1103  |  invalid_param  |  The phone numbers array is too big (max. allowed: 25000 numbers) |  
|  400 | 1105  |  invalid_param  |  The parameter `from` is empty or not set |  
|  400 | 1106  |  invalid_param  |  The parameter `from` is not valid (min 3, max 15 characters) |  
|  400 | 1107  |  invalid_param  |  The parameter `text` is empty or not set |  
|  400 | 1108  |  invalid_param  |  The parameter `scheduledDate` is not a valid date |  
|  400 | 1109  |  invalid_param  |  The parameter `dlrCallbackUrl` is not a valid URL |  
|  400 | 1111  |  invalid_param  |  Idempotency Id provided is not a valid UUID (v1-v5) |  
|  400 | 1112  |  invalid_param  |  The shortlink/attachment ID provided for tracking is invalid or not found |  
|  400 | 1116  |  invalid_param  |  The scheduled date is in the past |  
|  400 | 1113  |  insufficient_credit  |  Insufficient credit |  
|  400 | 1114  |  insufficient_credit  |  Credit limit reached. To increase the credit limit, please contact your account manager |  
| 400 | 1110 | invalid_param | Invalid alphabet. Must be one of: `NONE`, `NON_GSM`, `RUSSIAN_CYRILLIC`, `BULGARIAN_CYRILLIC`, `UKRAINIAN_CYRILLIC`, `MACEDONIAN_CYRILLIC`, `BELARUSIAN_CYRILLIC`, `SERBIAN_CYRILLIC`, `POLISH`, `ROMANIAN`, `TURKISH`, `GREEK` |  
| 400 | 1135 | invalid_param | The parameter \\'transliteration\\' should be an object |   
| 400 | 1503 | invalid_param | The parameter `removeEmojis` is not boolean (true or false) |  
|  400 | 1136  |  invalid_param  |  Invalid number of characters for the placeholder {{numbers}} |  
|  400 | 1136  |  invalid_param  |  Invalid number of characters for the placeholder {{letters}} |  
|  400 | 1136  |  invalid_param  |  Invalid number of characters for the placeholder {{alphanumeric}} |  
|  400 | 1137  |  invalid_param  |  Number of characters for placeholders can be between 1 and 20 |  
|  403 | 1119  |  no_coverage  |  No coverage or restricted destination |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import sms_api
from smscx_client.model.model403_no_coverage import Model403NoCoverage
from smscx_client.model.send_sms_campaign_request import SendSmsCampaignRequest
from smscx_client.model.model400_invalid_param import Model400InvalidParam
from smscx_client.model.model500_server_error import Model500ServerError
from smscx_client.model.model401_unauthorized import Model401Unauthorized
from smscx_client.model.send_sms_campaign_response import SendSmsCampaignResponse
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = sms_api.SmsApi(
    smscx_client.ApiClient(configuration)
)    
send_sms_campaign_request = SendSmsCampaignRequest(
        groups=[
            1,
        ],
        _from="_from_example",
        text="Hello {{firstName}} {{lastName}} This is example text {{optoutLink}}",
        #scheduled_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        #is_utc=True,
        dlr_callback_url="https://webhook/receive-sms-delivery-reports",
        #short_response=False,
        #no_text_details=False,
        #show_timezone=False,
        idempotency_id="bf325375-e030-fccb-a009-17317c574773",
        transliteration=Transliteration(
            alphabet="NONE",
            remove_emojis=False,
        ),
    ) # SendSmsCampaignRequest | 

try:
    # Send SMS campaign
    api_response = api_instance.send_sms_campaign(send_sms_campaign_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling SmsApi->send_sms_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_sms_campaign_request** | [**SendSmsCampaignRequest**](../model/SendSmsCampaignRequest.md)|  | required

### Return type

[**SendSmsCampaignResponse**](../model/SendSmsCampaignResponse.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth), [BearerAuth](../../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Idempotency-Id -  <br>  * X-Request-Id -  <br>  * X-Response-Time -  <br>  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#available-methods) [[Back to Model list]](../../README.md#models) [[Back to README]](../../README.md)

