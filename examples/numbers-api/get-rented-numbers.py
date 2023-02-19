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

features = 3 # int | Filter by number features (1 - receive SMS, 2 - send SMS, 1 + 2 = 3 - send and receive SMS) (optional)
country_iso = "fr" # str | Filter by country iso. Two-letter country code defined in ISO-3166 alpha 2 standard (case insensitive) (optional)
number_type = "mobile" # str | Filter by type of phone number (optional)
active_rent = True # bool | Filter by active rent (optional)
inbound_sms_sender = True # bool | Filter numbers that support inbound SMS from alphanumeric sender ID (optional)
include = "4559" # str | Filter phone numbers that include the following digits (optional)
exclude = "1554" # str | Filter phone numbers that exclude the following digits (optional)


try:
    # Get list of your rented numbers
    api_response = api_instance.get_rented_numbers()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->get_rented_numbers: %s\n" % e)


try:
    # Get list of your rented numbers
    api_response = api_instance.get_rented_numbers(features=features, country_iso=country_iso, number_type=number_type, active_rent=active_rent, inbound_sms_sender=inbound_sms_sender, include=include, exclude=exclude)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->get_rented_numbers: %s\n" % e)