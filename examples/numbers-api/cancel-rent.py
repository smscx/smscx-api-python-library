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