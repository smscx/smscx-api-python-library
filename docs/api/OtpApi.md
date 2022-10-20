# smscx_client.OtpApi

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_otp()**](OtpApi.md#cancel_otp) | **DELETE** /otp/{otpId} | Cancel OTP
[**get_otp_status()**](OtpApi.md#get_otp_status) | **GET** /otp/{otpId} | Get OTP status
[**new_otp()**](OtpApi.md#new_otp) 💰 | **POST** /otp | New OTP
[**verify_otp()**](OtpApi.md#verify_otp) | **POST** /otp/{otpId} | Verify OTP


# **cancel_otp()**
> CancelOtpResponse cancel_otp(otp_id)

Cancel OTP

Cancel OTP request if a valid identifier was provided.

### Errors for DELETE `/otp/{otpId}`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
| 403 | 2030 | access_denied | Otp already cancelled |  
| 403 | 2031 | access_denied | You cannot cancel a non-pending Otp |
| 404 | 2021 | not_found | Otp ID not found |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import otp_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = otp_api.OtpApi(
    smscx_client.ApiClient(configuration)
)    
otp_id = "a17fb13d-f4ac-4d93-9439-ef41ab8de390"

try:
    # Cancel OTP
    api_response = api_instance.cancel_otp(otp_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OtpApi->cancel_otp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otp_id** | **str**| Identifier of the OTP request | required

### Return type

[**CancelOtpResponse**](../model/CancelOtpResponse.md)

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

# **get_otp_status()**
> DataOtp get_otp_status(otp_id)

Get OTP status

Retrieves the details of OTP status if a valid identifier was provided.    

### Status for OTP requests  
| Status | Description |  
|:------------:|:------------|  
| PENDING | The OTP is pending validation by user |  
| VERIFIED | The OTP was validated by user |  
| EXPIRED | The validity of OTP has expired |  
| CANCELLED | The OTP was cancelled by the user |  
| FAILED | The OTP failed because too many unsuccessful attempts |

### Errors for GET `/otp/{otpId}`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
| 404 | 2021 | not_found | Otp ID not found |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import otp_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = otp_api.OtpApi(
    smscx_client.ApiClient(configuration)
)    
otp_id = "a17fb13d-f4ac-4d93-9439-ef41ab8de390"

try:
    # Get OTP status
    api_response = api_instance.get_otp_status(otp_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OtpApi->get_otp_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otp_id** | **str**| Identifier of the OTP request | required

### Return type

[**DataOtp**](../model/DataOtp.md)

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

# **new_otp()**<span>💰</span>
> NewOtpResponse new_otp(new_otp_request)

New OTP

Create a OTP request to verify a phone number.    

### Status for OTP requests  

| Status | Description |  
|:------------:|:------------|  
| PENDING | The OTP is pending validation by user |  
| VERIFIED | The OTP was validated by user |  
| EXPIRED | The validity of OTP has expired |  
| CANCELLED | The OTP was cancelled by the user |  
| FAILED | The OTP failed because too many unsuccessful attempts |

### Errors for POST `/otp`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
| 400 | 2001 | invalid_param | The parameter 'phoneNumber' is empty or not set |  
| 400 | 2002 | invalid_param | The parameter 'countryIso' is empty or not set |  
| 400 | 2003 | invalid_param | Country ISO provided is invalid |  
| 400 | 2004 | invalid_param | The parameter 'from' is empty or not set |  
| 400 | 2005 | invalid_param | The parameter 'from' is not valid (min 3, max 15 characters) |  
| 400 | 2006 | invalid_param | The parameter 'template' is empty or not set |  
| 400 | 2006 | invalid_param | The parameter 'template' does not contain placeholder {{pin}} |  
| 400 | 2007 | invalid_param | The parameter 'ttl' is not a number |  
| 400 | 2008 | invalid_param | Min value for 'ttl' is 60 seconds |  
| 400 | 2009 | invalid_param | Max value for 'ttl' is 1800 seconds (30 mins) |  
| 400 | 2010 | invalid_param | The parameter 'maxAttempts' is not a number |  
| 400 | 2011 | invalid_param | Min value for 'maxAttempts' is 1 |  
| 400 | 2012 | invalid_param | Max value for 'maxAttempts' is 10 |  
| 400 | 2013 | invalid_param | The parameter 'pinType' is empty or not set |  
| 400 | 2014 | invalid_param | Invalid parameter 'pinType'. Must be one of: letters, numbers, alphanumeric |  
| 400 | 2015 | invalid_param | The parameter 'pinLength' is not a number |  
| 400 | 2016 | invalid_param | Min value for 'pinLength' is 4 |  
| 400 | 2017 | invalid_param | Max value for 'pinLength' is 10 |  
| 400 | 2018 | invalid_param | Track ID provided (parameter 'trackId') is not a valid UUID (v1-v5) |  
| 400 | 2019 | invalid_param | The parameter 'otpCallbackUrl' is not a valid URL |  
| 400 | 2020 | invalid_param | The phone number provided is invalid |  

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import otp_api
from smscx_client.model.new_otp_request import NewOtpRequest

from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = otp_api.OtpApi(
    smscx_client.ApiClient(configuration)
)    
new_otp_request = NewOtpRequest(
        phone_number="+336122464xx",
        country_iso="FR",
        _from="InfoText",
        template="Your verification code is {{pin}}",
        track_id="bf325375-e030-fccb-a009-17317c574773",
        ttl=180,
        max_attempts=4,
        pin_type="numbers",
        pin_length=4,
        otp_callback_url="https://webhook/receive-otp-status-updates",
    )

try:
    # New OTP
    api_response = api_instance.new_otp(new_otp_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OtpApi->new_otp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_otp_request** | [**NewOtpRequest**](../model/NewOtpRequest.md)|  |

### Return type

[**NewOtpResponse**](../model/NewOtpResponse.md)

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

# **verify_otp()**
> VerifyPinResponse verify_otp(otp_id, verify_pin_request)

Verify OTP

Verify the OTP received on the phone number.    
### Errors for POST `/otp/{otpId}`  
| HTTP code  | Error code  | Type  | Description  |  
|:------------:|:------------:|:------------:| ------------ |  
| 404 | 2021 | not_found | Otp ID not found |  
| 400 | 2022 | invalid_param | The parameter pin is empty or not set |  
| 400 | 2023 | otp_verified | The OTP was already verified |  
| 400 | 2024 | otp_cancelled | The OTP was canceled |  
| 400 | 2025 | otp_expired | The OTP has expired |  
| 400 | 2026 | otp_failed | The OTP has failed, maximum attempts reached |  
| 400 | 2027 | otp_failed | Max attempts reached |  
| 400 | 2028 | otp_expired | The PIN has expired |  
| 400 | 2029 | invalid_pin | The PIN provided does not verify |

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import time
import smscx_client
from smscx_client.api import otp_api
from smscx_client.model.verify_pin_request import VerifyPinRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = otp_api.OtpApi(
    smscx_client.ApiClient(configuration)
)    
otp_id = "a17fb13d-f4ac-4d93-9439-ef41ab8de390"
pin = "1544"

try:
    # Verify OTP
    api_response = api_instance.verify_otp(otp_id, pin)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OtpApi->verify_otp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otp_id** | **str**| Identifier of the OTP request | required
 **pin** | **str** | PIN code to be verified | required

### Return type

[**VerifyPinResponse**](../model/VerifyPinResponse.md)

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

