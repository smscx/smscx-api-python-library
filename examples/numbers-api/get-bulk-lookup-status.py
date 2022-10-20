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
    # Get Bulk Lookup result
    api_response = api_instance.get_bulk_lookup_status(lookup_bulk_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->get_bulk_lookup_status: %s\n" % e)