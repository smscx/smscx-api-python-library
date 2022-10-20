import time
import smscx_client
from smscx_client.api import viber_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = viber_api.ViberApi(
    smscx_client.ApiClient(configuration)
)    

# Identifier of a scheduled Viber campaign
campaign_id = "cbb72a72-0dfa-4288-b3d0-05fab904f0b2" 

try:
    # Delete scheduled Viber campaign
    api_response = api_instance.delete_scheduled_viber_campaign(campaign_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ViberApi->delete_scheduled_viber_campaign: %s\n" % e)