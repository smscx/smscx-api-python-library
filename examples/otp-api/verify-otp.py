import time
import smscx_client
from smscx_client.api import otp_api
from smscx_client.model.verify_pin_request import VerifyPinRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = otp_api.OtpApi(
    smscx_client.ApiClient(configuration)
)    
otp_id = "a17fb13d-f4ac-4d93-9439-ef41ab8de390"
pin = "1544"

try:
    # Verify OTP
    api_response = api_instance.verify_otp(otp_id, pin)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OtpApi->verify_otp: %s\n" % e)