import time
import smscx_client
from smscx_client.api import optouts_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = optouts_api.OptoutsApi(
    smscx_client.ApiClient(configuration)
)    
optout_id = 458

try:
    # Delete contact from optouts list
    api_response = api_instance.delete_contact_from_optouts_list(optout_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OptoutsApi->delete_contact_from_optouts_list: %s\n" % e)