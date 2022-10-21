# smscx_client.OauthApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_token()**](OauthApi.md#get_access_token) | **POST** /oauth/token | Get access token


# **get_access_token()**
> OauthTokenResponse get_access_token()

Get access token

Generate an access token.    
  
### Errors for POST `/oauth/token`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
|  400 | 1600  |  invalid_request  |  The request is missing a required parameter (grant_type) |  
|  400 | 1600  |  invalid_scope  |  The requested scope is invalid, unknown, or malformed |  
|  400 | 1600  |  unsupported_grant_type  |  The grant type is not supported (only client_credentials) |  
|  401 | 1600  |  invalid_client  |  Invalid client |

### Example

* Basic Authentication (BasicAuth):

```python
import time
import smscx_client
from smscx_client.api import oauth_api
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = smscx_client.Configuration(
    username = "YOUR_APPLICATION_ID",
    password = "YOUR_APPLICATION_SECRET"
)

# Create an instance of the API class
api_instance = oauth_api.OauthApi(
    smscx_client.ApiClient(configuration)
)    

# A list of space-delimited, case-sensitive strings. If left empty or ommited, the issued access token will be granted with all scopes (full privileges) (optional)
scope = "sms groups templates originators numbers reports templates shortlinks"

try:
    # Get access token
    api_response = api_instance.get_access_token()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OauthApi->get_access_token: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get access token
    api_response = api_instance.get_access_token(scope=scope)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OauthApi->get_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| Grant type (or flow) represents the methods through which the application will get Access Tokens. Must have value &#x60;client_credentials&#x60; | defaults to "client_credentials"
 **scope** | **str**| A list of space-delimited, case-sensitive strings. If left empty or ommited, the issued access token will be granted with all scopes (full privileges) | [optional]

### Return type

[**OauthTokenResponse**](../model/OauthTokenResponse.md)

### Authorization

[BasicAuth](../../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
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

