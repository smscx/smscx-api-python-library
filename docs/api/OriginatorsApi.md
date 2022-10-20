# smscx_client.OriginatorsApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_originator()**](OriginatorsApi.md#create_originator) | **POST** /originators | Create new originator
[**delete_originator()**](OriginatorsApi.md#delete_originator) | **DELETE** /originators/{originatorId} | Delete originator
[**get_originators_list()**](OriginatorsApi.md#get_originators_list) | **GET** /originators | Get originators list


# **create_originator()**
> OriginatorNewResponse create_originator(originator_new_request)

Create new originator

Creates and submits an originator for approval.  

### Errors for POST `/originators`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1301  |  invalid_param  |  The originator is empty or parameter `originator` not set |  
|  400 | 1303  |  invalid_param  |  The parameter `originator` can contain only letters and numbers |  
|  400 | 1304  |  invalid_param  |  The alphanumeric originator provided is invalid (min 3, max 11 characters) |  
|  400 | 1305  |  invalid_param  |  The numeric originator provided is invalid (min 3, max 15 characters) |  
|  400 | 1306  |  duplicate_value  |  Originator already exists |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import originators_api
from smscx_client.model.originator_new_request import OriginatorNewRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = originators_api.OriginatorsApi(
    smscx_client.ApiClient(configuration)
)    
originator_new_request = OriginatorNewRequest(
        originator="MyCompany",
    ) 

try:
    # Create new originator
    api_response = api_instance.create_originator(originator_new_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OriginatorsApi->create_originator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **originator_new_request** | [**OriginatorNewRequest**](../model/OriginatorNewRequest.md)|  | required

### Return type

[**OriginatorNewResponse**](../model/OriginatorNewResponse.md)

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

# **delete_originator()**
> OriginatorNewResponse delete_originator(originator_id)

Delete originator

Deletes an originator if a valid identifier was provided.    

### Errors for DELETE `/originators/{originatorId}`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1300  |  not_found  |  Originator ID not found

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import originators_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = originators_api.OriginatorsApi(
    smscx_client.ApiClient(configuration)
)    
originator_id = 1388

try:
    # Delete originator
    api_response = api_instance.delete_originator(originator_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OriginatorsApi->delete_originator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **originator_id** | **int**| Identifier of the originator | required

### Return type

[**OriginatorNewResponse**](../model/OriginatorNewResponse.md)

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

# **get_originators_list()**
> OriginatorsListResponse get_originators_list()

Get originators list

Retrieves the list of existing originators (sender ids). The originators are returned sorted by creation date, with the most recent group appearing first.

If no originators are available, an empty data object is returned

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import originators_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = originators_api.OriginatorsApi(
    smscx_client.ApiClient(configuration)
)    

try:
    # Get originators list
    api_response = api_instance.get_originators_list()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OriginatorsApi->get_originators_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OriginatorsListResponse**](../model/OriginatorsListResponse.md)

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

