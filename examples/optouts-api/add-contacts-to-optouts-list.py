import time
import smscx_client
from smscx_client.api import optouts_api
from smscx_client.model.add_contacts_to_group_request import AddContactsToGroupRequest
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
add_contacts_to_optouts_request = AddContactsToGroupRequest(
        phone_numbers=[
            "+436645185xx",
            "+791234076xx",
        ],
        allow_invalid=False,
        country_iso="FR",
    )

try:
    # Add contact to optouts list
    api_response = api_instance.add_contact_to_optouts_list(add_contacts_to_optouts_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OptoutsApi->add_contact_to_optouts_list: %s\n" % e)