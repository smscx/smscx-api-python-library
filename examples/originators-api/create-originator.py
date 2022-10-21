import time
import smscx_client
from smscx_client.api import originators_api
from smscx_client.model.originator_new_request import OriginatorNewRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = originators_api.OriginatorsApi(
    smscx_client.ApiClient(configuration)
)    
originator_new_request = OriginatorNewRequest(
        originator="MyCompany",
    ) 

try:
    # Create new originator
    api_response = api_instance.create_originator(originator_new_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OriginatorsApi->create_originator: %s\n" % e)