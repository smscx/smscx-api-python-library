import time
import smscx_client
from smscx_client.api import shortlinks_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = shortlinks_api.ShortlinksApi(
    smscx_client.ApiClient(configuration)
)    
short_id = "KgTX"

try:
    # Export shortlink hits to CSV
    api_response = api_instance.export_shortlink_hits_to_csv(short_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ShortlinksApi->export_shortlink_hits_to_csv: %s\n" % e)