# smscx_client.AttachmentsApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_attachment()**](AttachmentsApi.md#delete_attachment) | **DELETE** /attachments/{attachmentId} | Delete attachment
[**export_attachment_hits_to_csv()**](AttachmentsApi.md#export_attachment_hits_to_csv) | **GET** /attachments/{attachmentId}/csv | Export attachment hits to CSV
[**export_attachment_hits_to_xlsx()**](AttachmentsApi.md#export_attachment_hits_to_xlsx) | **GET** /attachments/{attachmentId}/xlsx | Export attachment hits to XLSX
[**get_attachment_hits()**](AttachmentsApi.md#get_attachment_hits) | **GET** /attachments/{attachmentId} | Get attachment hits
[**get_attachments_list()**](AttachmentsApi.md#get_attachments_list) | **GET** /attachments | Get attachments list


# **delete_attachment()**
> AttachmentDeleteResponse delete_attachment(attachment_id)

Delete attachment

Deletes an attachment and all the hits data associated, if a valid identifier was provided.  

### Errors for DELETE `/attachments/{attachmentId}`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1420  |  not_found  | Attachment ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import attachments_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = attachments_api.AttachmentsApi(
    smscx_client.ApiClient(configuration)
)    

# Identifier of the attachment
attachment_id = "KgTX" 

try:
    # Delete attachment
    api_response = api_instance.delete_attachment(attachment_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling AttachmentsApi->delete_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| Identifier of the attachment | required

### Return type

[**AttachmentDeleteResponse**](../model/AttachmentDeleteResponse.md)

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

# **export_attachment_hits_to_csv()**
> str export_attachment_hits_to_csv(attachment_id)

Export attachment hits to CSV

Exports the hits details of an attachment (phone number, device, model, operating system, browser, city, country, etc.) to a CSV file.    

If there are no hits for the attachment, an empty CSV file is returned (with first line headers).    

### Errors for GET /attachments/{attachmentId}/csv  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1420  |  not_found  | Attachment ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import attachments_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = attachments_api.AttachmentsApi(
    smscx_client.ApiClient(configuration)
)    

# Identifier of the attachment
attachment_id = "KgTX" 

try:
    # Export attachment hits to CSV
    api_response = api_instance.export_attachment_hits_to_csv(attachment_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling AttachmentsApi->export_attachment_hits_to_csv: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| Identifier of the attachment | required

### Return type

**str**

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth), [BearerAuth](../../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv, application/json


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

# **export_attachment_hits_to_xlsx()**
> file_type export_attachment_hits_to_xlsx(attachment_id)

Export attachment hits to XLSX

Exports the hits details of an attachment (phone number, device, model, operating system, browser, city, country, etc.) to a XLSX file (Excel).    

If there are no hits for the attachment, an empty XLSX file is returned (with first line headers).    

### Errors for GET /attachments/{attachmentId}/xlsx  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1420  |  not_found  | Attachment ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import attachments_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = attachments_api.AttachmentsApi(
    smscx_client.ApiClient(configuration)
)    

# Identifier of the attachment
attachment_id = "KgTX" 

try:
    # Export attachment hits to XLSX
    api_response = api_instance.export_attachment_hits_to_xlsx(attachment_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling AttachmentsApi->export_attachment_hits_to_xlsx: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| Identifier of the attachment | required

### Return type

**file_type**

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth), [BearerAuth](../../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/json


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

# **get_attachment_hits()**
> AttachmentDetailsResponse get_attachment_hits(attachment_id)

Get attachment hits

Retrieves the hits details (phone number, device, model, operating system, browser, city, country, etc.) of an attachment if a valid identifier was provided.    
### Errors for GET `/attachments/{attachmentId}`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1420  |  not_found  | Attachment ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import attachments_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = attachments_api.AttachmentsApi(
    smscx_client.ApiClient(configuration)
)    
attachment_id = "KgTX" # str | Identifier of the attachment
short_response = False # bool | If set to true, it will return the full `info` object and an empty `data` object (optional) if omitted the server will use the default value of False
limit = 100 # int | A limit on the number of objects to be returned (optional) if omitted the server will use the default value of 500
next = "NTM2NTA" # str | The next token used to retrieve additional data (optional)
previous = "NTQxNTA" # str | The previous token used to retrieve additional data (optional)

try:
    # Get attachment hits
    api_response = api_instance.get_attachment_hits(attachment_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling AttachmentsApi->get_attachment_hits: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get attachment hits
    api_response = api_instance.get_attachment_hits(attachment_id, short_response=short_response, limit=limit, next=next, previous=previous)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling AttachmentsApi->get_attachment_hits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| Identifier of the attachment | required
 **short_response** | **bool**| If set to true, it will return the full &#x60;info&#x60; object and an empty &#x60;data&#x60; object | [optional] if omitted the server will use the default value of False
 **limit** | **int**| A limit on the number of objects to be returned | [optional] if omitted the server will use the default value of 500
 **next** | **str**| The next token used to retrieve additional data | [optional]
 **previous** | **str**| The previous token used to retrieve additional data | [optional]

### Return type

[**AttachmentDetailsResponse**](../model/AttachmentDetailsResponse.md)

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

# **get_attachments_list()**
> AttachmentListResponse get_attachments_list()

Get attachments list

Retrieves the list of existing attachments. The attachments are returned sorted by creation date, with the most recent attachment appearing first.    

If no attachments are available, an empty data object is returned.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import attachments_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = attachments_api.AttachmentsApi(
    smscx_client.ApiClient(configuration)
)    

try:
    # Get attachments list
    api_response = api_instance.get_attachments_list()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling AttachmentsApi->get_attachments_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AttachmentListResponse**](../model/AttachmentListResponse.md)

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

