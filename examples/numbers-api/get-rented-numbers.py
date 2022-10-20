import time
import smscx_client
from smscx_client.api import numbers_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = numbers_api.NumbersApi(
    smscx_client.ApiClient(configuration)
)    

try:
    # Get list of your rented numbers
    api_response = api_instance.get_rented_numbers()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->get_rented_numbers: %s\n" % e)