import time
import smscx_client
from smscx_client.api import originators_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = originators_api.OriginatorsApi(
    smscx_client.ApiClient(configuration)
)    
originator_id = 1388

try:
    # Delete originator
    api_response = api_instance.delete_originator(originator_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OriginatorsApi->delete_originator: %s\n" % e)