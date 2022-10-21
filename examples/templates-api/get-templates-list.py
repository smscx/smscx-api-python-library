import time
import smscx_client
from smscx_client.api import templates_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = templates_api.TemplatesApi(
    smscx_client.ApiClient(configuration)
)    

try:
    # Get templates list
    api_response = api_instance.get_templates_list()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling TemplatesApi->get_templates_list: %s\n" % e)