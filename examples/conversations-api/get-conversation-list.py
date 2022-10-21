import time
import smscx_client
from smscx_client.api import conversations_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = conversations_api.ConversationsApi(
    smscx_client.ApiClient(configuration)
)    

try:
    # Get conversations list
    api_response = api_instance.get_converstions_list()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ConversationsApi->get_converstions_list: %s\n" % e)