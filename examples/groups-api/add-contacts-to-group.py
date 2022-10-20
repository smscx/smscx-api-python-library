import time
import smscx_client
from smscx_client.api import groups_api
from smscx_client.model.add_contacts_to_group_request import AddContactsToGroupRequest
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
group_id = 2245
add_contacts_to_group_request = AddContactsToGroupRequest(None) # AddContactsToGroupRequest | 

try:
    # Add contacts to group
    api_response = api_instance.add_contacts_to_group(group_id, add_contacts_to_group_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling GroupsApi->add_contacts_to_group: %s\n" % e)