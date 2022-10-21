# smscx_client.MultichannelApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_scheduled_multichannel_campaign()**](MultichannelApi.md#delete_scheduled_multichannel_campaign) | **DELETE** /multichannel/scheduled/campaign/{campaignId} | Delete scheduled Multichannel campaign
[**delete_scheduled_multichannel_message()**](MultichannelApi.md#delete_scheduled_multichannel_message) | **DELETE** /multichannel/scheduled/{msgId} | Delete scheduled Multichannel message
[**estimate_multichannel_campaign()**](MultichannelApi.md#estimate_multichannel_campaign) | **POST** /multichannel/campaign/estimate | Estimate Multichannel campaign
[**estimate_multichannel_message()**](MultichannelApi.md#estimate_multichannel_message) | **POST** /multichannel/estimate | Estimate Multichannel message
[**send_multichannel_campaign()**](MultichannelApi.md#send_multichannel_campaign) 💰 | **POST** /multichannel/campaign | Send Multichannel campaign
[**send_multichannel_message()**](MultichannelApi.md#send_multichannel_message) 💰 | **POST** /multichannel | Send Multichannel message


# **delete_scheduled_multichannel_campaign()**
> DeleteScheduledCampaign delete_scheduled_multichannel_campaign(campaign_id)

Delete scheduled Multichannel campaign

Delete a scheduled Multichannel campaign by providing a valid identifier (`campaignId`).    

The cost of the deleted scheduled Multichannel campaign will be returned to the balance of the account.    

If part of the Multichannel campaign has already started, only scheduled messages will be deleted. Messages already sent cannot be deleted.

### Errors for DELETE `/multichannel/scheduled/campaign/{campaignId}`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1155  |  invalid_param  |  Campaign ID provided is not valid |
|  403 | 1118  |  access_denied  |  Only scheduled campaigns/messages can be deleted |  
|  404 | 1150  |  not_found  |  Campaign ID provided was not found or is not scheduled |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import multichannel_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = multichannel_api.MultichannelApi(
    smscx_client.ApiClient(configuration)
)    
campaign_id = "9f90f919-9b19-43db-921f-c8e05ae7054c"

try:
    # Delete scheduled Multichannel campaign
    api_response = api_instance.delete_scheduled_multichannel_campaign(campaign_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling MultichannelApi->delete_scheduled_multichannel_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Identifier of a scheduled Multichannel campaign | required

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

# **delete_scheduled_multichannel_message()**
> DeleteScheduledMsg delete_scheduled_multichannel_message(msg_id)

Delete scheduled Multichannel message

Delete a scheduled Multichannel message by providing a valid identifier (`msgId`).

The cost of the deleted scheduled Multichannel message will be returned to the balance of the account. 
  
### Errors for DELETE `/multichannel/scheduled/{msgId}`

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1115  |  invalid_param  |  Message ID provided is not valid |
|  403 | 1118  |  access_denied  |  Only scheduled campaigns/messages can be deleted |  
|  404 | 1100  |  not_found  |  Message ID provided was not found or is not scheduled |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import multichannel_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = multichannel_api.MultichannelApi(
    smscx_client.ApiClient(configuration)
)    
msg_id = "396d2afa-1440-4f36-a365-b99a5ceaea23"

try:
    # Delete scheduled Multichannel message
    api_response = api_instance.delete_scheduled_multichannel_message(msg_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling MultichannelApi->delete_scheduled_multichannel_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msg_id** | **str**| Identifier of a scheduled Multichannel message | required

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

# **estimate_multichannel_campaign()**
> SendMultichannelCampaignResponse estimate_multichannel_campaign(send_multichannel_campaign_request_estimate)

Estimate Multichannel campaign

Estimate the cost of sending a Multichannel message to groups of phone numbers.    

This endpoint is identical to `/multichannel/campaign` endpoint, but it will only simulate the Multichannel sending (no billing).    

The request body and the response are the same as for `/multichannel/campaign` endpoint.

### Errors for POST `/multichannel/campaigns/estimate`

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1101  |  invalid_param  |  The parameter `groups` is empty or not set |  
|  400 | 1140  |  invalid_param  |  Group ID is not a valid group |  
|  400 | 1102  |  invalid_param  |  Group is empty |  
|  400 | 1103  |  invalid_param  |  The phone numbers array is too big (max. allowed: 25000 numbers) |  
|  400 | 1105  |  invalid_param  |  The parameter `from` is empty or not set |  
|  400 | 1106  |  invalid_param  |  The parameter `from` is not valid (min 3, max 11 characters) |  
|  400 | 1107  |  invalid_param  |  The parameter `text` is empty or not set |  
|  400 | 1108  |  invalid_param  |  The parameter `scheduledDate` is not a valid date |  
|  400 | 1109  |  invalid_param  |  The parameter `dlrCallbackUrl` is not a valid URL |  
|  400 | 1112  |  invalid_param  |  The shortlink/attachment ID provided for tracking is invalid or not found |  
|  400 | 1116  |  invalid_param  |  The scheduled date is in the past |  
|  400 | 1103  |  invalid_param  |  The phone numbers array is too big (max. allowed: 25000 numbers) |  
|  400 | 1113  |  insufficient_credit  |  Insufficient credit |  
|  400 | 1114  |  insufficient_credit  |  Credit limit reached. To increase the credit limit, please contact your account manager |  
|  400 | 1124  |  invalid_param  |  The parameter `ttl` is not a number |  
|  400 | 1125  |  invalid_param  |  Min value for `ttl` is 300 seconds |  
|  400 | 1134  |  invalid_param  |  Max value for `ttl` is 1209600 seconds (14 days) |  
|  400 | 1120  |  invalid_param  |  The parameter `strategy` is empty or not set |  
|  400 | 1121  |  invalid_param  |  The parameter `strategy` must have at least two channels |  
|  400 | 1122  |  invalid_param  |  The parameter `strategy` must have channel `sms` as last element |  
|  400 | 1129  |  invalid_param  |  The parameter `strategy` contains duplicate channels |  
|  400 | 1123  |  invalid_param  |  The parameter `channel` is not valid. Allowed values: |  
|  400 | 1126  |  invalid_param  |  The parameter `templateId` is not set |  
|  400 | 1127  |  invalid_param  |  The parameter `templateId` is not valid |  
|  400 | 1128  |  invalid_param  |  The template ID provided is not a valid template |  
|  400 | 1130  |  insufficient_credit  |  Insufficient credit for failover sending |
|  403 | 1132  |  access_denied  |  The template ID provided is not approved |  
|  403 | 1133  |  access_denied  |  The template ID provided is not locked |  
|  403 | 1119  |  no_coverage  |  No coverage or restricted destination |  
|  403 | 1131  |  access_denied  |  The strategy contains channels that are not active: |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import multichannel_api
from smscx_client.model.send_multichannel_campaign_request_estimate import SendMultichannelCampaignRequestEstimate
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = multichannel_api.MultichannelApi(
    smscx_client.ApiClient(configuration)
)    
send_multichannel_campaign_request_estimate = SendMultichannelCampaignRequestEstimate(
        groups=[
            1,
        ],
        _from="_from_example",
        strategy=[
            Strategy(
                channel="viber",
                template_id=1,
                text="text_example",
            ),
        ],
        ttl=300,
        scheduled_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        is_utc=True,
        dlr_callback_url="dlr_callback_url_example",
        short_response=False,
        no_text_details=False,
        show_timezone=False,
    )

try:
    # Estimate Multichannel campaign
    api_response = api_instance.estimate_multichannel_campaign(send_multichannel_campaign_request_estimate)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling MultichannelApi->estimate_multichannel_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_multichannel_campaign_request_estimate** | [**SendMultichannelCampaignRequestEstimate**](../model/SendMultichannelCampaignRequestEstimate.md)|  | required

### Return type

[**SendMultichannelCampaignResponse**](../model/SendMultichannelCampaignResponse.md)

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

# **estimate_multichannel_message()**
> SendMultichannelMessageResponse estimate_multichannel_message(send_multichannel_message_request_estimate)

Estimate Multichannel message

Estimate the cost of sending a Multichannel message.    

This endpoint is identical to `/multichannel` endpoint, but it will only simulate the Multichannel sending (no billing).    

The request body and the response are the same as for `/multichannel` endpoint.

### Errors for POST `/multichannel/estimate`

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1104  |  invalid_param  | The parameter `to` is empty or not set |  
|  400 | 1105  |  invalid_param  |  The parameter `from` is empty or not set |  
|  400 | 1106  |  invalid_param  |  The parameter `from` is not valid (min 3, max 11 characters) |  
|  400 | 1107  |  invalid_param  |  The parameter `text` is empty or not set |  
|  400 | 1108  |  invalid_param  |  The parameter `scheduledDate` is not a valid date |  
|  400 | 1109  |  invalid_param  |  The parameter `dlrCallbackUrl` is not a valid URL |  
|  400 | 1112  |  invalid_param  |  The shortlink/attachment ID provided for tracking is invalid or not found |  
|  400 | 1116  |  invalid_param  |  The scheduled date is in the past |  
|  400 | 1103  |  invalid_param  |  The phone numbers array is too big (max. allowed: 25000 numbers) |  
|  400 | 1207  |  invalid_param  | The phone number provided is not valid |  
|  400 | 1210  |  invalid_param  |  The phone numbers provided are invalid |  |  403 | 1119  |  no_coverage  |  No coverage or restricted destination |  
|  400 | 1113  |  insufficient_credit  |  Insufficient credit |  
|  400 | 1114  |  insufficient_credit  |  Credit limit reached. To increase the credit limit, please contact your account manager |  
|  400 | 1130  |  insufficient_credit  |  Insufficient credit for failover sending |  
|  400 | 1124  |  invalid_param  |  The parameter `ttl` is not a number |  
|  400 | 1125  |  invalid_param  |  Min value for `ttl` is 300 seconds |  
|  400 | 1134  |  invalid_param  |  Max value for `ttl` is 1209600 seconds (14 days) |  
|  400 | 1120  |  invalid_param  |  The parameter `strategy` is empty or not set |  
|  400 | 1121  |  invalid_param  |  The parameter `strategy` must have at least two channels |  
|  400 | 1122  |  invalid_param  |  The parameter `strategy` must have channel `sms` as last element |  
|  400 | 1129  |  invalid_param  |  The parameter `strategy` contains duplicate channels |  
|  400 | 1123  |  invalid_param  |  The parameter `channel` is not valid. Allowed values: |  
|  400 | 1126  |  invalid_param  |  The parameter `templateId` is not set |  
|  400 | 1127  |  invalid_param  |  The parameter `templateId` is not valid |  
|  400 | 1128  |  invalid_param  |  The template ID provided is not a valid template |  
|  403 | 1132  |  access_denied  |  The template ID provided is not approved |  
|  403 | 1133  |  access_denied  |  The template ID provided is not locked |
|  403 | 1131  |  access_denied  |  The strategy contains channels that are not active: |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import multichannel_api
from smscx_client.model.send_multichannel_message_request_estimate import SendMultichannelMessageRequestEstimate
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = multichannel_api.MultichannelApi(
    smscx_client.ApiClient(configuration)
)    
send_multichannel_message_request_estimate = SendMultichannelMessageRequestEstimate(
        to=[
            "to_example",
        ],
        _from="_from_example",
        strategy=[
            Strategy(
                channel="viber",
                template_id=1,
                text="text_example",
            ),
        ],
        ttl=300,
        country_iso="country_iso_example",
        allow_invalid=False,
        scheduled_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        is_utc=True,
        dlr_callback_url="dlr_callback_url_example",
        track_data="bf325375-e030-fccb-a009-17317c574773",
        short_response=False,
        no_text_details=False,
        show_timezone=False,
    ) # SendMultichannelMessageRequestEstimate | 

try:
    # Estimate Multichannel message
    api_response = api_instance.estimate_multichannel_message(send_multichannel_message_request_estimate)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling MultichannelApi->estimate_multichannel_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_multichannel_message_request_estimate** | [**SendMultichannelMessageRequestEstimate**](../model/SendMultichannelMessageRequestEstimate.md)|  | required

### Return type

[**SendMultichannelMessageResponse**](../model/SendMultichannelMessageResponse.md)

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

# **send_multichannel_campaign()**<span>💰</span>
> SendMultichannelCampaignResponse send_multichannel_campaign(send_multichannel_campaign_request)

Send Multichannel campaign

Sends Multichannel message to existing group(s) of contacts.    

> Note: This endpoint accepts idempotent requests by providing an additional `idempotencyId` parameter in body with a unique value generated by the client of type UUID v1-v5. To confirm that the server understood the request, the response will contain the header `X-Idempotency-Id` with your unique value.  By using idempotency you can retry requests in case of network error or server not responding in time, without accidentally performing the same operation twice and have a guarantee of not being billed twice.     > We recommend to always use Idempotency ID when sending Multichannel campaigns


### Errors for POST `/multichannel/campaigns`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1101  |  invalid_param  |  The parameter `groups` is empty or not set |  
|  400 | 1140  |  invalid_param  |  Group ID is not a valid group |  
|  400 | 1102  |  invalid_param  |  Group is empty |  
|  400 | 1103  |  invalid_param  |  The phone numbers array is too big (max. allowed: 25000 numbers) |  
|  400 | 1105  |  invalid_param  |  The parameter `from` is empty or not set |  
|  400 | 1106  |  invalid_param  |  The parameter `from` is not valid (min 3, max 11 characters) |  
|  400 | 1107  |  invalid_param  |  The parameter `text` is empty or not set |  
|  400 | 1108  |  invalid_param  |  The parameter `scheduledDate` is not a valid date |  
|  400 | 1109  |  invalid_param  |  The parameter `dlrCallbackUrl` is not a valid URL |  
|  400 | 1111  |  invalid_param  |  Idempotency Id provided is not a valid UUID (v1-v5) |  
|  400 | 1112  |  invalid_param  |  The shortlink/attachment ID provided for tracking is invalid or not found |  
|  400 | 1116  |  invalid_param  |  The scheduled date is in the past |  
|  400 | 1103  |  invalid_param  |  The phone numbers array is too big (max. allowed: 25000 numbers) |  
|  400 | 1113  |  insufficient_credit  |  Insufficient credit |  
|  400 | 1114  |  insufficient_credit  |  Credit limit reached. To increase the credit limit, please contact your account manager |  
|  400 | 1124  |  invalid_param  |  The parameter `ttl` is not a number |  
|  400 | 1125  |  invalid_param  |  Min value for `ttl` is 300 seconds |  
|  400 | 1134  |  invalid_param  |  Max value for `ttl` is 1209600 seconds (14 days) |  
|  400 | 1120  |  invalid_param  |  The parameter `strategy` is empty or not set |  
|  400 | 1121  |  invalid_param  |  The parameter `strategy` must have at least two channels |  
|  400 | 1122  |  invalid_param  |  The parameter `strategy` must have channel `sms` as last element |  
|  400 | 1129  |  invalid_param  |  The parameter `strategy` contains duplicate channels |  
|  400 | 1123  |  invalid_param  |  The parameter `channel` is not valid. Allowed values: |  
|  400 | 1126  |  invalid_param  |  The parameter `templateId` is not set |  
|  400 | 1127  |  invalid_param  |  The parameter `templateId` is not valid |  
|  400 | 1128  |  invalid_param  |  The template ID provided is not a valid template |  
|  400 | 1130  |  insufficient_credit  |  Insufficient credit for failover sending |
|  403 | 1132  |  access_denied  |  The template ID provided is not approved |  
|  403 | 1133  |  access_denied  |  The template ID provided is not locked |  
|  403 | 1131  |  access_denied  |  The strategy contains channels that are not active: |  
|  403 | 1119  |  no_coverage  |  No coverage or restricted destination |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import multichannel_api
from smscx_client.model.send_multichannel_campaign_request import SendMultichannelCampaignRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = multichannel_api.MultichannelApi(
    smscx_client.ApiClient(configuration)
)    
send_multichannel_campaign_request = SendMultichannelCampaignRequest(
        groups=[
            1,
        ],
        _from="_from_example",
        strategy=[
            Strategy(
                channel="viber",
                template_id=1,
                text="text_example",
            ),
        ],
        ttl=300,
        scheduled_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        is_utc=True,
        dlr_callback_url="https://my-callback-url/endpoint",
        short_response=False,
        no_text_details=False,
        show_timezone=False,
        idempotency_id="bf325375-e030-fccb-a009-17317c574773",
    )

try:
    # Send Multichannel campaign
    api_response = api_instance.send_multichannel_campaign(send_multichannel_campaign_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling MultichannelApi->send_multichannel_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_multichannel_campaign_request** | [**SendMultichannelCampaignRequest**](../model/SendMultichannelCampaignRequest.md)|  | required

### Return type

[**SendMultichannelCampaignResponse**](../model/SendMultichannelCampaignResponse.md)

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

# **send_multichannel_message()**<span>💰</span>
> SendMultichannelMessageResponse send_multichannel_message(send_multichannel_message_request)

Send Multichannel message

Sends Multichannel message to a single phone number or to a list of phone numbers.    

This endpoint was designed to handle big data objects (up to 25.000 Multichannel messages in one request).    

If you have loops or iterations we recommend building the send object in your application, and make a single request to this endpoint. The time of making the requests will decrease - by doing a single request with multiple send objects vs making requests in a loop -  and you won't have to worry about making concurrent API calls.    

> Note: This endpoint accepts idempotent requests by providing an additional `idempotencyId` parameter in body with a unique value generated by the client of type UUID v1-v5. To confirm that the server understood the request, the response will contain the header `X-Idempotency-Id` with your unique value.  By using idempotency you can retry requests in case of network error or server not responding in time, without accidentally performing the same operation twice and have a guarantee of not being billed twice.

### Errors for POST `/multichannel`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1104  |  invalid_param  | The parameter `to` is empty or not set |  
|  400 | 1105  |  invalid_param  |  The parameter `from` is empty or not set |  
|  400 | 1106  |  invalid_param  |  The parameter `from` is not valid (min 3, max 11 characters) |  
|  400 | 1107  |  invalid_param  |  The parameter `text` is empty or not set |  
|  400 | 1108  |  invalid_param  |  The parameter `scheduledDate` is not a valid date |  
|  400 | 1109  |  invalid_param  |  The parameter `dlrCallbackUrl` is not a valid URL |  
|  400 | 1111  |  invalid_param  |  Idempotency Id provided is not a valid UUID (v1-v5) |  
|  400 | 1112  |  invalid_param  |  The shortlink/attachment ID provided for tracking is invalid or not found |  
|  400 | 1116  |  invalid_param  |  The scheduled date is in the past |  
|  400 | 1103  |  invalid_param  |  The phone numbers array is too big (max. allowed: 25000 numbers) |  
|  400 | 1207  |  invalid_param  | The phone number provided is not valid |  
|  400 | 1210  |  invalid_param  |  The phone numbers provided are invalid |  
|  400 | 1113  |  insufficient_credit  |  Insufficient credit |  
|  400 | 1114  |  insufficient_credit  |  Credit limit reached. To increase the credit limit, please contact your account manager |  
|  400 | 1130  |  insufficient_credit  |  Insufficient credit for failover sending |  
|  400 | 1124  |  invalid_param  |  The parameter `ttl` is not a number |  
|  400 | 1125  |  invalid_param  |  Min value for `ttl` is 300 seconds |  
|  400 | 1134  |  invalid_param  |  Max value for `ttl` is 1209600 seconds (14 days) |  
|  400 | 1120  |  invalid_param  |  The parameter `strategy` is empty or not set |  
|  400 | 1121  |  invalid_param  |  The parameter `strategy` must have at least two channels |  
|  400 | 1122  |  invalid_param  |  The parameter `strategy` must have channel `sms` as last element |  
|  400 | 1129  |  invalid_param  |  The parameter `strategy` contains duplicate channels |  
|  400 | 1123  |  invalid_param  |  The parameter `channel` is not valid. Allowed values: |  
|  400 | 1126  |  invalid_param  |  The parameter `templateId` is not set |  
|  400 | 1127  |  invalid_param  |  The parameter `templateId` is not valid |  
|  400 | 1128  |  invalid_param  |  The template ID provided is not a valid template |  
|  403 | 1132  |  access_denied  |  The template ID provided is not approved |  
|  403 | 1133  |  access_denied  |  The template ID provided is not locked |
|  403 | 1131  |  access_denied  |  The strategy contains channels that are not active: |  
|  403 | 1119  |  no_coverage  |  No coverage or restricted destination |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import multichannel_api
from smscx_client.model.send_multichannel_message_request import SendMultichannelMessageRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = multichannel_api.MultichannelApi(
    smscx_client.ApiClient(configuration)
)    
send_multichannel_message_request = SendMultichannelMessageRequest(
        to=[
            "to_example",
        ],
        _from="_from_example",
        strategy=[
            Strategy(
                channel="viber",
                template_id=1,
                text="text_example",
            ),
        ],
        ttl=300,
        country_iso="country_iso_example",
        allow_invalid=False,
        scheduled_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        is_utc=True,
        dlr_callback_url="dlr_callback_url_example",
        track_data="bf325375-e030-fccb-a009-17317c574773",
        short_response=False,
        no_text_details=False,
        show_timezone=False,
        idempotency_id="bf325375-e030-fccb-a009-17317c574773",
    )

try:
    # Send Multichannel message
    api_response = api_instance.send_multichannel_message(send_multichannel_message_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling MultichannelApi->send_multichannel_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_multichannel_message_request** | [**SendMultichannelMessageRequest**](../model/SendMultichannelMessageRequest.md)|  | required

### Return type

[**SendMultichannelMessageResponse**](../model/SendMultichannelMessageResponse.md)

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

