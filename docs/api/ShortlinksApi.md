# smscx_client.ShortlinksApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shortlink()**](ShortlinksApi.md#create_shortlink) | **POST** /shortlinks | Create shortlink
[**delete_shortlink()**](ShortlinksApi.md#delete_shortlink) | **DELETE** /shortlinks/{shortId} | Delete shortlink
[**export_shortlink_hits_to_csv()**](ShortlinksApi.md#export_shortlink_hits_to_csv) | **GET** /shortlinks/{shortId}/csv | Export shortlink hits to CSV
[**export_shortlink_hits_to_xlsx()**](ShortlinksApi.md#export_shortlink_hits_to_xlsx) | **GET** /shortlinks/{shortId}/xlsx | Export shortlink hits to XLSX
[**get_shortlink_hits()**](ShortlinksApi.md#get_shortlink_hits) | **GET** /shortlinks/{shortId} | Get shortlink hits
[**get_shortlinks_list()**](ShortlinksApi.md#get_shortlinks_list) | **GET** /shortlinks | Get shortlinks list
[**update_shortlink()**](ShortlinksApi.md#update_shortlink) | **PATCH** /shortlinks/{shortId} | Update shortlink


# **create_shortlink()**
> ShortlinkNewResponse create_shortlink(shortlink_new_request)

Create shortlink

Creates a new shortlink.

### Errors for POST `/shortlinks`

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1401  |  invalid_param  |  The URL is empty or parameter `url` not set |  
|  400 | 1402  |  invalid_param  |  The URL provided is invalid |  
|  400 | 1404  |  invalid_param  |  The parameter `name` is invalid (min 3, max 25 characters) |  
|  400 | 1405  |  duplicate_id  |  Short ID already exists |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import shortlinks_api
from smscx_client.model.shortlink_new_request import ShortlinkNewRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = shortlinks_api.ShortlinksApi(
    smscx_client.ApiClient(configuration)
)    
shortlink_new_request = ShortlinkNewRequest(
        name="My new shortlink",
        url="https://this-is-my-long-link/this-is-a-long-path",
    )

try:
    # Create shortlink
    api_response = api_instance.create_shortlink(shortlink_new_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ShortlinksApi->create_shortlink: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shortlink_new_request** | [**ShortlinkNewRequest**](../model/ShortlinkNewRequest.md)|  | required

### Return type

[**ShortlinkNewResponse**](../model/ShortlinkNewResponse.md)

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

# **delete_shortlink()**
> ShortlinkDeleteResponse delete_shortlink(short_id)

Delete shortlink

Deletes a shortlink and all the hits data associated, if a valid identifier was provided.

### Errors for DELETE `/shortlinks/{shortId}`

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1400  |  not_found  |  Shortlink ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import shortlinks_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = shortlinks_api.ShortlinksApi(
    smscx_client.ApiClient(configuration)
)    
short_id = "KgTX" # str | Identifier of the shortlink

try:
    # Delete shortlink
    api_response = api_instance.delete_shortlink(short_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ShortlinksApi->delete_shortlink: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_id** | **str**| Identifier of the shortlink | required

### Return type

[**ShortlinkDeleteResponse**](../model/ShortlinkDeleteResponse.md)

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

# **export_shortlink_hits_to_csv()**
> str export_shortlink_hits_to_csv(short_id)

Export shortlink hits to CSV

Exports the hits details of a shortlink (phone number, device, model, operating system, browser, city, country, etc.) to a CSV file.    

If there are no hits for the shortlink, an empty CSV file is returned (with first line headers).

### Errors for GET `/shortlinks/{shortId}/csv`

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1400  |  not_found  |  Shortlink ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import shortlinks_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = shortlinks_api.ShortlinksApi(
    smscx_client.ApiClient(configuration)
)    
short_id = "KgTX"

try:
    # Export shortlink hits to CSV
    api_response = api_instance.export_shortlink_hits_to_csv(short_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ShortlinksApi->export_shortlink_hits_to_csv: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_id** | **str**| Identifier of the shortlink | required

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

# **export_shortlink_hits_to_xlsx()**
> file_type export_shortlink_hits_to_xlsx(short_id)

Export shortlink hits to XLSX

Exports the hits details of a shortlink (phone number, device, model, operating system, browser, city, country, etc.) to a XLSX file (Excel).    

If there are no hits for the shortlink, an empty XLSX file is returned (with first line headers).    

### Errors for GET `/shortlinks/{shortId}/xlsx`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1400  |  not_found  |  Shortlink ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import shortlinks_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = shortlinks_api.ShortlinksApi(
    smscx_client.ApiClient(configuration)
)    
short_id = "KgTX"

try:
    # Export shortlink hits to XLSX
    api_response = api_instance.export_shortlink_hits_to_xlsx(short_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ShortlinksApi->export_shortlink_hits_to_xlsx: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_id** | **str**| Identifier of the shortlink | required

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

# **get_shortlink_hits()**
> ShortlinkDetailsResponse get_shortlink_hits(short_id)

Get shortlink hits

Retrieves the hits details (phone number, device, model, operating system, browser, city, country, etc.) of a shortlink if a valid identifier was provided.    

### Errors for GET `/shortlinks/{shortId}`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1400  |  not_found  |  Shortlink ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import shortlinks_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = shortlinks_api.ShortlinksApi(
    smscx_client.ApiClient(configuration)
)    
short_id = "KgTX" # str | Identifier of the shortlink
short_response = False # bool | If set to true, it will return the full `info` object and an empty `data` object (optional) if omitted the server will use the default value of False
limit = 100 # int | A limit on the number of objects to be returned (optional) if omitted the server will use the default value of 500
next = "NTM2NTA" # str | The next token used to retrieve additional data (optional)
previous = "NTQxNTA" # str | The previous token used to retrieve additional data (optional)

try:
    # Get shortlink hits
    api_response = api_instance.get_shortlink_hits(short_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ShortlinksApi->get_shortlink_hits: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get shortlink hits
    api_response = api_instance.get_shortlink_hits(short_id, short_response=short_response, limit=limit, next=next, previous=previous)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ShortlinksApi->get_shortlink_hits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_id** | **str**| Identifier of the shortlink |
 **short_response** | **bool**| If set to true, it will return the full &#x60;info&#x60; object and an empty &#x60;data&#x60; object | [optional] if omitted the server will use the default value of False
 **limit** | **int**| A limit on the number of objects to be returned | [optional] if omitted the server will use the default value of 500
 **next** | **str**| The next token used to retrieve additional data | [optional]
 **previous** | **str**| The previous token used to retrieve additional data | [optional]

### Return type

[**ShortlinkDetailsResponse**](../model/ShortlinkDetailsResponse.md)

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

# **get_shortlinks_list()**
> ShortlinksListResponse get_shortlinks_list()

Get shortlinks list

Retrieves the list of existing shortlinks. The shortlinks are returned sorted by creation date, with the most recent shortlink appearing first.    

If no shortlinks are available, an empty data object is returned.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import shortlinks_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = shortlinks_api.ShortlinksApi(
    smscx_client.ApiClient(configuration)
)    

try:
    # Get shortlinks list
    api_response = api_instance.get_shortlinks_list()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ShortlinksApi->get_shortlinks_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ShortlinksListResponse**](../model/ShortlinksListResponse.md)

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

# **update_shortlink()**
> ShortlinkUpdateResponse update_shortlink(short_id, shortlink_update_request)

Update shortlink

Updates the specified shortlink by setting the values of the parameters passed. Any parameters not provided will be left unchanged.    

Returns HTTP `204 No content` if the parameters provided did not update the contact because the data was already the same.  

### Errors for PATCH `/shortlinks/{shortId} `  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1400  |  not_found  |  Shortlink ID not found |  
|  400 | 1401  |  invalid_param  |  The URL is empty or parameter `url` not set |  
|  400 | 1402  |  invalid_param  |  The URL provided is invalid |  
|  400 | 1404  |  invalid_param  |  The parameter `name` is invalid (min 3, max 25 characters) |  
|  400 | 1406  |  invalid_param  |  At least one parameter required (name, url) |  
|  400 | 1407  |  duplicate_value  |  You already have a shortlink with this name |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import shortlinks_api
from smscx_client.model.shortlink_update_request import ShortlinkUpdateRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = shortlinks_api.ShortlinksApi(
    smscx_client.ApiClient(configuration)
)    
short_id = "KgTX" # str | Identifier of the shortlink
shortlink_update_request = ShortlinkUpdateRequest(
        name="name_example",
        url="url_example",
    )

try:
    # Update shortlink
    api_response = api_instance.update_shortlink(short_id, shortlink_update_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ShortlinksApi->update_shortlink: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_id** | **str**| Identifier of the shortlink | required
 **shortlink_update_request** | [**ShortlinkUpdateRequest**](../model/ShortlinkUpdateRequest.md)|  | required

### Return type

[**ShortlinkUpdateResponse**](../model/ShortlinkUpdateResponse.md)

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

