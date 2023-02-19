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