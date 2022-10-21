import time
import smscx_client
from smscx_client.api import groups_api
from smscx_client.model.update_number_request import UpdateNumberRequest
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
phone_number_id = "68aa4d9f-ee25-4a32-95d0-7272efe3b238" # str | Identifier of the phone number
update_number_request = UpdateNumberRequest(
        phone_number="phone_number_example",
        first_name="first_name_example",
        last_name="last_name_example",
        email="email_example",
        field1="field1_example",
        field2="field2_example",
        field3="field3_example",
        field4="field4_example",
        field5="field5_example",
        custom_fields=CustomFieldsObj(
            custom_field_name={
                "key": "key_example",
            },
        ),
    ) # UpdateNumberRequest | 

try:
    # Update contact from group
    api_response = api_instance.update_contact_from_group(group_id, phone_number_id, update_number_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling GroupsApi->update_contact_from_group: %s\n" % e)