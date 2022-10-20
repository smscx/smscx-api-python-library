import time
import smscx_client
from smscx_client.api import shortlinks_api
from smscx_client.model.shortlink_new_request import ShortlinkNewRequest
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
shortlink_new_request = ShortlinkNewRequest(
        name="My new shortlink",
        url="https://this-is-my-long-link/this-is-a-long-path",
    )

try:
    # Create shortlink
    api_response = api_instance.create_shortlink(shortlink_new_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ShortlinksApi->create_shortlink: %s\n" % e)