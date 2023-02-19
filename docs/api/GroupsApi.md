# smscx_client.GroupsApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_contacts_to_group()**](GroupsApi.md#add_contacts_to_group) | **POST** /groups/{groupId} | Add contacts to group
[**add_contacts_to_group_with_fields()**](GroupsApi.md#add_contacts_to_group_with_fields) | **POST** /groups/{groupId} | Add contacts to group with fields (first name, last name, email etc.)
[**create_group()**](GroupsApi.md#create_group) | **POST** /groups | Create new group
[**delete_contact_from_group()**](GroupsApi.md#delete_contact_from_group) | **DELETE** /groups/{groupId}/{phoneNumberId} | Delete contact from group
[**delete_group()**](GroupsApi.md#delete_group) | **DELETE** /groups/{groupId} | Delete group
[**empty_group()**](GroupsApi.md#empty_group) | **GET** /groups/{groupId}/empty | Empty group
[**export_group_to_csv()**](GroupsApi.md#export_group_to_csv) | **GET** /groups/{groupId}/csv | Export group to CSV
[**export_group_to_xlsx()**](GroupsApi.md#export_group_to_xlsx) | **GET** /groups/{groupId}/xlsx | Export group to XLSX
[**get_group_details()**](GroupsApi.md#get_group_details) | **GET** /groups/{groupId} | Get group details
[**get_groups_list()**](GroupsApi.md#get_groups_list) | **GET** /groups | Get list of groups
[**update_contact_from_group()**](GroupsApi.md#update_contact_from_group) | **PATCH** /groups/{groupId}/{phoneNumberId} | Update contact from group


# **add_contacts_to_group()**
> AddContactsToGroupResponse add_contacts_to_group(group_id, add_contacts_to_group_request)

Add contacts to group

Add contacts to a group if a valid identifier was provided.    
### Errors for POST `/groups/{groupId}`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1203  |  invalid_param  | The parameter `phoneNumbers` is empty or not set |  
|  400 | 1208  |  invalid_param  |  The parameter `phoneNumbers` must be an array of phone numbers  |    
|  400 | 1207  |  invalid_param  | The phone number provided is not valid |  
|  400 | 1210  |  invalid_param  | The phone numbers provided are invalid |  
|  404 | 1200  |  not_found  | Group ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import groups_api
from smscx_client.model.add_contacts_to_group_request import AddContactsToGroupRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = groups_api.GroupsApi(
    smscx_client.ApiClient(configuration)
)    
group_id = 1899
add_contacts_to_group_request = AddContactsToGroupRequest(
    phone_numbers=['+3931238788xx','+3584121989xx', '+33612467216', '123456'],
    allow_invalid=True
) 

try:
    # Add contacts to group
    api_response = api_instance.add_contacts_to_group(group_id, add_contacts_to_group_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling GroupsApi->add_contacts_to_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Identifier of a group of contacts | required
 **add_contacts_to_group_request** | [**AddContactsToGroupRequest**](../model/AddContactsToGroupRequest.md)|  | required

### Return type

[**AddContactsToGroupResponse**](../model/AddContactsToGroupResponse.md)

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


# **add_contacts_to_group_with_fields()**
> AddContactsToGroupResponse add_contacts_to_group_with_fields(group_id, add_contacts_to_group_request)

Add contacts to group

Add contacts to a group if a valid identifier was provided.    
### Errors for POST `/groups/{groupId}`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1203  |  invalid_param  | The parameter `phoneNumbers` is empty or not set |  
|  400 | 1208  |  invalid_param  |  The parameter `phoneNumbers` must be an array of phone numbers  |    
|  400 | 1207  |  invalid_param  | The phone number provided is not valid |  
|  400 | 1210  |  invalid_param  | The phone numbers provided are invalid |  
|  404 | 1200  |  not_found  | Group ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import groups_api
from smscx_client.model.add_contacts_to_group_with_fields_request import AddContactsToGroupWithFieldsRequest
from smscx_client.model.group_add import GroupAdd
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = groups_api.GroupsApi(
    smscx_client.ApiClient(configuration)
)    
group_id = 1
add_contacts_to_group_request = AddContactsToGroupWithFieldsRequest(
    phone_numbers=[GroupAdd(
            phone_number="+336125151xx",
            first_name="John",
            last_name="Doe",
            email="john@doe.com",
            field1="field1_example",
            field2="field2_example",
            field3="field3_example",
            field4="field4_example",
            field5="field5_example",
        ),GroupAdd(
            phone_number="+336128298xx",
            first_name="Alain",
            last_name="Maurice",
            email="alain@maurice.com",
            field1="field1_example",
            field2="field2_example",
            field3="field3_example",
            field4="field4_example",
            field5="field5_example",
        ),
    ],
    allow_invalid=True
) 

try:
    # Add contacts to group
    api_response = api_instance.add_contacts_to_group_with_fields(group_id, add_contacts_to_group_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling GroupsApi->add_contacts_to_group_with_fields: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Identifier of a group of contacts | required
 **add_contacts_to_group_request** | [**AddContactsToGroupWithFieldsRequest**](../model/AddContactsToGroupWithFieldsRequest.md)|  | required

### Return type

[**AddContactsToGroupResponse**](../model/AddContactsToGroupResponse.md)

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

# **create_group()**
> NewGroupResponse create_group(new_group_request)

Create new group
  
### Errors for POST `/groups`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1204  |  invalid_param  | The name is empty or parameter `name` not set |  
|  400 | 1206  |  invalid_param  | The name provided is invalid (min 3, max 60 characters) |  
|  400 | 1211  |  duplicate_value  | You already have a group with this name |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import groups_api
from smscx_client.model.new_group_request import NewGroupRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = groups_api.GroupsApi(
    smscx_client.ApiClient(configuration)
)    
new_group_request = NewGroupRequest(
        name="My new group",
    )

try:
    # Create new group
    api_response = api_instance.create_group(new_group_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling GroupsApi->create_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_group_request** | [**NewGroupRequest**](../model/NewGroupRequest.md)|  | required

### Return type

[**NewGroupResponse**](../model/NewGroupResponse.md)

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

# **delete_contact_from_group()**
> DeleteContact delete_contact_from_group(group_id, phone_number_id)

Delete contact from group

Deletes a contact from a group if a valid group identifier was provided.    

### Errors for DELETE `/groups/{groupId}/{phoneNumberId}`

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1200  |  not_found  | Group ID not found |  
|  404 | 1202  |  not_found  | Phone number ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import groups_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = groups_api.GroupsApi(
    smscx_client.ApiClient(configuration)
)    
group_id = 2245 # int | Identifier of a group of contacts
phone_number_id = "68aa4d9f-ee25-4a32-95d0-7272efe3b238" # str | Identifier of the phone number

try:
    # Delete contact from group
    api_response = api_instance.delete_contact_from_group(group_id, phone_number_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling GroupsApi->delete_contact_from_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Identifier of a group of contacts | required
 **phone_number_id** | **str**| Identifier of the phone number | required

### Return type

[**DeleteContact**](../model/DeleteContact.md)

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

# **delete_group()**
> DeleteGroup delete_group(group_id)

Delete group

Deletes a group and all the contacts in the group

### Errors for DELETE `/groups/{groupId}`

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1200  |  not_found  | Group ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import groups_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = groups_api.GroupsApi(
    smscx_client.ApiClient(configuration)
)    
group_id = 2245

try:
    # Delete group
    api_response = api_instance.delete_group(group_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling GroupsApi->delete_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Identifier of a group of contacts | required

### Return type

[**DeleteGroup**](../model/DeleteGroup.md)

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

# **empty_group()**
> GroupResponse empty_group(group_id)

Empty group

Deletes all the contacts in a group.        

Returns HTTP `204 No content` if group is already empty.    

### Errors for GET `/groups/{groupId}/empty`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1200  |  not_found  | Group ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import groups_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = groups_api.GroupsApi(
    smscx_client.ApiClient(configuration)
)    
group_id = 2245 # int | Identifier of a group of contacts

try:
    # Empty group
    api_response = api_instance.empty_group(group_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling GroupsApi->empty_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Identifier of a group of contacts | required

### Return type

[**GroupResponse**](../model/GroupResponse.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth), [BearerAuth](../../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No Content (group already empty) |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#available-methods) [[Back to Model list]](../../README.md#models) [[Back to README]](../../README.md)

# **export_group_to_csv()**
> str export_group_to_csv(group_id)

Export group to CSV

Exports the contacts from a group to a CSV file.    

If the group is empty, an empty CSV file is returned (with first line headers).    

### Errors for GET `/groups/{groupId}/csv`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1200  |  not_found  | Group ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import groups_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = groups_api.GroupsApi(
    smscx_client.ApiClient(configuration)
)    
group_id = 2245

try:
    # Export group to CSV
    api_response = api_instance.export_group_to_csv(group_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling GroupsApi->export_group_to_csv: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Identifier of a group of contacts | required

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

# **export_group_to_xlsx()**
> file_type export_group_to_xlsx(group_id)

Export group to XLSX

Exports the contacts from a group to a XLSX file (Excel).    

If the group is empty, an empty XLSX file is returned (with first line headers).    

### Errors for GET `/groups/{groupId}/xlsx`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1200  |  not_found  | Group ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import groups_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = groups_api.GroupsApi(
    smscx_client.ApiClient(configuration)
)    
group_id = 2245

try:
    # Export group to XLSX
    api_response = api_instance.export_group_to_xlsx(group_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling GroupsApi->export_group_to_xlsx: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Identifier of a group of contacts | required

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

# **get_group_details()**
> GroupDetailsResponse get_group_details(group_id)

Get group details

Retrieves the details of a group if a valid identifier was provided.

### Errors for GET `/groups/{groupId}`

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  404 | 1200  |  not_found  | Group ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import groups_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = groups_api.GroupsApi(
    smscx_client.ApiClient(configuration)
)    
group_id = 2245 # int | Identifier of a group of contacts
short_response = False # bool | If set to true, it will return the full `info` object and an empty `data` object (optional) if omitted the server will use the default value of False
limit = 100 # int | A limit on the number of objects to be returned (optional) if omitted the server will use the default value of 500
next = "NTM2NTA" # str | The next token used to retrieve additional data (optional)
previous = "NTQxNTA" # str | The previous token used to retrieve additional data (optional)

try:
    # Get group details
    api_response = api_instance.get_group_details(group_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling GroupsApi->get_group_details: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get group details
    api_response = api_instance.get_group_details(group_id, short_response=short_response, limit=limit, next=next, previous=previous)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling GroupsApi->get_group_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Identifier of a group of contacts | required
 **short_response** | **bool**| If set to true, it will return the full &#x60;info&#x60; object and an empty &#x60;data&#x60; object | [optional] if omitted the server will use the default value of False
 **limit** | **int**| A limit on the number of objects to be returned | [optional] if omitted the server will use the default value of 500
 **next** | **str**| The next token used to retrieve additional data | [optional]
 **previous** | **str**| The previous token used to retrieve additional data | [optional]

### Return type

[**GroupDetailsResponse**](../model/GroupDetailsResponse.md)

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

# **get_groups_list()**
> GroupsList get_groups_list()

Get list of groups

Retrieves the list of existing groups of contacts. The groups are returned sorted by creation date, with the most recent group appearing first.    

If no groups are available, an empty data object is returned.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import groups_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = groups_api.GroupsApi(
    smscx_client.ApiClient(configuration)
)    

try:
    # Get list of groups
    api_response = api_instance.get_groups_list()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling GroupsApi->get_groups_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GroupsList**](../model/GroupsList.md)

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

# **update_contact_from_group()**
> UpdateNumberResponse update_contact_from_group(group_id, phone_number_id, update_number_request)

Update contact from group

Updates the specified contact by setting the values of the parameters passed. Any parameters not provided will be left unchanged.    

Returns HTTP `204 No content` if the parameters provided did not update the contact because the data was already the same. 

### Errors for PATCH `/groups/{groupId}/{phoneNumberId}`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1213  |  invalid_param  | At least one parameter required (phoneNumber, firstName, lastName, email, field1, field2, field3, field4, field5, customFields) |  
|  400 | 1215  |  duplicate_value  | The phone number already exists |
|  404 | 1202  |  not_found  | Phone number ID not found |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import groups_api
from smscx_client.model.update_number_request import UpdateNumberRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = groups_api.GroupsApi(
    smscx_client.ApiClient(configuration)
)    
group_id = 2245 # int | Identifier of a group of contacts
phone_number_id = "68aa4d9f-ee25-4a32-95d0-7272efe3b238" # str | Identifier of the phone number
update_number_request = UpdateNumberRequest(
        phone_number="+447400389364",
        first_name="John",
        last_name="Doe",
        email="john@doe.com",
        field1="field1_example",
        field2="field2_example",
        field3="field3_example",
        field4="field4_example",
        field5="field5_example",
        ),
    ) # UpdateNumberRequest | 

try:
    # Update contact from group
    api_response = api_instance.update_contact_from_group(group_id, phone_number_id, update_number_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling GroupsApi->update_contact_from_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Identifier of a group of contacts | required
 **phone_number_id** | **str**| Identifier of the phone number | required
 **update_number_request** | [**UpdateNumberRequest**](../model/UpdateNumberRequest.md)|  | required

### Return type

[**UpdateNumberResponse**](../model/UpdateNumberResponse.md)

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

