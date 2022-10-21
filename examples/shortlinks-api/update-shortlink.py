import time
import smscx_client
from smscx_client.api import shortlinks_api
from smscx_client.model.shortlink_update_request import ShortlinkUpdateRequest
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
short_id = "KgTX" # str | Identifier of the shortlink
shortlink_update_request = ShortlinkUpdateRequest(
        name="name_example",
        url="url_example",
    )

try:
    # Update shortlink
    api_response = api_instance.update_shortlink(short_id, shortlink_update_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ShortlinksApi->update_shortlink: %s\n" % e)