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