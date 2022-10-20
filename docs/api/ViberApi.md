# smscx_client.ViberApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_scheduled_viber_campaign()**](ViberApi.md#delete_scheduled_viber_campaign) | **DELETE** /viber/scheduled/campaign/{campaignId} | Delete scheduled Viber campaign
[**delete_scheduled_viber_message()**](ViberApi.md#delete_scheduled_viber_message) | **DELETE** /viber/scheduled/{msgId} | Delete scheduled Viber message
[**estimate_viber_campaign()**](ViberApi.md#estimate_viber_campaign) | **POST** /viber/campaign/estimate | Estimate Viber campaign
[**estimate_viber_message()**](ViberApi.md#estimate_viber_message) | **POST** /viber/estimate | Estimate Viber message
[**send_viber_campaign()**](ViberApi.md#send_viber_campaign) 💰 | **POST** /viber/campaign | Send Viber campaign
[**send_viber_message()**](ViberApi.md#send_viber_message) 💰 | **POST** /viber | Send Viber message


# **delete_scheduled_viber_campaign()**
> DeleteScheduledCampaign delete_scheduled_viber_campaign(campaign_id)

Delete scheduled Viber campaign

Delete a scheduled Viber campaign by providing a valid identifier (`campaignId`).    

The cost of the deleted scheduled Viber campaign will be returned to the balance of the account.    

If part of the Viber campaign has already started, only scheduled messages will be deleted. Messages already sent cannot be deleted. 

### Errors for DELETE `/viber/scheduled/campaign/{campaignId}`  

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
from smscx_client.api import viber_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = viber_api.ViberApi(
    smscx_client.ApiClient(configuration)
)    

# Identifier of a scheduled Viber campaign
campaign_id = "cbb72a72-0dfa-4288-b3d0-05fab904f0b2" 

try:
    # Delete scheduled Viber campaign
    api_response = api_instance.delete_scheduled_viber_campaign(campaign_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ViberApi->delete_scheduled_viber_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Identifier of a scheduled Viber campaign | required

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

# **delete_scheduled_viber_message()**
> DeleteScheduledMsg delete_scheduled_viber_message(msg_id)

Delete scheduled Viber message

Delete a scheduled Viber message by providing a valid identifier (`msgId`).    

The cost of the deleted scheduled Viber message will be returned to the balance of the account.   

### Errors for DELETE `/viber/scheduled/{msgId}`  

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
from smscx_client.api import viber_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = viber_api.ViberApi(
    smscx_client.ApiClient(configuration)
)    

# Identifier of a scheduled Viber message
msg_id = "3328fe13-2b99-4282-b62e-d891f5e452a8" 

try:
    # Delete scheduled Viber message
    api_response = api_instance.delete_scheduled_viber_message(msg_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ViberApi->delete_scheduled_viber_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msg_id** | **str**| Identifier of a scheduled Viber message | required

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

# **estimate_viber_campaign()**
> SendViberCampaignResponse estimate_viber_campaign(send_viber_campaign_request_estimate)

Estimate Viber campaign

Estimate the cost of sending a Viber message to groups of phone numbers.    

This endpoint is identical to `/viber/campaign` endpoint, but it will only simulate the Viber sending (no billing).    

The request body and the response are the same as for `/viber/campaign` endpoint.   

### Errors for POST `/viber/campaigns/estimate`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1101  |  invalid_param  |  The parameter `groups` is empty or not set |  
|  400 | 1140  |  invalid_param  |  Group ID is not a valid group |  
|  400 | 1102  |  invalid_param  |  Group is empty |  
|  400 | 1103  |  invalid_param  |  The phone numbers array is too big (max. allowed: 25000 numbers) |  
|  400 | 1105  |  invalid_param  |  The parameter `from` is empty or not set |  
|  400 | 1108  |  invalid_param  |  The parameter `scheduledDate` is not a valid date |  
|  400 | 1109  |  invalid_param  |  The parameter `dlrCallbackUrl` is not a valid URL |  
|  400 | 1112  |  invalid_param  |  The shortlink/attachment ID provided for tracking is invalid or not found |  
|  400 | 1116  |  invalid_param  |  The scheduled date is in the past |  
|  400 | 1207  |  invalid_param  | The phone number provided is not valid |  
|  400 | 1210  |  invalid_param  |  The phone numbers provided are invalid |  
|  403 | 1119  |  no_coverage  |  No coverage or restricted destination |  
|  400 | 1113  |  insufficient_credit  |  Insufficient credit |  
|  400 | 1114  |  insufficient_credit  |  Credit limit reached. To increase the credit limit, please contact your account manager |  
|  400 | 1126  |  invalid_param  |  The parameter `templateId` is not set |  
|  400 | 1127  |  invalid_param  |  The parameter `templateId` is not valid |  
|  400 | 1128  |  invalid_param  |  The template ID provided is not a valid template |  
|  403 | 1132  |  access_denied  |  The template ID provided is not approved |  
|  403 | 1133  |  access_denied  |  The template ID provided is not locked |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import viber_api
from smscx_client.model.send_viber_campaign_request_estimate import SendViberCampaignRequestEstimate
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = viber_api.ViberApi(
    smscx_client.ApiClient(configuration)
)    
send_viber_campaign_request_estimate = SendViberCampaignRequestEstimate(
        groups=[
            1321,
        ],
        _from="InfoText",
        template_id=187,
        #scheduled_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        #is_utc=True,
        dlr_callback_url="https://webhook/receive-delivery-reports",
        #short_response=False,
        #no_text_details=False,
        #show_timezone=False,
    ) 

try:
    # Estimate Viber campaign
    api_response = api_instance.estimate_viber_campaign(send_viber_campaign_request_estimate)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ViberApi->estimate_viber_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_viber_campaign_request_estimate** | [**SendViberCampaignRequestEstimate**](../model/SendViberCampaignRequestEstimate.md)|  | required

### Return type

[**SendViberCampaignResponse**](../model/SendViberCampaignResponse.md)

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

# **estimate_viber_message()**
> SendViberMessageResponse estimate_viber_message(send_viber_message_request_estimate)

Estimate Viber message

Estimate the cost of sending a Viber message.    

This endpoint is identical to `/viber` endpoint, but it will only simulate the Viber sending (no billing).    

The request body and the response are the same as for `/viber` endpoint.    

### Errors for POST `/viber/estimate`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1104  |  invalid_param  | The parameter `to` is empty or not set |  
|  400 | 1105  |  invalid_param  |  The parameter `from` is empty or not set |  
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
|  400 | 1126  |  invalid_param  |  The parameter `templateId` is not set |  
|  400 | 1127  |  invalid_param  |  The parameter `templateId` is not valid |  
|  400 | 1128  |  invalid_param  |  The template ID provided is not a valid template |  
|  403 | 1132  |  access_denied  |  The template ID provided is not approved |  
|  403 | 1133  |  access_denied  |  The template ID provided is not locked |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import viber_api
from smscx_client.model.send_viber_message_request_estimate import SendViberMessageRequestEstimate
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = viber_api.ViberApi(
    smscx_client.ApiClient(configuration)
)    
send_viber_message_request_estimate = SendViberMessageRequestEstimate(
        to=[
            "+359485721xx",
        ],
        _from="InfoText",
        template_id=261,
        #scheduled_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        #is_utc=True,
        dlr_callback_url="https://webhook/receive-delivery-reports",
        track_data="bf325375-e030-fccb-a009-17317c574773",
        #short_response=False,
        #no_text_details=False,
        #show_timezone=False,
    )     

try:
    # Estimate Viber message
    api_response = api_instance.estimate_viber_message(send_viber_message_request_estimate)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ViberApi->estimate_viber_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_viber_message_request_estimate** | [**SendViberMessageRequestEstimate**](../model/SendViberMessageRequestEstimate.md)|  | required

### Return type

[**SendViberMessageResponse**](../model/SendViberMessageResponse.md)

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

# **send_viber_campaign()**<span>💰</span>
> SendViberCampaignResponse send_viber_campaign(send_viber_campaign_request)

Send Viber campaign

Sends Viber message to existing group(s) of contacts.    

> Note: This endpoint accepts idempotent requests by providing an additional `idempotencyId` parameter in body with a unique value generated by the client of type UUID v1-v5. To confirm that the server understood the request, the response will contain the header `X-Idempotency-Id` with your unique value.  By using idempotency you can retry requests in case of network error or server not responding in time, without accidentally performing the same operation twice and have a guarantee of not being billed twice.     > We recommend to always use Idempotency ID when sending Viber campaigns      

### Errors for POST `/viber/campaigns`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1101  |  invalid_param  |  The parameter `groups` is empty or not set |  
|  400 | 1140  |  invalid_param  |  Group ID is not a valid group |  
|  400 | 1102  |  invalid_param  |  Group is empty |  
|  400 | 1103  |  invalid_param  |  The phone numbers array is too big (max. allowed: 25000 numbers) |  
|  400 | 1105  |  invalid_param  |  The parameter `from` is empty or not set |  
|  400 | 1108  |  invalid_param  |  The parameter `scheduledDate` is not a valid date |  
|  400 | 1109  |  invalid_param  |  The parameter `dlrCallbackUrl` is not a valid URL |  
|  400 | 1111  |  invalid_param  |  Idempotency Id provided is not a valid UUID (v1-v5) |  
|  400 | 1112  |  invalid_param  |  The shortlink/attachment ID provided for tracking is invalid or not found |  
|  400 | 1116  |  invalid_param  |  The scheduled date is in the past |  
|  400 | 1207  |  invalid_param  | The phone number provided is not valid |  
|  400 | 1210  |  invalid_param  |  The phone numbers provided are invalid |  
|  403 | 1119  |  no_coverage  |  No coverage or restricted destination |  
|  400 | 1113  |  insufficient_credit  |  Insufficient credit |  
|  400 | 1114  |  insufficient_credit  |  Credit limit reached. To increase the credit limit, please contact your account manager |  
|  400 | 1126  |  invalid_param  |  The parameter `templateId` is not set |  
|  400 | 1127  |  invalid_param  |  The parameter `templateId` is not valid |  
|  400 | 1128  |  invalid_param  |  The template ID provided is not a valid template |  
|  403 | 1132  |  access_denied  |  The template ID provided is not approved |  
|  403 | 1133  |  access_denied  |  The template ID provided is not locked |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import viber_api
from smscx_client.model.send_viber_campaign_request import SendViberCampaignRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = viber_api.ViberApi(
    smscx_client.ApiClient(configuration)
)    
send_viber_campaign_request = SendViberCampaignRequest(
        groups=[
            631, 
            781,
        ],
        _from="InfoText",
        template_id=187,
        #scheduled_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        #is_utc=True,
        dlr_callback_url="https://webhook/receive-delivery-reports",
        #short_response=False,
        #no_text_details=False,
        #show_timezone=False,
        idempotency_id="bf325375-e030-fccb-a009-17317c574773",
    ) # SendViberCampaignRequest | 

try:
    # Send Viber campaign
    api_response = api_instance.send_viber_campaign(send_viber_campaign_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ViberApi->send_viber_campaign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_viber_campaign_request** | [**SendViberCampaignRequest**](../model/SendViberCampaignRequest.md)|  | required

### Return type

[**SendViberCampaignResponse**](../model/SendViberCampaignResponse.md)

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

# **send_viber_message()**<span>💰</span>
> SendViberMessageResponse send_viber_message(send_viber_message_request)

Send Viber message

Sends Viber message to a single phone number or to a list of phone numbers.    

This endpoint was designed to handle big data objects (up to 25.000 Viber messages in one request).    

If you have loops or iterations we recommend building the send object in your application, and make a single request to this endpoint. The time of making the requests will decrease - by doing a single request with multiple send objects vs making requests in a loop -  and you won't have to worry about making concurrent API calls.    

> Note: This endpoint accepts idempotent requests by providing an additional `idempotencyId` parameter in body with a unique value generated by the client of type UUID v1-v5. To confirm that the server understood the request, the response will contain the header `X-Idempotency-Id` with your unique value.  By using idempotency you can retry requests in case of network error or server not responding in time, without accidentally performing the same operation twice and have a guarantee of not being billed twice.       


### Errors for POST `/viber`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1104  |  invalid_param  | The parameter `to` is empty or not set |  
|  400 | 1105  |  invalid_param  |  The parameter `from` is empty or not set |  
|  400 | 1108  |  invalid_param  |  The parameter `scheduledDate` is not a valid date |  
|  400 | 1109  |  invalid_param  |  The parameter `dlrCallbackUrl` is not a valid URL |  
|  400 | 1111  |  invalid_param  |  Idempotency Id provided is not a valid UUID (v1-v5) |  
|  400 | 1112  |  invalid_param  |  The shortlink/attachment ID provided for tracking is invalid or not found |  
|  400 | 1116  |  invalid_param  |  The scheduled date is in the past |  
|  400 | 1103  |  invalid_param  |  The phone numbers array is too big (max. allowed: 25000 numbers) |  
|  400 | 1207  |  invalid_param  | The phone number provided is not valid |  
|  400 | 1210  |  invalid_param  |  The phone numbers provided are invalid |  
|  403 | 1119  |  no_coverage  |  No coverage or restricted destination |  
|  400 | 1113  |  insufficient_credit  |  Insufficient credit |  
|  400 | 1114  |  insufficient_credit  |  Credit limit reached. To increase the credit limit, please contact your account manager |  
|  400 | 1126  |  invalid_param  |  The parameter `templateId` is not set |  
|  400 | 1127  |  invalid_param  |  The parameter `templateId` is not valid |  
|  400 | 1128  |  invalid_param  |  The template ID provided is not a valid template |  
|  403 | 1132  |  access_denied  |  The template ID provided is not approved |  
|  403 | 1133  |  access_denied  |  The template ID provided is not locked |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import viber_api
from smscx_client.model.send_viber_message_request import SendViberMessageRequest
from smscx_client.model.model403_no_coverage import Model403NoCoverage
from smscx_client.model.model400_invalid_param import Model400InvalidParam
from smscx_client.model.model500_server_error import Model500ServerError
from smscx_client.model.model401_unauthorized import Model401Unauthorized
from smscx_client.model.send_viber_message_response import SendViberMessageResponse
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = viber_api.ViberApi(
    smscx_client.ApiClient(configuration)
)    
send_viber_message_request = SendViberMessageRequest(
        to=[
            "+4474006003xx",
            "+417813350xx",
            "+3584129058xx",
            "+3931238638xx",
            "+316122393xx",
            "+3519121547xx",
            "+336125151xx",
            "+791236471xx",
            "+3069121512xx",
        ],
        _from="InfoText",
        template_id=2561,
        #scheduled_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        #is_utc=True,
        dlr_callback_url="https://webhook/receive-delivery-reports",
        track_data="bf325375-e030-fccb-a009-17317c574773",
        #short_response=False,
        #no_text_details=False,
        #show_timezone=False,
        idempotency_id="bf325375-e030-fccb-a009-17317c574773",
    )

try:
    # Send Viber message
    api_response = api_instance.send_viber_message(send_viber_message_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ViberApi->send_viber_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_viber_message_request** | [**SendViberMessageRequest**](../model/SendViberMessageRequest.md)|  | required

### Return type

[**SendViberMessageResponse**](../model/SendViberMessageResponse.md)

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

