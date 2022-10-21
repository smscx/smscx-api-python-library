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
conversation_id = "c38fa60d-ce8f-4918-8b9d-d991bc44cb73" 

try:
    # Mark conversation as read
    api_response = api_instance.mark_conversation_as_read(conversation_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ConversationsApi->mark_conversation_as_read: %s\n" % e)