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
campaign_id = "9f90f919-9b19-43db-921f-c8e05ae7054c"

try:
    # Delete scheduled Multichannel campaign
    api_response = api_instance.delete_scheduled_multichannel_campaign(campaign_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling MultichannelApi->delete_scheduled_multichannel_campaign: %s\n" % e)