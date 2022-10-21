import time
import smscx_client
from smscx_client.api import applications_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = applications_api.ApplicationsApi(
    smscx_client.ApiClient(configuration)
)    

try:
    # Get scopes
    api_response = api_instance.get_scopes()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ApplicationsApi->get_scopes: %s\n" % e)