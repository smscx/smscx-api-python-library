import time
import smscx_client
from smscx_client.api import whatsapp_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = whatsapp_api.WhatsappApi(
    smscx_client.ApiClient(configuration)
)    

# Identifier of a scheduled Whatsapp message
msg_id = "3328fe13-2b99-4282-b62e-d891f5e452a8" 

try:
    # Delete scheduled Whatsapp message
    api_response = api_instance.delete_scheduled_whatsapp_message(msg_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling WhatsappApi->delete_scheduled_whatsapp_message: %s\n" % e)