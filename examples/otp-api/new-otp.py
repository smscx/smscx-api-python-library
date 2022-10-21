import time
import smscx_client
from smscx_client.api import otp_api
from smscx_client.model.new_otp_request import NewOtpRequest

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
new_otp_request = NewOtpRequest(
        phone_number="+336122464xx",
        country_iso="FR",
        _from="InfoText",
        template="Your verification code is {{pin}}",
        track_id="bf325375-e030-fccb-a009-17317c574773",
        ttl=180,
        max_attempts=4,
        pin_type="numbers",
        pin_length=4,
        otp_callback_url="https://webhook/receive-otp-status-updates",
    )

try:
    # New OTP
    api_response = api_instance.new_otp(new_otp_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OtpApi->new_otp: %s\n" % e)