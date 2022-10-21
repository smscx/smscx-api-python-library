# smscx_client.WhatsappApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_scheduled_whatsapp_message()**](WhatsappApi.md#delete_scheduled_whatsapp_message) | **DELETE** /whatsapp/scheduled/{msgId} | Delete scheduled Whatsapp message
[**estimate_whatsapp_message()**](WhatsappApi.md#estimate_whatsapp_message) | **POST** /whatsapp/estimate | Estimate Whatsapp message
[**send_whatsapp_message()**](WhatsappApi.md#send_whatsapp_message) 💰 | **POST** /whatsapp | Send Whatsapp message


# **delete_scheduled_whatsapp_message()**
> DeleteScheduledMsg delete_scheduled_whatsapp_message(msg_id)

Delete scheduled Whatsapp message

Delete a scheduled Whatsapp message by providing a valid identifier (`msgId`).    

The cost of the deleted scheduled Whatsapp message will be returned to the balance of the account.    

### Errors for DELETE `/whatsapp/scheduled/{msgId}`  

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
from smscx_client.api import whatsapp_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = whatsapp_api.WhatsappApi(
    smscx_client.ApiClient(configuration)
)    

# Identifier of a scheduled Whatsapp message
msg_id = "3328fe13-2b99-4282-b62e-d891f5e452a8" 

try:
    # Delete scheduled Whatsapp message
    api_response = api_instance.delete_scheduled_whatsapp_message(msg_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling WhatsappApi->delete_scheduled_whatsapp_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msg_id** | **str**| Identifier of a scheduled Whatsapp message |

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

# **estimate_whatsapp_message()**
> SendWhatsappMessageResponse estimate_whatsapp_message(send_whatsapp_message_request_estimate)

Estimate Whatsapp message

Estimate the cost of sending a Whatsapp message.    

This endpoint is identical to `/whatsapp` endpoint, but it will only simulate the Whatsapp sending (no billing).    

The request body and the response are the same as for `/whatsapp` endpoint.    

### Errors for POST `/whatsapp/estimate`  

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
|  400 | 1113  |  insufficient_credit  |  Insufficient credit |  
|  400 | 1114  |  insufficient_credit  |  Credit limit reached. To increase the credit limit, please contact your account manager |  
|  400 | 1126  |  invalid_param  |  The parameter `templateId` is not set |  
|  400 | 1127  |  invalid_param  |  The parameter `templateId` is not valid |  
|  400 | 1128  |  invalid_param  |  The template ID provided is not a valid template |  
|  403 | 1132  |  access_denied  |  The template ID provided is not approved |  
|  403 | 1133  |  access_denied  |  The template ID provided is not locked |
|  403 | 1119  |  no_coverage  |  No coverage or restricted destination |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import whatsapp_api
from smscx_client.model.send_whatsapp_message_request_estimate import SendWhatsappMessageRequestEstimate
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = whatsapp_api.WhatsappApi(
    smscx_client.ApiClient(configuration)
)    
send_whatsapp_message_request_estimate = SendWhatsappMessageRequestEstimate(
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
    # Estimate Whatsapp message
    api_response = api_instance.estimate_whatsapp_message(send_whatsapp_message_request_estimate)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling WhatsappApi->estimate_whatsapp_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_whatsapp_message_request_estimate** | [**SendWhatsappMessageRequestEstimate**](../model/SendWhatsappMessageRequestEstimate.md)|  | required

### Return type

[**SendWhatsappMessageResponse**](../model/SendWhatsappMessageResponse.md)

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

# **send_whatsapp_message()**<span>💰</span>
> SendWhatsappMessageResponse send_whatsapp_message(send_whatsapp_message_request)

Send Whatsapp message

Sends Whatsapp message to a single phone number.    

> Note: This endpoint accepts idempotent requests by providing an additional `idempotencyId` parameter in body with a unique value generated by the client of type UUID v1-v5. To confirm that the server understood the request, the response will contain the header `X-Idempotency-Id` with your unique value.  By using idempotency you can retry requests in case of network error or server not responding in time, without accidentally performing the same operation twice and have a guarantee of not being billed twice.     

### Errors for POST `/whatsapp`  
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
|  400 | 1113  |  insufficient_credit  |  Insufficient credit |  
|  400 | 1114  |  insufficient_credit  |  Credit limit reached. To increase the credit limit, please contact your account manager |  
|  400 | 1126  |  invalid_param  |  The parameter `templateId` is not set |  
|  400 | 1127  |  invalid_param  |  The parameter `templateId` is not valid |  
|  400 | 1128  |  invalid_param  |  The template ID provided is not a valid template |  
|  403 | 1132  |  access_denied  |  The template ID provided is not approved |  
|  403 | 1133  |  access_denied  |  The template ID provided is not locked |
|  403 | 1119  |  no_coverage  |  No coverage or restricted destination |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import whatsapp_api
from smscx_client.model.send_whatsapp_message_request import SendWhatsappMessageRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = whatsapp_api.WhatsappApi(
    smscx_client.ApiClient(configuration)
)    
send_whatsapp_message_request = SendWhatsappMessageRequest(
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
    # Send Whatsapp message
    api_response = api_instance.send_whatsapp_message(send_whatsapp_message_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling WhatsappApi->send_whatsapp_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_whatsapp_message_request** | [**SendWhatsappMessageRequest**](../model/SendWhatsappMessageRequest.md)|  | required

### Return type

[**SendWhatsappMessageResponse**](../model/SendWhatsappMessageResponse.md)

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

