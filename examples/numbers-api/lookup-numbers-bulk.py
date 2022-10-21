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
            "+33612246444",
        ],
        #country_iso="FR",
        lookup_callback_url="https://my-webhook/endpoint",
    )

try:
    # Lookup numbers in bulk
    api_response = api_instance.lookup_numbers(numbers_lookup_request)
    pprint(api_response)
except smscx_client.InvalidPhoneNumberException as e:
    print("Invalid Phone number")
    # Your code for invalid phone number      
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->lookup_numbers: %s\n" % e)