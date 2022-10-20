# smscx_client.TemplatesApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_template()**](TemplatesApi.md#create_template) | **POST** /templates | Create template
[**delete_template()**](TemplatesApi.md#delete_template) | **DELETE** /templates/{templateId} | Delete template
[**get_template()**](TemplatesApi.md#get_template) | **GET** /templates/{templateId} | Get template
[**get_templates_list()**](TemplatesApi.md#get_templates_list) | **GET** /templates | Get templates list
[**update_template()**](TemplatesApi.md#update_template) | **PATCH** /templates/{templateId} | Update template


# **create_template()**
> TemplatesNewResponse create_template(templates_new_request)

Create template

Creates a new template.    

### Errors for POST `/templates`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 |  1801  |  invalid_param  |  The text message is empty or parameter `text` not set |  
|  400 |  1802  |  invalid_param  |  The parameter `text` is invalid |  
|  400 | 1803  |  invalid_param  |  The name provided is invalid (min 3, max 100 characters) |  
|  400 | 1806  |  invalid_param  |  The parameter `channel` is not valid. Allowed values: |  
|  400 | 1805  |  duplicate_value  |  You already have a template with this name  |    
|  400 | 1811  |  invalid_param  |  Text message too long (max 1000 characters)  |    
|  400 | 1808  |  invalid_param  |  Button caption is too long (min 1, max. 30 characters)  |    
|  400 | 1809  |  invalid_param  |  Invalid target URL |  
|  400 | 1810  |  invalid_param  |  Invalid image URL  |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import templates_api
from smscx_client.model.templates_new_request import TemplatesNewRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = templates_api.TemplatesApi(
    smscx_client.ApiClient(configuration)
)    
templates_new_request = TemplatesNewRequest(
        name="My text template",
        text="This is my text template {{optoutLink}}",
        channel="sms",
    )

try:
    # Create template
    api_response = api_instance.create_template(templates_new_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling TemplatesApi->create_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templates_new_request** | [**TemplatesNewRequest**](../model/TemplatesNewRequest.md)|  | required

### Return type

[**TemplatesNewResponse**](../model/TemplatesNewResponse.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth), [BearerAuth](../../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * X-Request-Id -  <br>  * X-Response-Time -  <br>  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#available-methods) [[Back to Model list]](../../README.md#models) [[Back to README]](../../README.md)

# **delete_template()**
> TemplatesDeleteResponse delete_template(template_id)

Delete template

Deletes a template if a valid identifier was provided.

### Errors for DELETE `/templates/{templateId}`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1800  |  not_found  |  Template ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import templates_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = templates_api.TemplatesApi(
    smscx_client.ApiClient(configuration)
)    
template_id = 39774 

try:
    # Delete template
    api_response = api_instance.delete_template(template_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling TemplatesApi->delete_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Identifier of the template | required

### Return type

[**TemplatesDeleteResponse**](../model/TemplatesDeleteResponse.md)

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

# **get_template()**
> TemplateDetailsResponse get_template(template_id)

Get template

Retrieves the details of a template if a valid identifier was provided.  

### Errors for GET `/templates/{templateId}`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1800  |  not_found  |  Template ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import templates_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = templates_api.TemplatesApi(
    smscx_client.ApiClient(configuration)
)    
template_id = 39774

try:
    # Get template
    api_response = api_instance.get_template(template_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling TemplatesApi->get_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Identifier of the template | required

### Return type

[**TemplateDetailsResponse**](../model/TemplateDetailsResponse.md)

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

# **get_templates_list()**
> TemplatesListResponse get_templates_list()

Get templates list

Retrieves the list of existing templates. The templates are returned sorted by creation date, with the most recent templates appearing first.    

If no templates are available, an empty data object is returned.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import templates_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = templates_api.TemplatesApi(
    smscx_client.ApiClient(configuration)
)    

try:
    # Get templates list
    api_response = api_instance.get_templates_list()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling TemplatesApi->get_templates_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TemplatesListResponse**](../model/TemplatesListResponse.md)

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

# **update_template()**
> TemplatesUpdateResponse update_template(template_id, templates_update_request)

Update template

Updates the specified template by setting the values of the parameters passed. Any parameters not provided will be left unchanged.    

### Errors for PATCH `/templates/{templateId}`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1800  |  not_found  |  Template ID not found |  
|  400 | 1802  |  invalid_param  |  The parameter `text` is invalid |  
|  400 | 1803  |  invalid_param  |  The name provided is invalid (min 3, max 100 characters) |  
|  400 | 1804  |  invalid_param  |  At least one parameter required (name, text) |  
|  400 | 1811  |  invalid_param  |  Text message too long (max 1000 characters) |  
|  403 | 1812  |  access_denied  |  Template is locked for editing |  
|  400 | 1810  |  invalid_param  |  Invalid image URL |  
|  400 | 1808  |  invalid_param  |  Button caption is too long (min 1, max. 30 characters) |  
|  400 | 1809  |  invalid_param  |  Invalid target URL |  
|  400 | 1805  |  duplicate_value  |  You already have a template with this name |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import templates_api
from smscx_client.model.templates_update_response import TemplatesUpdateResponse
from smscx_client.model.templates_update_request import TemplatesUpdateRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = templates_api.TemplatesApi(
    smscx_client.ApiClient(configuration)
)    
template_id = 39774 # int | Identifier of the template
templates_update_request = TemplatesUpdateRequest(
        name="My edited template name",
        text="My edited template text",
        channel="sms",
    )

try:
    # Update template
    api_response = api_instance.update_template(template_id, templates_update_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling TemplatesApi->update_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**| Identifier of the template | required
 **templates_update_request** | [**TemplatesUpdateRequest**](../model/TemplatesUpdateRequest.md)|  | required

### Return type

[**TemplatesUpdateResponse**](../model/TemplatesUpdateResponse.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth), [BearerAuth](../../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-Id -  <br>  * X-Response-Time -  <br>  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  |
**204** | No content (nothing to update, same data) |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#available-methods) [[Back to Model list]](../../README.md#models) [[Back to README]](../../README.md)

