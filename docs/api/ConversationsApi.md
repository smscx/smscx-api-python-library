# smscx_client.ConversationsApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_conversation()**](ConversationsApi.md#get_conversation) | **GET** /conversations/{conversationId} | Get conversation
[**get_converstions_list()**](ConversationsApi.md#get_converstions_list) | **GET** /conversations | Get conversations list
[**mark_conversation_as_read()**](ConversationsApi.md#mark_conversation_as_read) | **GET** /conversations/{conversationId}/read | Mark conversation as read
[**send_conversation_reply_sms()**](ConversationsApi.md#send_conversation_reply_sms) 💰 | **POST** /conversations/{conversationId}/sms | Send conversation reply via SMS
[**send_conversation_reply_viber()**](ConversationsApi.md#send_conversation_reply_viber) 💰 | **POST** /conversations/{conversationId}/viber | Send conversation reply via Viber
[**send_conversation_reply_whatsapp()**](ConversationsApi.md#send_conversation_reply_whatsapp) 💰 | **POST** /conversations/{conversationId}/whatsapp | Send conversation reply via Whatsapp


# **get_conversation()**
> ConversationDetailsResponse get_conversation(conversation_id)

Get conversation

Retrieves the details of a conversation if a valid identifier was provided.

### Errors for GET `/conversations/{conversationId}`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1180  |  not_found  | Conversation ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import conversations_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = conversations_api.ConversationsApi(
    smscx_client.ApiClient(configuration)
)    
conversation_id = "c38fa60d-ce8f-4918-8b9d-d991bc44cb73" 

try:
    # Get conversation
    api_response = api_instance.get_conversation(conversation_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ConversationsApi->get_conversation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| Identifier of the conversation | required

### Return type

[**ConversationDetailsResponse**](../model/ConversationDetailsResponse.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth), [BearerAuth](../../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-Id -  <br>  * X-Response-Time -  <br>  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#available-methods) [[Back to Model list]](../../README.md#models) [[Back to README]](../../README.md)

# **get_converstions_list()**
> ConversationsListResponse get_converstions_list()

Get conversations list

Retrieves the list of existing conversations. The list is sorted by last reply date, with the most recent reply appearing first.   

If no conversations are available, an empty data object is returned.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import conversations_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = conversations_api.ConversationsApi(
    smscx_client.ApiClient(configuration)
)    

try:
    # Get conversations list
    api_response = api_instance.get_converstions_list()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ConversationsApi->get_converstions_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationsListResponse**](../model/ConversationsListResponse.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth), [BearerAuth](../../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-Id -  <br>  * X-Response-Time -  <br>  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#available-methods) [[Back to Model list]](../../README.md#models) [[Back to README]](../../README.md)

# **mark_conversation_as_read()**
> ConversationReadResponse mark_conversation_as_read(conversation_id)

Mark conversation as read

Marks a conversation as read    
### Errors for GET `/conversations/{conversationId}/read`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1180  |  not_found  | Conversation ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import conversations_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = conversations_api.ConversationsApi(
    smscx_client.ApiClient(configuration)
)    
conversation_id = "c38fa60d-ce8f-4918-8b9d-d991bc44cb73" 

try:
    # Mark conversation as read
    api_response = api_instance.mark_conversation_as_read(conversation_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ConversationsApi->mark_conversation_as_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| Identifier of the conversation | required

### Return type

[**ConversationReadResponse**](../model/ConversationReadResponse.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth), [BearerAuth](../../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-Id -  <br>  * X-Response-Time -  <br>  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#available-methods) [[Back to Model list]](../../README.md#models) [[Back to README]](../../README.md)

# **send_conversation_reply_sms()**<span>💰</span>
> ConversationReplySmsResponse send_conversation_reply_sms(conversation_id, conversation_reply_sms_request)

Send conversation reply via SMS

Sends a reply to a conversation using sms channel.    
### Errors for POST `/conversations/{conversationId}/sms`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1180  |  not_found  | Conversation ID not found |  
|  400 | 1801  |  invalid_param  | The text message is empty or parameter `text` not set |  
|  400 | 1802  |  invalid_param  | The parameter `text` is invalid |  
|  400 | 1111  |  invalid_param  |  Idempotency Id provided is not a valid UUID (v1-v5) |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import conversations_api
from smscx_client.model.conversation_reply_sms_request import ConversationReplySmsRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = conversations_api.ConversationsApi(
    smscx_client.ApiClient(configuration)
)    
conversation_id = "c38fa60d-ce8f-4918-8b9d-d991bc44cb73" 
conversation_reply_sms_request = ConversationReplySmsRequest(
        text="text_example",
    )

try:
    # Send conversation reply via SMS
    api_response = api_instance.send_conversation_reply_sms(conversation_id, conversation_reply_sms_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ConversationsApi->send_conversation_reply_sms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| Identifier of the conversation | required
 **conversation_reply_sms_request** | [**ConversationReplySmsRequest**](../model/ConversationReplySmsRequest.md)|  | required

### Return type

[**ConversationReplySmsResponse**](../model/ConversationReplySmsResponse.md)

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
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#available-methods) [[Back to Model list]](../../README.md#models) [[Back to README]](../../README.md)

# **send_conversation_reply_viber()**<span>💰</span>
> ConversationReplyViberRespone send_conversation_reply_viber(conversation_id, conversation_reply_viber_request)

Send conversation reply via Viber

Sends a reply to a conversation using viber channel.

### Errors for POST `/conversations/{conversationId}/viber`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1180  |  not_found  | Conversation ID not found |  
|  403 | 1181  |  access_denied  | Cannot reply with channel Viber. More than 24 hours since user reply |  
|  400 | 1801  |  invalid_param  | The text message is empty or parameter `text` not set |  
|  400 | 1802  |  invalid_param  | The parameter `text` is invalid |  
|  400 | 1811  |  invalid_param  | Text message too long (max 1000 characters) |  
|  400 | 1111  |  invalid_param  |  Idempotency Id provided is not a valid UUID (v1-v5) |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import conversations_api
from smscx_client.model.conversation_reply_viber_request import ConversationReplyViberRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = conversations_api.ConversationsApi(
    smscx_client.ApiClient(configuration)
)    
conversation_id = "c38fa60d-ce8f-4918-8b9d-d991bc44cb73" 
conversation_reply_viber_request = ConversationReplyViberRequest(
        text="text_example",
        rich_media={},
    )

try:
    # Send conversation reply via Viber
    api_response = api_instance.send_conversation_reply_viber(conversation_id, conversation_reply_viber_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ConversationsApi->send_conversation_reply_viber: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| Identifier of the conversation | required
 **conversation_reply_viber_request** | [**ConversationReplyViberRequest**](../model/ConversationReplyViberRequest.md)|  | required

### Return type

[**ConversationReplyViberRespone**](../model/ConversationReplyViberRespone.md)

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
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#available-methods) [[Back to Model list]](../../README.md#models) [[Back to README]](../../README.md)

# **send_conversation_reply_whatsapp()**<span>💰</span>
> ConversationReplyWhatsappResponse send_conversation_reply_whatsapp(conversation_id, conversation_reply_whatsapp_request)

Send conversation reply via Whatsapp

Sends a reply to a conversation using whatsapp channel.    

### Errors for POST `/conversations/{conversationId}/whatsapp`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1180  |  not_found  | Conversation ID not found |  
|  403 | 1182  |  access_denied  | Cannot reply with channel Whatsapp. More than 24 hours since user reply |  
|  400 | 1801  |  invalid_param  | The text message is empty or parameter `text` not set |  
|  400 | 1802  |  invalid_param  | The parameter `text` is invalid |  
|  400 | 1811  |  invalid_param  | Text message too long (max 1000 characters) |  
|  400 | 1111  |  invalid_param  |  Idempotency Id provided is not a valid UUID (v1-v5) |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import conversations_api
from smscx_client.model.conversation_reply_whatsapp_request import ConversationReplyWhatsappRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = conversations_api.ConversationsApi(
    smscx_client.ApiClient(configuration)
)    
conversation_id = "c38fa60d-ce8f-4918-8b9d-d991bc44cb73" 
conversation_reply_whatsapp_request = ConversationReplyWhatsappRequest(
        text="text_example",
        rich_media={},
    )

try:
    # Send conversation reply via Whatsapp
    api_response = api_instance.send_conversation_reply_whatsapp(conversation_id, conversation_reply_whatsapp_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ConversationsApi->send_conversation_reply_whatsapp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| Identifier of the conversation | required
 **conversation_reply_whatsapp_request** | [**ConversationReplyWhatsappRequest**](../model/ConversationReplyWhatsappRequest.md)|  | required

### Return type

[**ConversationReplyWhatsappResponse**](../model/ConversationReplyWhatsappResponse.md)

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
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#available-methods) [[Back to Model list]](../../README.md#models) [[Back to README]](../../README.md)

