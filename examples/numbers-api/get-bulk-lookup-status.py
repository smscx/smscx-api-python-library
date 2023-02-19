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
limit = 100 # int | A limit on the number of objects to be returned (optional) if omitted the server will use the default value of 500
next = None # str | The next token used to retrieve additional data (optional)
previous = None # str | The previous token used to retrieve additional data (optional)

# example passing only required values which don't have defaults set
try:
    # Get Bulk Lookup result
    api_response = api_instance.get_bulk_lookup_status(lookup_bulk_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->get_bulk_lookup_status: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get Bulk Lookup result
    api_response = api_instance.get_bulk_lookup_status(lookup_bulk_id, limit=limit, next=next, previous=previous)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->get_bulk_lookup_status: %s\n" % e)