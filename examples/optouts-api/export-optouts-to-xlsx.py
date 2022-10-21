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

try:
    # Export optouts to XLSX
    api_response = api_instance.export_optouts_to_xlsx()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OptoutsApi->export_optouts_to_xlsx: %s\n" % e)