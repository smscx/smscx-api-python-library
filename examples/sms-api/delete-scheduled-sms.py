import time
import smscx_client
from smscx_client.api import sms_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = sms_api.SmsApi(
    smscx_client.ApiClient(configuration)
)    

# Identifier of a scheduled message
msg_id = "3328fe13-2b99-4282-b62e-d891f5e452a8" 

try:
    # Delete scheduled SMS
    api_response = api_instance.delete_scheduled_sms(msg_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling SmsApi->delete_scheduled_sms: %s\n" % e)