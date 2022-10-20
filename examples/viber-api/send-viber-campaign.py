import time
import smscx_client
from smscx_client.api import viber_api
from smscx_client.model.send_viber_campaign_request import SendViberCampaignRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = viber_api.ViberApi(
    smscx_client.ApiClient(configuration)
)    
send_viber_campaign_request = SendViberCampaignRequest(
        groups=[
            631, 
            781,
        ],
        _from="InfoText",
        template_id=187,
        #scheduled_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        #is_utc=True,
        dlr_callback_url="https://webhook/receive-delivery-reports",
        #short_response=False,
        #no_text_details=False,
        #show_timezone=False,
        idempotency_id="bf325375-e030-fccb-a009-17317c574773",
    ) # SendViberCampaignRequest | 

try:
    # Send Viber campaign
    api_response = api_instance.send_viber_campaign(send_viber_campaign_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ViberApi->send_viber_campaign: %s\n" % e)