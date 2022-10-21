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
channel = "sms" # str | 
traffic_type = "transactional" # str | 
country_iso = "FR" # str | 

try:
    # Get pricing for channel by country iso
    api_response = api_instance.get_channel_pricing_by_country_iso(channel, traffic_type, country_iso)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling AccountApi->get_channel_pricing_by_country_iso: %s\n" % e)