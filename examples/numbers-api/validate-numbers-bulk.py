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
            "phone_numbers_example",
        ],
        country_iso="country_iso_example",
    ) # NumbersValidateRequest | 

try:
    # Validate numbers in bulk
    api_response = api_instance.validate_numbers(numbers_validate_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->validate_numbers: %s\n" % e)