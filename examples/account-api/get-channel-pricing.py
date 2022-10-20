import time
import smscx_client
from smscx_client.api import account_api
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
channel = "sms"
traffic_type = "transactional"

try:
    # Get channels pricing
    api_response = api_instance.get_channel_pricing(channel, traffic_type)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling AccountApi->get_channel_pricing: %s\n" % e)