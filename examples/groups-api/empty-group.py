import time
import smscx_client
from smscx_client.api import groups_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = groups_api.GroupsApi(
    smscx_client.ApiClient(configuration)
)    
group_id = 2245 # int | Identifier of a group of contacts

try:
    # Empty group
    api_response = api_instance.empty_group(group_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling GroupsApi->empty_group: %s\n" % e)