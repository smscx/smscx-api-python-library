# smscx_client.ApplicationsApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_application_settings()**](ApplicationsApi.md#get_application_settings) | **GET** /applications/{applicationId} | Get application settings
[**get_applications_list()**](ApplicationsApi.md#get_applications_list) | **GET** /applications | Get applications list
[**get_scopes()**](ApplicationsApi.md#get_scopes) | **GET** /applications/scopes | Get scopes


# **get_application_settings()**
> ApplicationSettingsResponse get_application_settings(application_id)

Get application settings

Retrieves the settings of an application if a valid identifier was provided.      

The method returns all scopes settings.    

### Errors for GET `/applications/{applicationId}`    
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1500  |  not_found  | Application ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import applications_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = applications_api.ApplicationsApi(
    smscx_client.ApiClient(configuration)
)    

# Identifier of the application id
application_id = "7873310555ea4ee972518ae9559f276707c77fae" 

try:
    # Get application settings
    api_response = api_instance.get_application_settings(application_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ApplicationsApi->get_application_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Identifier of the application id | required

### Return type

[**ApplicationSettingsResponse**](../model/ApplicationSettingsResponse.md)

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

# **get_applications_list()**
> ApplicationsListResponse get_applications_list()

Get applications list

Retrieves the list of existing applications. The applications are returned sorted by creation date, with the most recent applications appearing first.    

If no applications are available, an empty data object is returned.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import applications_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = applications_api.ApplicationsApi(
    smscx_client.ApiClient(configuration)
)    

try:
    # Get applications list
    api_response = api_instance.get_applications_list()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ApplicationsApi->get_applications_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ApplicationsListResponse**](../model/ApplicationsListResponse.md)

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

# **get_scopes()**
> [str] get_scopes()

Get scopes

Retrieves the list of available scopes for the API.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import applications_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = applications_api.ApplicationsApi(
    smscx_client.ApiClient(configuration)
)    

try:
    # Get scopes
    api_response = api_instance.get_scopes()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ApplicationsApi->get_scopes: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[str]**

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

