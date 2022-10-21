import time
import smscx_client
from smscx_client.api import groups_api
from smscx_client.model.new_group_request import NewGroupRequest
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
new_group_request = NewGroupRequest(
        name="name_example",
    )

try:
    # Create new group
    api_response = api_instance.create_group(new_group_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling GroupsApi->create_group: %s\n" % e)