# smscx_client.AccountApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_balance()**](AccountApi.md#get_account_balance) | **GET** /account/balance | Get account balance
[**get_channel_pricing()**](AccountApi.md#get_channel_pricing) | **GET** /account/pricing/{channel}/{trafficType} | Get channels pricing
[**get_channel_pricing_by_country_iso()**](AccountApi.md#get_channel_pricing_by_country_iso) | **GET** /account/pricing/{channel}/{trafficType}/{countryIso} | Get pricing for channel by country iso
[**get_channels_status()**](AccountApi.md#get_channels_status) | **GET** /account/channels/status | Get status of all channels


# **get_account_balance()**
> AccountBalance get_account_balance()

Get account balance

Retrieves the account balance, currency (eur, usd), billing (prepaid, postpaid).

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import account_api
from smscx_client.model.account_balance import AccountBalance
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = account_api.AccountApi(
    smscx_client.ApiClient(configuration)
)    

try:
    # Get account balance
    api_response = api_instance.get_account_balance()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling AccountApi->get_account_balance: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountBalance**](../model/AccountBalance.md)

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

# **get_channel_pricing()**
> GetChannelPricing200Response get_channel_pricing(channel, traffic_type)

Get channels pricing

Retrieves the full pricing for the requested channel.    
### Errors for GET `/account/pricing/{channel}/{trafficType}`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1521  |  invalid_param  | The channel requested is not valid |  
|  403 | 1523  |  no_coverage  | No coverage |


### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import account_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = account_api.AccountApi(
    smscx_client.ApiClient(configuration)
)    
channel = "sms"
traffic_type = "transactional"

try:
    # Get channels pricing
    api_response = api_instance.get_channel_pricing(channel, traffic_type)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling AccountApi->get_channel_pricing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel** | **str**|  | required
 **traffic_type** | **str**|  | required

### Return type

[**GetChannelPricing200Response**](../model/GetChannelPricing200Response.md)

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

# **get_channel_pricing_by_country_iso()**
> GetChannelPricing200Response get_channel_pricing_by_country_iso(channel, traffic_type, country_iso)

Get pricing for channel by country iso

Retrieves the pricing for the requested channel, for a specific country ISO.    
### Errors for `/account/pricing/{channel}/{trafficType}/{countryIso}`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1521  |  invalid_param  | The channel requested is not valid |  
|  400 | 1522  |  invalid_param  | Invalid country iso |  
|  403 | 1523  |  no_coverage  | No coverage |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import account_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = account_api.AccountApi(
    smscx_client.ApiClient(configuration)
)    
channel = "sms" # str | 
traffic_type = "transactional" # str | 
country_iso = "FR" # str | 

try:
    # Get pricing for channel by country iso
    api_response = api_instance.get_channel_pricing_by_country_iso(channel, traffic_type, country_iso)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling AccountApi->get_channel_pricing_by_country_iso: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel** | **str**|  | required
 **traffic_type** | **str**|  | required
 **country_iso** | **str**|  | required

### Return type

[**GetChannelPricing200Response**](../model/GetChannelPricing200Response.md)

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

# **get_channels_status()**
> ChannelsStatus get_channels_status()

Get status of all channels

Retrieves the active status of all channels (true for active, false for inactive)

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import account_api
from smscx_client.model.channels_status import ChannelsStatus

from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = account_api.AccountApi(
    smscx_client.ApiClient(configuration)
)    

try:
    # Get status of all channels
    api_response = api_instance.get_channels_status()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling AccountApi->get_channels_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ChannelsStatus**](../model/ChannelsStatus.md)

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

