import time
import smscx_client
from smscx_client.api import whatsapp_api
from smscx_client.model.send_whatsapp_message_request import SendWhatsappMessageRequest
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
send_whatsapp_message_request = SendWhatsappMessageRequest(
        to=[
            "+359485721xx",
        ],
        _from="InfoText",
        template_id=261,
        #scheduled_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        #is_utc=True,
        dlr_callback_url="https://webhook/receive-delivery-reports",
        track_data="bf325375-e030-fccb-a009-17317c574773",
        #short_response=False,
        #no_text_details=False,
        #show_timezone=False,
    )

try:
    # Send Whatsapp message
    api_response = api_instance.send_whatsapp_message(send_whatsapp_message_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling WhatsappApi->send_whatsapp_message: %s\n" % e)