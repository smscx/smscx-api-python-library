import time
import smscx_client
from smscx_client.api import numbers_api
from smscx_client.model.rent_number_request import RentNumberRequest
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
rent_number_request = RentNumberRequest(
        number_id="bf325375-e030-fccb-a009-17317c574773",
        rent_period=1,
        auto_renew=False,
        callback_url="https://webhook/receive-inbound-sms/",
    )

try:
    # Rent phone number
    api_response = api_instance.rent_number(rent_number_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling NumbersApi->rent_number: %s\n" % e)