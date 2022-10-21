import time
import smscx_client
from smscx_client.api import account_api
from smscx_client.model.channels_status import ChannelsStatus

from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = account_api.AccountApi(
    smscx_client.ApiClient(configuration)
)    

try:
    # Get status of all channels
    api_response = api_instance.get_channels_status()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling AccountApi->get_channels_status: %s\n" % e)