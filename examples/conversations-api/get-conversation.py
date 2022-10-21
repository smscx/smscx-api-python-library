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
    # Get conversation
    api_response = api_instance.get_conversation(conversation_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ConversationsApi->get_conversation: %s\n" % e)