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
country_iso = "FR" # str | 
features = 3 # int | Filter by number features (1 - receive SMS, 2 - send SMS, 1 + 2 = 3 - send and receive SMS) (optional)
number_type = "mobile" # str | Filter by type of phone number (optional)
setup_time = "instant" # str | Filter by time of setup (optional)
registration = True # bool | Filter by registration (optional)
inbound_sms_sender = True # bool | Filter numbers that support inbound SMS from alphanumeric sender ID (optional)
include = "4559" # str | Filter phone numbers that include the following digits (optional)
exclude = "1554" # str | Filter phone numbers that exclude the following digits (optional)

# example passing only required values which don't have defaults set
try:
    # Get available numbers for rent
    api_response = api_instance.get_available_numbers(country_iso)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->get_available_numbers: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get available numbers for rent
    api_response = api_instance.get_available_numbers(country_iso, features=features, number_type=number_type, setup_time=setup_time, registration=registration, inbound_sms_sender=inbound_sms_sender, include=include, exclude=exclude)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->get_available_numbers: %s\n" % e)