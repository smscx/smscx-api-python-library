# smscx_client.OptoutsApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_contact_to_optouts_list()**](OptoutsApi.md#add_contact_to_optouts_list) | **POST** /optouts | Add contact to optouts list
[**delete_contact_from_optouts_list()**](OptoutsApi.md#delete_contact_from_optouts_list) | **DELETE** /optouts/{optoutId} | Delete contact from optouts list
[**export_optouts_to_csv()**](OptoutsApi.md#export_optouts_to_csv) | **GET** /optouts/csv | Export optouts to CSV
[**export_optouts_to_xlsx()**](OptoutsApi.md#export_optouts_to_xlsx) | **GET** /optouts/xlsx | Export optouts to XLSX
[**get_optouts_list()**](OptoutsApi.md#get_optouts_list) | **GET** /optouts | Get optouts list


# **add_contact_to_optouts_list()**
> OptoutsNewResponse add_contact_to_optouts_list(add_contacts_to_group_request)

Add contact to optouts list

Add contacts to the optout list. 

Even if you mistakenly send SMS to a contact that is in the optouts list, the SMS.CX API will detect the contact and not send any messages to unsubscribed contacts. 

Also, you will not be billed - sending a SMS to an unsubscribed contact will be saved as 0 cost.  


### Errors for POST `/optouts`

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1203  |  invalid_param  |  The parameter `phoneNumbers` is empty or not set |  
|  400 | 1208  |  invalid_param  |  The parameter `phoneNumbers` must be an array of phone numbers  |    
|  400 | 1210  |  invalid_param  |  The phone numbers provided are invalid |  
|  400 | 1441  |  invalid_param  | No valid phone numbers were provided or already in the optout list |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import optouts_api
from smscx_client.model.add_contacts_to_group_request import AddContactsToGroupRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = optouts_api.OptoutsApi(
    smscx_client.ApiClient(configuration)
)    
add_contacts_to_group_request = AddContactsToGroupRequest(
        phone_numbers=[
            "+33612246450",
        ],
        allow_invalid=False,
        country_iso="FR",
    )

try:
    # Add contact to optouts list
    api_response = api_instance.add_contact_to_optouts_list(add_contacts_to_group_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OptoutsApi->add_contact_to_optouts_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_contacts_to_group_request** | [**AddContactsToGroupRequest**](../model/AddContactsToGroupRequest.md)|  | required

### Return type

[**OptoutsNewResponse**](../model/OptoutsNewResponse.md)

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

# **delete_contact_from_optouts_list()**
> OptoutsDeleteResponse delete_contact_from_optouts_list(optout_id)

Delete contact from optouts list

Removes a contact from the optout list if a valid phone number identifier was provided.    

Only contacts that were added with the API can be deleted.      

Contacts that opted out via `link` cannot be deleted.

### Errors for DELETE `/optouts/{optoutId}`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1202  |  not_found  |  Phone number ID not found  
|  403 | 1443  |  access_denied  |  Cannot delete this phone number from the optout list because it was added via optout type `link`. Allowed optout type to delete: `admin` |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import optouts_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = optouts_api.OptoutsApi(
    smscx_client.ApiClient(configuration)
)    
optout_id = 458

try:
    # Delete contact from optouts list
    api_response = api_instance.delete_contact_from_optouts_list(optout_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OptoutsApi->delete_contact_from_optouts_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optout_id** | **int**| Identifier of the phone number in the optout list | required

### Return type

[**OptoutsDeleteResponse**](../model/OptoutsDeleteResponse.md)

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

# **export_optouts_to_csv()**
> str export_optouts_to_csv()

Export optouts to CSV

Exports the contacts from the optout list to a CSV file.    

If the optout list is empty, an empty CSV file is returned (with first line headers).

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import optouts_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = optouts_api.OptoutsApi(
    smscx_client.ApiClient(configuration)
)    

try:
    # Export optouts to CSV
    api_response = api_instance.export_optouts_to_csv()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OptoutsApi->export_optouts_to_csv: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#available-methods) [[Back to Model list]](../../README.md#models) [[Back to README]](../../README.md)

# **export_optouts_to_xlsx()**
> file_type export_optouts_to_xlsx()

Export optouts to XLSX

Exports the contacts from the optout list to a XLSX file (Excel).    

If the optout list is empty, an empty XLSX file is returned (with first line headers).

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import optouts_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = optouts_api.OptoutsApi(
    smscx_client.ApiClient(configuration)
)    

try:
    # Export optouts to XLSX
    api_response = api_instance.export_optouts_to_xlsx()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OptoutsApi->export_optouts_to_xlsx: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#available-methods) [[Back to Model list]](../../README.md#models) [[Back to README]](../../README.md)

# **get_optouts_list()**
> OptoutsListResponse get_optouts_list()

Get optouts list

Retrieves the list of existing contacts that opted out. The optouts are returned sorted by creation date, with the most recent optout contact appearing first.    

If no optouts are available, an empty data object is returned.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import optouts_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = optouts_api.OptoutsApi(
    smscx_client.ApiClient(configuration)
)    
limit = 100 # int | A limit on the number of objects to be returned (optional) if omitted the server will use the default value of 500
next = "NTM2NTA" # str | The next token used to retrieve additional data (optional)
previous = "NTQxNTA" # str | The previous token used to retrieve additional data (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get optouts list
    api_response = api_instance.get_optouts_list(limit=limit, next=next, previous=previous)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OptoutsApi->get_optouts_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| A limit on the number of objects to be returned | [optional] if omitted the server will use the default value of 500
 **next** | **str**| The next token used to retrieve additional data | [optional]
 **previous** | **str**| The previous token used to retrieve additional data | [optional]

### Return type

[**OptoutsListResponse**](../model/OptoutsListResponse.md)

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

