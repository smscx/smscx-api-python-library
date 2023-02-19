# smscx_client.NumbersApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bulk_lookup_status()**](NumbersApi.md#get_bulk_lookup_status) | **GET** /numbers/lookup/lookupBulkId/{lookupBulkId} | Get Bulk Lookup result
[**get_bulk_lookup_campaigns()**](NumbersApi.md#get_bulk_lookup_campaigns) | **GET** /numbers/lookup | Get list of bulk lookup campaigns
[**get_single_lookup_status()**](NumbersApi.md#get_single_lookup_status) | **GET** /numbers/lookup/lookupId/{lookupId} | Get Single Lookup result
[**lookup_number()**](NumbersApi.md#lookup_number) 💰 | **GET** /numbers/lookup/{phoneNumber} | Lookup number
[**lookup_numbers()**](NumbersApi.md#lookup_numbers) 💰 | **POST** /numbers/lookup | Lookup numbers in bulk
[**export_number_lookup_report_to_csv()**](NumbersApi.md#export_number_lookup_report_to_csv) | **GET** /numbers/lookup/lookupBulkId/{lookupBulkId}/csv | Export number lookup campaign to CSV
[**export_number_lookup_report_to_xlsx()**](NumbersApi.md#export_number_lookup_report_to_xlsx) | **GET** /numbers/lookup/lookupBulkId/{lookupBulkId}/xlsx | Export number lookup campaign to XLSX
[**validate_number()**](NumbersApi.md#validate_number) | **GET** /numbers/validate/{phoneNumber} | Validate number
[**validate_numbers()**](NumbersApi.md#validate_numbers) | **POST** /numbers/validate | Validate numbers in bulk
[**get_available_numbers()**](NumbersApi.md#get_available_numbers) | **GET** /numbers/rent/available/{countryIso} | Get available numbers for rent
[**rent_number()**](NumbersApi.md#rent_number) 💰 | **POST** /numbers/rent | Rent phone number
[**cancel_rent()**](NumbersApi.md#cancel_rent) | **DELETE** /numbers/rent/{rentId} | Cancel rent for phone number
[**renew_rent()**](NumbersApi.md#renew_rent) 💰 | **PATCH** /numbers/rent/{rentId} | Renew rent for phone number
[**get_rent_status()**](NumbersApi.md#get_rent_status) | **GET** /numbers/rent/{rentId} | Get status of rent
[**get_rented_numbers()**](NumbersApi.md#get_rented_numbers) | **GET** /numbers/rent | Get list of your rented numbers
[**get_inbound_sms()**](NumbersApi.md#get_inbound_sms) | **GET** /numbers/rent/{rentId}/inbound | Get inbound SMS from rented number
[**edit_rent_settings()**](NumbersApi.md#edit_rent_settings) | **PATCH** /numbers/rent/{rentId}/edit | Edit settings for active rent

# **get_bulk_lookup_status()**
> NumbersBulkLookupResult get_bulk_lookup_status(lookup_bulk_id)

Get Bulk Lookup result

Get details of a bulk phone number lookup.

### Errors for GET `/numbers/lookup/lookupBulkId/{lookupBulkId}`

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
| 400 | 1218 | not_found | The lookupBulkId provided is invalid |  
| 404 | 1220 | invalid_param | Lookup Bulk ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import numbers_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = numbers_api.NumbersApi(
    smscx_client.ApiClient(configuration)
)    
lookup_bulk_id = "68aa4d9f-ee25-4a32-95d0-7272efe3b238" # str | Identifier of the bulk number lookup campaign
limit = 100 # int | A limit on the number of objects to be returned (optional) if omitted the server will use the default value of 500
next = None # str | The next token used to retrieve additional data (optional)
previous = None # str | The previous token used to retrieve additional data (optional)

# example passing only required values which don't have defaults set
try:
    # Get Bulk Lookup result
    api_response = api_instance.get_bulk_lookup_status(lookup_bulk_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->get_bulk_lookup_status: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get Bulk Lookup result
    api_response = api_instance.get_bulk_lookup_status(lookup_bulk_id, limit=limit, next=next, previous=previous)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->get_bulk_lookup_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lookup_bulk_id** | **str**| Identifier of the bulk number lookup campaign | required
 **limit** | **int**| A limit on the number of objects to be returned | [optional] if omitted the server will use the default value of 500
 **next** | **str**| The next token used to retrieve additional data | [optional]
 **previous** | **str**| The previous token used to retrieve additional data | [optional]

### Return type

[**NumbersBulkLookupResult**](../model/NumbersBulkLookupResult.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth), [BearerAuth](../../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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


# **get_bulk_lookup_campaigns()**
> BulkLookupCampaignsResponse get_bulk_lookup_campaigns()

Get list of bulk lookup campaigns

Get list of bulk lookup campaigns

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import numbers_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = numbers_api.NumbersApi(
    smscx_client.ApiClient(configuration)
)    
limit = 100 # int | A limit on the number of objects to be returned (optional) if omitted the server will use the default value of 500
next = None # str | The next token used to retrieve additional data (optional)
previous = None # str | The previous token used to retrieve additional data (optional)

try:
    # Get list of bulk lookup campaigns
    api_response = api_instance.get_bulk_lookup_campaigns(limit=limit, next=next, previous=previous)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->get_bulk_lookup_campaigns: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| A limit on the number of objects to be returned | [optional] if omitted the server will use the default value of 500
 **next** | **str**| The next token used to retrieve additional data | [optional]
 **previous** | **str**| The previous token used to retrieve additional data | [optional]

### Return type

[**BulkLookupCampaignsResponse**](../model/BulkLookupCampaignsResponse.md)

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

# **get_single_lookup_status()**
> DataNumberLookup get_single_lookup_status(lookup_id)

Get Single Lookup result

Get details of a single number lookup.

### Errors for GET `/numbers/lookup/lookupId/{lookupId}`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
| 400 | 1217 | invalid_param | The lookupId provided is invalid |  
| 404 | 1219 | not_found | Lookup  ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import numbers_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = numbers_api.NumbersApi(
    smscx_client.ApiClient(configuration)
)    

# Identifier of the number lookup
lookup_id = "68aa4d9f-ee25-4a32-95d0-7272efe3b238"

try:
    # Get Single Lookup result
    api_response = api_instance.get_single_lookup_status(lookup_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->get_single_lookup_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lookup_id** | **str**| Identifier of the number lookup | required

### Return type

[**DataNumberLookup**](../model/DataNumberLookup.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth), [BearerAuth](../../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **lookup_number()**<span>💰</span>
> NumberLookupResponse lookup_number(phone_number)

Lookup number

Lookup a single phone number, provided in international E.164 format. Returns info about status of the number (ACTIVE, ABSENT), if the phone number is ported, roaming, original and current network operator.    

The endpoint returns error if phone number is invalid.    

### Statuses of phone number lookup  

| Status | Description | 
|:------------:|:------------|  
| ACTIVE | Phone number is reachable |  
| ABSENT | Phone number is not reachable |  
| BARRED | Phone number has a block from their operator |  
| UNKNOWN | Unknown subscriber. Phone number is not reachable |  
| FAILED | Lookup for this phone number failed |    

### Errors for GET `/numbers/lookup/{phoneNumber}`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
| 400 | 1207 | invalid_param | The phone number is invalid |  
| 403 | 1214 | no_coverage | No coverage or restricted destination |  
| 400 | 1113 | insufficient_credit | Insufficient credit |  
| 400 | 1114 | insufficient_credit | Credit limit reached. To increase the credit limit, please contact your account manager |  
| 400 | 1212 | invalid_param | Invalid request parameters |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import numbers_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = numbers_api.NumbersApi(
    smscx_client.ApiClient(configuration)
)    
phone_number = "+33612246450"

try:
    # Lookup number
    api_response = api_instance.lookup_number(phone_number)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->lookup_number: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**| Phone number in international E.164 format (eg. **+33612424105**). The leading plus sign of the international format can be set as is, ommited or url encoded. The API will automatically format and set the plus sign.  
 The following values are considered valid:   
 - +33612424105 
 - 33612424105 
 - %2B33612424105 | required

### Return type

[**NumberLookupResponse**](../model/NumberLookupResponse.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth), [BearerAuth](../../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **lookup_numbers()**<span>💰</span>
> NumbersLookupResponse lookup_numbers(numbers_lookup_request)

Lookup numbers in bulk

Lookup a list of phone numbers. The result of the bulk phone lookup: status of the number (ACTIVE, ABSENT), if the phone numbers are ported, roaming, original and current network operator. 

You can lookup in bulk up to **40.000 phone numbers**.    

The endpoint does not return error if phone numbers are invalid.    

### Statuses of phone number lookup  
| Status | Description |  
|:------------:|:------------|  
| ACTIVE | Phone number is reachable |  
| ABSENT | Phone number is not reachable |  
| BARRED | Phone number has a block from their operator |  
| UNKNOWN | Unknown subscriber. Phone number is not reachable |  
| FAILED | Lookup for this phone number failed |    

### Errors for POST `/numbers/lookup`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
| 400 | 1203 | invalid_param | The parameter 'phoneNumbers' is empty or not set |  
| 400 | 1208 | invalid_param | The parameter 'phoneNumbers' must be an array of phone numbers |  
| 400 | 1205 | invalid_param | The phone numbers array is too big (max. allowed: 40000 numbers) |  
| 400 | 1209 | invalid_param | The parameter 'lookupCallbackUrl' is not a valid URL |  
| 400 | 1216 | invalid_param | No valid numbers provided or no coverage |  
| 400 | 1113 | insufficient_credit | Insufficient credit |  
| 400 | 1114 | insufficient_credit | Credit limit reached. To increase the credit limit, please contact your account manager |
| 403 | 1214 | no_coverage | No coverage or restricted destination |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import numbers_api
from smscx_client.model.numbers_lookup_request import NumbersLookupRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = numbers_api.NumbersApi(
    smscx_client.ApiClient(configuration)
)    
numbers_lookup_request = NumbersLookupRequest(
        phone_numbers=[
            "+33612246450",
            "+33612246421",
            "+33612246xxx",
            "+33612219xxx",
            "+33612265xxx",
            "+337122",
            "+33612886370",
            # National format, if parameter country_iso is used
            "0612886370",
        ],
        # country_iso="FR",
        lookup_callback_url="https://my-webhook/endpoint",
    )

try:
    # Lookup numbers in bulk
    api_response = api_instance.lookup_numbers(numbers_lookup_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->lookup_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numbers_lookup_request** | [**NumbersLookupRequest**](../model/NumbersLookupRequest.md)|  | required

### Return type

[**NumbersLookupResponse**](../model/NumbersLookupResponse.md)

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

# **export_number_lookup_report_to_csv()**
> str export_number_lookup_report_to_csv(lookup_bulk_id)

Export number lookup campaign to CSV

Exports the details of a phone number lookup campaign to a CSV file.    
### Errors for GET `/numbers/lookup/lookupBulkId/{lookupBulkId}/csv`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1218  |  invalid_param  |  The lookupBulkId provided is invalid  |  
|  404 | 1220  |  not_found  |  Lookup Bulk ID not found  |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import numbers_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = numbers_api.NumbersApi(
    smscx_client.ApiClient(configuration)
)    
lookup_bulk_id = "68aa4d9f-ee25-4a32-95d0-7272efe3b238" # str | Identifier of the bulk number lookup campaign

try:
    # Export number lookup campaign to CSV
    api_response = api_instance.export_number_lookup_report_to_csv(lookup_bulk_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->export_number_lookup_report_to_csv: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lookup_bulk_id** | **str**| Identifier of the bulk number lookup campaign | required

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#available-methods) [[Back to Model list]](../../README.md#models) [[Back to README]](../../README.md)

# **export_number_lookup_report_to_xlsx()**

> file_type export_number_lookup_report_to_xlsx(lookup_bulk_id)

Export number lookup campaign to XLSX

Exports the details of a phone number lookup campaign to a XLSX file.    
### Errors for GET `/numbers/lookup/lookupBulkId/{lookupBulkId}/xlsx`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1218  |  invalid_param  |  The lookupBulkId provided is invalid  |  
|  404 | 1220  |  not_found  |  Lookup Bulk ID not found  |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import numbers_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = numbers_api.NumbersApi(
    smscx_client.ApiClient(configuration)
)    
lookup_bulk_id = "68aa4d9f-ee25-4a32-95d0-7272efe3b238" # str | Identifier of the bulk number lookup campaign

try:
    # Export number lookup campaign to XLSX
    api_response = api_instance.export_number_lookup_report_to_xlsx(lookup_bulk_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->export_number_lookup_report_to_xlsx: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lookup_bulk_id** | **str**| Identifier of the bulk number lookup campaign | required

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#available-methods) [[Back to Model list]](../../README.md#models) [[Back to README]](../../README.md)

# **validate_number()**
> NumberValidateResponse validate_number(phone_number)

Validate number

Validates a single phone number, provided in international E.164 format.    

The endpoint returns error if phone number is invalid.

### Errors for GET `/numbers/validate/{phoneNumber}`

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1207  |  invalid_param  |  The phone number is invalid  |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import numbers_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = numbers_api.NumbersApi(
    smscx_client.ApiClient(configuration)
)    
phone_number = "+33612246450" 

try:
    # Validate number
    api_response = api_instance.validate_number(phone_number)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->validate_number: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**| Phone number in international E.164 format (eg. **+33612424105**). The leading plus sign of the international format can be set as is, ommited or url encoded. The API will automatically format and set the plus sign.   
 The following values are considered valid:   
 - +33612424105 
 - 33612424105 
 - %2B33612424105 | required

### Return type

[**NumberValidateResponse**](../model/NumberValidateResponse.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth), [BearerAuth](../../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **validate_numbers()**
> NumbersValidateResponse validate_numbers(numbers_validate_request)

Validate numbers in bulk

Validate a list of phone numbers. You can validate in bulk up to **40.000 phone numbers**.    

This method will validate the list of phone numbers and return an array of objects, **preserving the order of the list provided** and not excluding the invalid phone numbers.     

An invalid phone number will have the parameter `invalid` with value `true` in the response object.      

### Errors for POST `/numbers/validate`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1203  |  invalid_param  |  The parameter `phoneNumbers` is empty or not set |  
|  400 | 1208  |  invalid_param  |  The parameter `phoneNumbers` must be an array of phone numbers |  
| 400 | 1205 | invalid_param | The phone numbers array is too big (max. allowed: 40000 numbers) |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import numbers_api
from smscx_client.model.numbers_validate_request import NumbersValidateRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = numbers_api.NumbersApi(
    smscx_client.ApiClient(configuration)
)    
numbers_validate_request = NumbersValidateRequest(
        phone_numbers=[
            "+33612246450",
            "+33612246421",
            "+33612246xxx",
            "+33612219xxx",
            "+33612265xxx",
            "+337122",
            "+33612886370",
            # National format, if parameter country_iso is used
            "0612886370",
        ],
        # country_iso="FR",
    ) # NumbersValidateRequest | 

try:
    # Validate numbers in bulk
    api_response = api_instance.validate_numbers(numbers_validate_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->validate_numbers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numbers_validate_request** | [**NumbersValidateRequest**](../model/NumbersValidateRequest.md)|  | required

### Return type

[**NumbersValidateResponse**](../model/NumbersValidateResponse.md)

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


# **get_available_numbers()**
> RentNumbersResponse get_available_numbers(country_iso)

Get available numbers for rent

Get the list of available phone numbers for rent

### Errors for GET `/numbers/rent/available/{countryIso}`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 2003  |  invalid_param  |  Country ISO provided is invalid |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import numbers_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = numbers_api.NumbersApi(
    smscx_client.ApiClient(configuration)
)    
country_iso = "FR" # str | 
features = 3 # int | Filter by number features (1 - receive SMS, 2 - send SMS, 1 + 2 = 3 - send and receive SMS) (optional)
number_type = "mobile" # str | Filter by type of phone number (optional)
setup_time = "instant" # str | Filter by time of setup (optional)
registration = True # bool | Filter by registration (optional)
inbound_sms_sender = True # bool | Filter numbers that support inbound SMS from alphanumeric sender ID (optional)
include = "4559" # str | Filter phone numbers that include the following digits (optional)
exclude = "1554" # str | Filter phone numbers that exclude the following digits (optional)

# example passing only required values which don't have defaults set
try:
    # Get available numbers for rent
    api_response = api_instance.get_available_numbers(country_iso)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->get_available_numbers: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get available numbers for rent
    api_response = api_instance.get_available_numbers(country_iso, features=features, number_type=number_type, setup_time=setup_time, registration=registration, inbound_sms_sender=inbound_sms_sender, include=include, exclude=exclude)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->get_available_numbers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_iso** | **str**|  | required
 **features** | **int**| Filter by number features (1 - receive SMS, 2 - send SMS, 1 + 2 &#x3D; 3 - send and receive SMS) | [optional]
 **number_type** | **str**| Filter by type of phone number | [optional]
 **setup_time** | **str**| Filter by time of setup | [optional]
 **registration** | **bool**| Filter by registration | [optional]
 **inbound_sms_sender** | **bool**| Filter numbers that support inbound SMS from alphanumeric sender ID | [optional]
 **include** | **str**| Filter phone numbers that include the following digits | [optional]
 **exclude** | **str**| Filter phone numbers that exclude the following digits | [optional]

### Return type

[**RentNumbersResponse**](../model/RentNumbersResponse.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth), [BearerAuth](../../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **rent_number()**<span>💰</span>
> RentNumberResponse rent_number(rent_number_request)

Rent phone number

Rent a phone number for a period of time (1, 7 or 30 days).

### Errors for POST `/numbers/rent`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1222  |  invalid_param  |  Invalid parameter `numberId` |  
|  400 | 1224  |  invalid_param  |  Rent period is invalid (1, 7 or 30 days) |  
|  400 | 1225  |  invalid_param  |  Parameter `autorenew` must be type boolean |  
|  400 | 1226  |  invalid_param  |  The parameter `callbackUrl` is not a valid url |  
|  400 | 1229  |  invalid_param  |  Rent period is lower than the minimum rent period of this number |  
|  400 | 1113  |  insufficient_credit  |  Insufficient credit |  
|  400 | 1234  |  invalid_param  |  Registration ID provided is invalid or not found |  
|  403 | 1231  |  access_denied  |  Cannot rent this phone number (already rented) |  
|  404 | 1230  |  not_found  |  Number ID not found or number is not available for rent anymore|  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import numbers_api
from smscx_client.model.rent_number_request import RentNumberRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = numbers_api.NumbersApi(
    smscx_client.ApiClient(configuration)
)    
rent_number_request = RentNumberRequest(
        number_id="bf325375-e030-fccb-a009-17317c574773",
        rent_period=30,
        auto_renew=False,
        callback_url="https://webhook/receive-inbound-sms/",
        # registration_id="bf325375-e030-fccb-a009-17317c574773",

    )

try:
    # Rent phone number
    api_response = api_instance.rent_number(rent_number_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->rent_number: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rent_number_request** | [**RentNumberRequest**](../model/RentNumberRequest.md)|  | required

### Return type

[**RentNumberResponse**](../model/RentNumberResponse.md)

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

# **cancel_rent()**
> CancelRentResponse cancel_rent(rent_id)

Cancel rent for phone number

Cancel rent for a phone number. Phone numbers rentals can be canceled within the first 30 minutes of renting period. Your account will be credited for the phone number rental cost.

### Errors for DELETE `/numbers/rent/{rentId}`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1221  |  invalid_param  |  The rentId provided is invalid |  
|  403 | 1227  |  access_denied  |  Cannot cancel this rent. More than 30 minutes passed from start of renting period |  
|  403 | 1232  |  access_denied  |  Cannot cancel this rent. The number has already been used for inbound SMS |  
|  404 | 1223  |  not_found  |  Rent ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import numbers_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = numbers_api.NumbersApi(
    smscx_client.ApiClient(configuration)
)    

# Identifier of the rental operation
rent_id = "471ddea7-930c-49e8-8e99-2683834dd92e"

try:
    # Cancel rent for phone number
    api_response = api_instance.cancel_rent(rent_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->cancel_rent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rent_id** | **str**| Identifier of the rental operation | required

### Return type

[**CancelRentResponse**](../model/CancelRentResponse.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth), [BearerAuth](../../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **renew_rent()**<span>💰</span>
> RenewNumberResponse renew_rent(rent_id, renew_rent_request)

Renew rent for phone number

Renew the rental of a phone number.

### Errors for PATCH `/numbers/rent/{rentId}`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1221  |  invalid_param  |  The rentId provided is invalid |  
|  400 | 1224  |  invalid_param  |  Rent period is invalid (1, 7 or 30 days) |  
|  400 | 1225  |  invalid_param  |  Parameter `autorenew` must be type boolean |  
|  400 | 1226  |  invalid_param  |  The parameter `callbackUrl` is not a valid url |  
|  400 | 1229  |  invalid_param  |  Rent period is lower than the minimum rent period of this number |  
|  400 | 1113  |  insufficient_credit  |  Insufficient credit |  
|  403 | 1228  |  access_denied  |  The rent cannot be renewed (rent already expired or phone number is not available for future rent) |  
|  404 | 1223  |  not_found  |  Rent ID not found |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import numbers_api
from smscx_client.model.renew_rent_request import RenewRentRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = numbers_api.NumbersApi(
    smscx_client.ApiClient(configuration)
)    

# Identifier of the rental operation
rent_id = "471ddea7-930c-49e8-8e99-2683834dd92e" 
renew_rent_request = RenewRentRequest(
        rent_period=30,
        auto_renew=False,
        callback_url="https://webhook/receive-sms-endpoint",
    ) # RenewRentRequest | 

try:
    # Renew rent for phone number
    api_response = api_instance.renew_rent(rent_id, renew_rent_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->renew_rent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rent_id** | **str**| Identifier of the rental operation | required
 **renew_rent_request** | [**RenewRentRequest**](../model/RenewRentRequest.md)|  | required

### Return type

[**RenewNumberResponse**](../model/RenewNumberResponse.md)

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

# **get_rent_status()**
> GetRentStatusResponse get_rent_status(rent_id)

Get status of rent

Get details of an existing rental.      

### Errors for GET `/numbers/rent/{rentId}`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1221  |  invalid_param  |  Invalid parameter `rentId` |  
|  404 | 1223  |  not_found  |  Rent ID not found |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import numbers_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = numbers_api.NumbersApi(
    smscx_client.ApiClient(configuration)
)    

# Identifier of the rental operation
rent_id = "471ddea7-930c-49e8-8e99-2683834dd92e" 

try:
    # Get status of rent
    api_response = api_instance.get_rent_status(rent_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->get_rent_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rent_id** | **str**| Identifier of the rental operation | required

### Return type

[**GetRentStatusResponse**](../model/GetRentStatusResponse.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth), [BearerAuth](../../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **get_rented_numbers()**
> RentedNumbersResponse get_rented_numbers()

Get list of your rented numbers

Get the list of your rented phone numbers

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import numbers_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = numbers_api.NumbersApi(
    smscx_client.ApiClient(configuration)
)    

features = 3 # int | Filter by number features (1 - receive SMS, 2 - send SMS, 1 + 2 = 3 - send and receive SMS) (optional)
country_iso = "fr" # str | Filter by country iso. Two-letter country code defined in ISO-3166 alpha 2 standard (case insensitive) (optional)
number_type = "mobile" # str | Filter by type of phone number (optional)
active_rent = True # bool | Filter by active rent (optional)
inbound_sms_sender = True # bool | Filter numbers that support inbound SMS from alphanumeric sender ID (optional)
include = "4559" # str | Filter phone numbers that include the following digits (optional)
exclude = "1554" # str | Filter phone numbers that exclude the following digits (optional)


try:
    # Get list of your rented numbers
    api_response = api_instance.get_rented_numbers()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->get_rented_numbers: %s\n" % e)


try:
    # Get list of your rented numbers
    api_response = api_instance.get_rented_numbers(features=features, country_iso=country_iso, number_type=number_type, active_rent=active_rent, inbound_sms_sender=inbound_sms_sender, include=include, exclude=exclude)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->get_rented_numbers: %s\n" % e)
```


### Parameters
 **features** | **int**| Filter by number features (1 - receive SMS, 2 - send SMS, 1 + 2 &#x3D; 3 - send and receive SMS) | [optional]
 **country_iso** | **str**| Filter by country iso. Two-letter country code defined in ISO-3166 alpha 2 standard (case insensitive) | [optional]
 **number_type** | **str**| Filter by type of phone number | [optional]
 **active_rent** | **bool**| Filter by active rent | [optional]
 **inbound_sms_sender** | **bool**| Filter numbers that support inbound SMS from alphanumeric sender ID | [optional]
 **include** | **str**| Filter phone numbers that include the following digits | [optional]
 **exclude** | **str**| Filter phone numbers that exclude the following digits | [optional]

### Return type

[**RentedNumbersResponse**](../model/RentedNumbersResponse.md)

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

# **get_inbound_sms()**
> GetInboundSMSResponse get_inbound_sms(rent_id)

Get inbound SMS from rented number

Get a list of SMS received on the rented phone number.

### Errors for GET `/numbers/rent/{rentId}/inbound`  

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1221  |  invalid_param  |  Invalid parameter `rentId` |  
|  404 | 1223  |  not_found  |  Rent ID not found |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import numbers_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = numbers_api.NumbersApi(
    smscx_client.ApiClient(configuration)
)    

# Identifier of the rental operation
rent_id = "471ddea7-930c-49e8-8e99-2683834dd92e"

try:
    # Get inbound SMS from rented number
    api_response = api_instance.get_inbound_sms(rent_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->get_inbound_sms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rent_id** | **str**| Identifier of the rental operation | required

### Return type

[**GetInboundSMSResponse**](../model/GetInboundSMSResponse.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth), [BearerAuth](../../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **edit_rent_settings()**
> EditRentResponse edit_rent_settings(rent_id, edit_rent_request)

Edit settings for active rent

### Errors for GET `/numbers/rent/{rentId}/edit`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1221  |  invalid_param  |  The rentId provided is invalid |  
|  400 | 1225  |  invalid_param  |  Parameter `autorenew` must be type boolean |  
|  400 | 1226  |  invalid_param  |  The parameter `callbackUrl` is not a valid url |  
|  400 | 1233  |  invalid_param  |  At least one parameter required (autoRenew, callbackUrl) |  
|  404 | 1223  |  not_found  |  Rent ID not found |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import numbers_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = numbers_api.NumbersApi(
    smscx_client.ApiClient(configuration)
)    
rent_id = "471ddea7-930c-49e8-8e99-2683834dd92e" # str | Identifier of the rental operation
edit_rent_request = EditRentRequest(
        auto_renew=False,
        callback_url="https://webhook/receive-sms-endpoint",
    ) # EditRentRequest | 

try:
    # Edit settings for active rent
    api_response = api_instance.edit_rent_settings(rent_id, edit_rent_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->edit_rent_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rent_id** | **str**| Identifier of the rental operation | required |
 **edit_rent_request** | [**EditRentRequest**](../model/EditRentRequest.md)|  | required |

### Return type

[**EditRentResponse**](../model/EditRentResponse.md)

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
