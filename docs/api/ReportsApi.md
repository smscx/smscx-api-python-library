# smscx_client.ReportsApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_advanced_report_to_csv()**](ReportsApi.md#export_advanced_report_to_csv) | **GET** /reports/csv | Export advanced report to CSV
[**export_advanced_report_to_xlsx()**](ReportsApi.md#export_advanced_report_to_xlsx) | **GET** /reports/xlsx | Export advanced report to XLSX
[**export_campaign_report_to_csv()**](ReportsApi.md#export_campaign_report_to_csv) | **GET** /reports/campaigns/{campaignId}/csv | Export campaign report to CSV
[**export_campaign_report_to_xlsx()**](ReportsApi.md#export_campaign_report_to_xlsx) | **GET** /reports/campaigns/{campaignId}/xlsx | Export campaign report to XLSX
[**get_advanced_report()**](ReportsApi.md#get_advanced_report) | **GET** /reports | Get advanced report
[**get_campaign_report()**](ReportsApi.md#get_campaign_report) | **GET** /reports/campaigns/{campaignId} | Get campaign report
[**get_campaigns_list()**](ReportsApi.md#get_campaigns_list) | **GET** /reports/campaigns | Get list of sent campaigns
[**get_single_report()**](ReportsApi.md#get_single_report) | **GET** /reports/single/{msgId} | Get report for single SMS or Viber or Whatsapp or Multichannel
[**get_summary_reports()**](ReportsApi.md#get_summary_reports) | **GET** /reports/summary/{dimension} | Get summary reports for a dimension


# **export_advanced_report_to_csv()**
> str export_advanced_report_to_csv(period, start_date, end_date)

Export advanced report to CSV

Exports the report for for the specified filters to a CSV file.  

The only required parameters are the dates filters: `period` parameter or `start_date` and `end_date`.    

If no data is available for the report, an empty CSV file is returned (with first line headers).

### Errors for GET `/reports/csv`

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1820  |  invalid_param  |  The parameter `period` is not a valid date (format Y-m or Y) |  
|  400 | 1821  |  invalid_param  |  The parameter `start_date` is not a valid date |  
|  400 | 1822  |  invalid_param  |  The parameter `end_date` is not a valid date |  
|  400 | 1823  |  invalid_param  |  The end date is before the start date |  
|  400 | 1824  |  invalid_param  |  No `period` parameter or interval (`start_date`, `end_date`) |  
|  400 | 1825  |  invalid_param  |  The parameter `source` is not valid |  
|  400 | 1826  |  invalid_param  |  The parameter `delivery_report` is not valid (delivered, failed or sent) |  
|  400 | 1827  |  invalid_param  |  The parameter `country_iso` is not for a valid country  |  
|  400 | 1828  |  invalid_param  |  The parameter `channel` is not valid (sms, viber, whatsapp, multichannel) |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import reports_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = reports_api.ReportsApi(
    smscx_client.ApiClient(configuration)
)    
period = "2021-07" # str | Period for the requested report in format **Y-M** or **Y**
start_date = "2021-03-01" # str | The start date of the report in format Y-M-D
end_date = "2021-04-30" # str | The end date of the report in format Y-M-D
channel = "sms" # str | Channel of the sent messages (optional)
source = "api" # str | Source of the sent messages (optional)
delivery_report = "delivered" # str |  (optional)
country_iso = "fr" # str | Two-letter country code defined in ISO-3166 alpha 2 standard (case insensitive) (optional)
limit = 100 # int | A limit on the number of objects to be returned (optional) if omitted the server will use the default value of 500

try:
    # Export advanced report to CSV
    api_response = api_instance.export_advanced_report_to_csv(period, start_date, end_date)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->export_advanced_report_to_csv: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Export advanced report to CSV
    api_response = api_instance.export_advanced_report_to_csv(period, start_date, end_date, channel=channel, source=source, delivery_report=delivery_report, country_iso=country_iso, limit=limit)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->export_advanced_report_to_csv: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**| Period for the requested report in format **Y-M** or **Y** |
 **start_date** | **str**| The start date of the report in format Y-M-D |
 **end_date** | **str**| The end date of the report in format Y-M-D |
 **channel** | **str**| Channel of the sent messages | [optional]
 **source** | **str**| Source of the sent messages | [optional]
 **delivery_report** | **str**|  | [optional]
 **country_iso** | **str**| Two-letter country code defined in ISO-3166 alpha 2 standard (case insensitive) | [optional]
 **limit** | **int**| A limit on the number of objects to be returned | [optional] if omitted the server will use the default value of 500

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
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#available-methods) [[Back to Model list]](../../README.md#models) [[Back to README]](../../README.md)

# **export_advanced_report_to_xlsx()**
> file_type export_advanced_report_to_xlsx(period, start_date, end_date)

Export advanced report to XLSX

Exports the report for for the specified filters to a XLSX file (Excel).  

The only required parameters are the dates filters: `period` parameter or `start_date` and `end_date`.    

If no data is available for the report, an empty XLSX file is returned (with first line headers). 

### Errors for GET `/reports/xlsx`

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1820  |  invalid_param  |  The parameter `period` is not a valid date (format Y-m or Y) |  
|  400 | 1821  |  invalid_param  |  The parameter `start_date` is not a valid date |  
|  400 | 1822  |  invalid_param  |  The parameter `end_date` is not a valid date |  
|  400 | 1823  |  invalid_param  |  The end date is before the start date |  
|  400 | 1824  |  invalid_param  |  No `period` parameter or interval (`start_date`, `end_date`) |  
|  400 | 1825  |  invalid_param  |  The parameter `source` is not valid |  
|  400 | 1826  |  invalid_param  |  The parameter `delivery_report` is not valid (delivered, failed or sent) |  
|  400 | 1827  |  invalid_param  |  The parameter `country_iso` is not for a valid country  |  
|  400 | 1828  |  invalid_param  |  The parameter `channel` is not valid (sms, viber, whatsapp, multichannel) |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import reports_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = reports_api.ReportsApi(
    smscx_client.ApiClient(configuration)
)    
period = "2021-07" # str | Period for the requested report in format **Y-M** or **Y**
start_date = "2021-03-01" # str | The start date of the report in format Y-M-D
end_date = "2021-04-30" # str | The end date of the report in format Y-M-D
channel = "sms" # str | Channel of the sent messages (optional)
source = "api" # str | Source of the sent messages (optional)
delivery_report = "delivered" # str |  (optional)
country_iso = "fr" # str | Two-letter country code defined in ISO-3166 alpha 2 standard (case insensitive) (optional)
limit = 100 # int | A limit on the number of objects to be returned (optional) if omitted the server will use the default value of 500

try:
    # Export advanced report to XLSX
    api_response = api_instance.export_advanced_report_to_xlsx(period, start_date, end_date)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->export_advanced_report_to_xlsx: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Export advanced report to XLSX
    api_response = api_instance.export_advanced_report_to_xlsx(period, start_date, end_date, channel=channel, source=source, delivery_report=delivery_report, country_iso=country_iso, limit=limit)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->export_advanced_report_to_xlsx: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**| Period for the requested report in format **Y-M** or **Y** |
 **start_date** | **str**| The start date of the report in format Y-M-D |
 **end_date** | **str**| The end date of the report in format Y-M-D |
 **channel** | **str**| Channel of the sent messages | [optional]
 **source** | **str**| Source of the sent messages | [optional]
 **delivery_report** | **str**|  | [optional]
 **country_iso** | **str**| Two-letter country code defined in ISO-3166 alpha 2 standard (case insensitive) | [optional]
 **limit** | **int**| A limit on the number of objects to be returned | [optional] if omitted the server will use the default value of 500

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
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#available-methods) [[Back to Model list]](../../README.md#models) [[Back to README]](../../README.md)

# **export_campaign_report_to_csv()**
> str export_campaign_report_to_csv(campaign_id)

Export campaign report to CSV

Exports the details of a sent campaign to a CSV file.

### Errors for GET `/reports/campaigns/{campaignId}/csv`

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1165  |  invalid_param  |  Campaign ID or msg ID provided is not valid  |
|  404 | 1160  |  not_found  |  Campaign ID or msg ID provided was not found  |    

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import reports_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = reports_api.ReportsApi(
    smscx_client.ApiClient(configuration)
)    
campaign_id = "4baf0298-0c21-4df1-a60a-6e3476e95e0b"

try:
    # Export campaign report to CSV
    api_response = api_instance.export_campaign_report_to_csv(campaign_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->export_campaign_report_to_csv: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Identifier of a sent campaign | required

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

# **export_campaign_report_to_xlsx()**
> file_type export_campaign_report_to_xlsx(campaign_id)

Export campaign report to XLSX

Exports the details of a sent campaign to a XLSX file (Excel).

### Errors for GET `/reports/campaigns/{campaignId}/xlsx`

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1165  |  invalid_param  |  Campaign ID or msg ID provided is not valid  |
|  404 | 1160  |  not_found  |  Campaign ID or msg ID provided was not found  |    

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import reports_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = reports_api.ReportsApi(
    smscx_client.ApiClient(configuration)
)
campaign_id = "4baf0298-0c21-4df1-a60a-6e3476e95e0b"

try:
    # Export campaign report to XLSX
    api_response = api_instance.export_campaign_report_to_xlsx(campaign_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->export_campaign_report_to_xlsx: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Identifier of a sent campaign | required

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

# **get_advanced_report()**
> ReportsAdvancedResponse get_advanced_report(period, start_date, end_date)

Get advanced report

Retrieves the report for the specified filters.  

The only required parameters are the dates filters: `period` parameter or `start_date` and `end_date`.    

If no data is available for the report, an empty data object is returned.

### Errors for GET `/reports`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1820  |  invalid_param  |  The parameter `period` is not a valid date (format Y-m or Y) |  
|  400 | 1821  |  invalid_param  |  The parameter `start_date` is not a valid date |  
|  400 | 1822  |  invalid_param  |  The parameter `end_date` is not a valid date |  
|  400 | 1823  |  invalid_param  |  The end date is before the start date |  
|  400 | 1824  |  invalid_param  |  No `period` parameter or interval (`start_date`, `end_date`) |  
|  400 | 1825  |  invalid_param  |  The parameter `source` is not valid |  
|  400 | 1826  |  invalid_param  |  The parameter `delivery_report` is not valid (delivered, failed or sent) |  
|  400 | 1827  |  invalid_param  |  The parameter `country_iso` is not for a valid country  |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import reports_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = reports_api.ReportsApi(
    smscx_client.ApiClient(configuration)
)    
period = "2021-07" # str | Period for the requested report in format **Y-M** or **Y**
start_date = "2021-03-01" # str | The start date of the report in format Y-M-D
end_date = "2021-04-30" # str | The end date of the report in format Y-M-D
channel = "sms" # str | Channel of the sent messages (optional)
source = "api" # str | Source of the sent messages (optional)
delivery_report = "delivered" # str |  (optional)
country_iso = "fr" # str | Two-letter country code defined in ISO-3166 alpha 2 standard (case insensitive) (optional)
short_response = False # bool | If set to true, it will return the full `info` object and an empty `data` object (optional) if omitted the server will use the default value of False
limit = 100 # int | A limit on the number of objects to be returned (optional) if omitted the server will use the default value of 500
next = "NTM2NTA" # str | The next token used to retrieve additional data (optional)
previous = "NTQxNTA" # str | The previous token used to retrieve additional data (optional)

try:
    # Get advanced report
    api_response = api_instance.get_advanced_report(period, start_date, end_date)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->get_advanced_report: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get advanced report
    api_response = api_instance.get_advanced_report(period, start_date, end_date, channel=channel, source=source, delivery_report=delivery_report, country_iso=country_iso, short_response=short_response, limit=limit, next=next, previous=previous)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->get_advanced_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**| Period for the requested report in format **Y-M** or **Y** |
 **start_date** | **str**| The start date of the report in format Y-M-D |
 **end_date** | **str**| The end date of the report in format Y-M-D |
 **channel** | **str**| Channel of the sent messages | [optional]
 **source** | **str**| Source of the sent messages | [optional]
 **delivery_report** | **str**|  | [optional]
 **country_iso** | **str**| Two-letter country code defined in ISO-3166 alpha 2 standard (case insensitive) | [optional]
 **short_response** | **bool**| If set to true, it will return the full &#x60;info&#x60; object and an empty &#x60;data&#x60; object | [optional] if omitted the server will use the default value of False
 **limit** | **int**| A limit on the number of objects to be returned | [optional] if omitted the server will use the default value of 500
 **next** | **str**| The next token used to retrieve additional data | [optional]
 **previous** | **str**| The previous token used to retrieve additional data | [optional]

### Return type

[**ReportsAdvancedResponse**](../model/ReportsAdvancedResponse.md)

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

# **get_campaign_report()**
> ReportsCampaignResponse get_campaign_report(campaign_id)

Get campaign report

Returns the details of a sent campaign if a valid identifier was provided.

### Errors for GET `/reports/campaigns/{campaignId}`

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1155  |  invalid_param  |  Campaign ID provided is not valid |
|  404 | 1150  |  not_found  |  Campaign ID provided was not found |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import reports_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = reports_api.ReportsApi(
    smscx_client.ApiClient(configuration)
)    
campaign_id = "4baf0298-0c21-4df1-a60a-6e3476e95e0b" # str | Identifier of a sent campaign
short_response = False # bool | If set to true, it will return the full `info` object and an empty `data` object (optional) if omitted the server will use the default value of False
limit = 100 # int | A limit on the number of objects to be returned (optional) if omitted the server will use the default value of 500
next = "NTM2NTA" # str | The next token used to retrieve additional data (optional)
previous = "NTQxNTA" # str | The previous token used to retrieve additional data (optional)

try:
    # Get campaign report
    api_response = api_instance.get_campaign_report(campaign_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->get_campaign_report: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get campaign report
    api_response = api_instance.get_campaign_report(campaign_id, short_response=short_response, limit=limit, next=next, previous=previous)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->get_campaign_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Identifier of a sent campaign |
 **short_response** | **bool**| If set to true, it will return the full &#x60;info&#x60; object and an empty &#x60;data&#x60; object | [optional] if omitted the server will use the default value of False
 **limit** | **int**| A limit on the number of objects to be returned | [optional] if omitted the server will use the default value of 500
 **next** | **str**| The next token used to retrieve additional data | [optional]
 **previous** | **str**| The previous token used to retrieve additional data | [optional]

### Return type

[**ReportsCampaignResponse**](../model/ReportsCampaignResponse.md)

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

# **get_campaigns_list()**
> ReportsCampaignsRespone get_campaigns_list()

Get list of sent campaigns

Returns a list of sent Campaigns, with the most recent appearing first.    

If no data is available, an empty data object is returned.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import reports_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = reports_api.ReportsApi(
    smscx_client.ApiClient(configuration)
)    
delivery_reports = True # bool | The response will contain an object **data.status** with delivery report summary for each campaign (optional) if omitted the server will use the default value of False
source = "api" # str | Source of the sent messages (optional)
limit = 100 # int | A limit on the number of objects to be returned (optional) if omitted the server will use the default value of 500
next = "NTM2NTA" # str | The next token used to retrieve additional data (optional)
previous = "NTQxNTA" # str | The previous token used to retrieve additional data (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get list of sent campaigns
    api_response = api_instance.get_campaigns_list(delivery_reports=delivery_reports, source=source, limit=limit, next=next, previous=previous)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->get_campaigns_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_reports** | **bool**| The response will contain an object **data.status** with delivery report summary for each campaign | [optional] if omitted the server will use the default value of False
 **source** | **str**| Source of the sent messages | [optional]
 **limit** | **int**| A limit on the number of objects to be returned | [optional] if omitted the server will use the default value of 500
 **next** | **str**| The next token used to retrieve additional data | [optional]
 **previous** | **str**| The previous token used to retrieve additional data | [optional]

### Return type

[**ReportsCampaignsRespone**](../model/ReportsCampaignsRespone.md)

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

# **get_single_report()**
> ReportSingleResponse get_single_report(msg_id)

Get report for single SMS or Viber or Whatsapp or Multichannel

Returns the details of a single message if a valid identifier was provided.    

### Errors for GET `/reports/single/{msgId} `

| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1165  |  invalid_param  |  Campaign ID or msg ID provided is not valid  |
|  404 | 1160  |  not_found  |  Campaign ID or msg ID provided was not found  |    

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import reports_api
from smscx_client.model.report_single_response import ReportSingleResponse
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = reports_api.ReportsApi(
    smscx_client.ApiClient(configuration)
)    
msg_id = "9eeed792-9c8c-463c-a8e2-43ebf4494c02"

try:
    # Get report for single SMS or Viber or Whatsapp or Multichannel
    api_response = api_instance.get_single_report(msg_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->get_single_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msg_id** | **str**| Identifier of a sent message | required

### Return type

[**ReportSingleResponse**](../model/ReportSingleResponse.md)

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

# **get_summary_reports()**
> GetSummaryReports200Response get_summary_reports(dimension, period, start_date, end_date)

Get summary reports for a dimension

Retrieves a summary report for the specified dimensions.   

The only required parameters are the dates for the report. 

The date filters can be: with `period` parameter or with `start_date` and `end_date`    

For some dimensions (**traffic** and **delivery**) the summary report will aggregate on dates.   

If the summary report was requested with **period** parameter, the dates will be months or days.  

If it was requested with interval **start_date** - **end_date**, the dates will be the days between the interval.    

Eg. period=2011, the property will be all months in the year  
period=2011-06, the property will be all days in month   
start_date=2021-06-15, end_date=2021-06-30, the properties will be all days between the interval      

If no data is available for the summary report an empty data object is returned.      
### Errors for GET `/reports/summary/{dimension}`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1829  |  invalid_param  |  Invalid dimension. Accepted dimensions: source, channel, country, traffic, delivery |    
|  400 | 1820  |  invalid_param  |  The parameter `period` is not a valid date (format Y-m or Y) |  
|  400 | 1821  |  invalid_param  |  The parameter `start_date` is not a valid date |  
|  400 | 1822  |  invalid_param  |  The parameter `end_date` is not a valid date |  
|  400 | 1823  |  invalid_param  |  The end date is before the start date |  
|  400 | 1824  |  invalid_param  |  No `period` parameter or interval (`start_date`, `end_date`) |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import reports_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = reports_api.ReportsApi(
    smscx_client.ApiClient(configuration)
)    
dimension = "source" # str | Dimension for wich the summary report is requested
period = "2021-07" # str | Period for the requested report in format **Y-M** or **Y**
start_date = "2021-03-01" # str | The start date of the report in format Y-M-D
end_date = "2021-04-30" # str | The end date of the report in format Y-M-D
limit = 100 # int | A limit on the number of objects to be returned (optional) if omitted the server will use the default value of 500

try:
    # Get summary reports for a dimension
    api_response = api_instance.get_summary_reports(dimension, period, start_date, end_date)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->get_summary_reports: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get summary reports for a dimension
    api_response = api_instance.get_summary_reports(dimension, period, start_date, end_date, limit=limit)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->get_summary_reports: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dimension** | **str**| Dimension for wich the summary report is requested |
 **period** | **str**| Period for the requested report in format **Y-M** or **Y** |
 **start_date** | **str**| The start date of the report in format Y-M-D |
 **end_date** | **str**| The end date of the report in format Y-M-D |
 **limit** | **int**| A limit on the number of objects to be returned | [optional] if omitted the server will use the default value of 500

### Return type

[**GetSummaryReports200Response**](../model/GetSummaryReports200Response.md)

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
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../../README.md#available-methods) [[Back to Model list]](../../README.md#models) [[Back to README]](../../README.md)

