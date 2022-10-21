import time
import smscx_client
from smscx_client.api import viber_api
from smscx_client.model.send_viber_campaign_request_estimate import SendViberCampaignRequestEstimate
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
send_viber_campaign_request_estimate = SendViberCampaignRequestEstimate(
        groups=[
            1321,
        ],
        _from="InfoText",
        template_id=187,
        #scheduled_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        #is_utc=True,
        dlr_callback_url="https://webhook/receive-delivery-reports",
        #short_response=False,
        #no_text_details=False,
        #show_timezone=False,
    ) 

try:
    # Estimate Viber campaign
    api_response = api_instance.estimate_viber_campaign(send_viber_campaign_request_estimate)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ViberApi->estimate_viber_campaign: %s\n" % e)