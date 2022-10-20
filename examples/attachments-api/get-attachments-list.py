import time
import smscx_client
from smscx_client.api import attachments_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = attachments_api.AttachmentsApi(
    smscx_client.ApiClient(configuration)
)    

try:
    # Get attachments list
    api_response = api_instance.get_attachments_list()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling AttachmentsApi->get_attachments_list: %s\n" % e)