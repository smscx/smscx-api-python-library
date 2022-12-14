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
phone_number = "+33612246450"

try:
    # Lookup number
    api_response = api_instance.lookup_number(phone_number)
    pprint(api_response)
except smscx_client.InvalidPhoneNumberException as e:
    print("Invalid Phone number")
    # Your code for invalid phone number      
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->lookup_number: %s\n" % e)