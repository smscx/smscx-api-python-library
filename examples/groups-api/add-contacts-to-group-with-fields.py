import time
import smscx_client
from smscx_client.api import groups_api
from smscx_client.model.add_contacts_to_group_with_fields_request import AddContactsToGroupWithFieldsRequest
from smscx_client.model.group_add import GroupAdd
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
group_id = 1
add_contacts_to_group_request = AddContactsToGroupWithFieldsRequest(
    phone_numbers=[GroupAdd(
            phone_number="+336125151xx",
            first_name="John",
            last_name="Doe",
            email="john@doe.com",
            field1="field1_example",
            field2="field2_example",
            field3="field3_example",
            field4="field4_example",
            field5="field5_example",
        ),GroupAdd(
            phone_number="+336128298xx",
            first_name="Alain",
            last_name="Maurice",
            email="alain@maurice.com",
            field1="field1_example",
            field2="field2_example",
            field3="field3_example",
            field4="field4_example",
            field5="field5_example",
        ),
    ],
    allow_invalid=True
) 

try:
    # Add contacts to group
    api_response = api_instance.add_contacts_to_group_with_fields(group_id, add_contacts_to_group_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling GroupsApi->add_contacts_to_group: %s\n" % e)    