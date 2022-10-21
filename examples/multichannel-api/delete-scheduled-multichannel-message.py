import time
import smscx_client
from smscx_client.api import multichannel_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = multichannel_api.MultichannelApi(
    smscx_client.ApiClient(configuration)
)    
msg_id = "396d2afa-1440-4f36-a365-b99a5ceaea23"

try:
    # Delete scheduled Multichannel message
    api_response = api_instance.delete_scheduled_multichannel_message(msg_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling MultichannelApi->delete_scheduled_multichannel_message: %s\n" % e)