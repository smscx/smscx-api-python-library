import time
import smscx_client
from smscx_client.api import multichannel_api
from smscx_client.model.send_multichannel_campaign_request import SendMultichannelCampaignRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = multichannel_api.MultichannelApi(
    smscx_client.ApiClient(configuration)
)    
send_multichannel_campaign_request = SendMultichannelCampaignRequest(
        groups=[
            1,
        ],
        _from="_from_example",
        strategy=[
            Strategy(
                channel="viber",
                template_id=1,
                text="text_example",
            ),
        ],
        ttl=300,
        scheduled_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        is_utc=True,
        dlr_callback_url="https://my-callback-url/endpoint",
        short_response=False,
        no_text_details=False,
        show_timezone=False,
        idempotency_id="bf325375-e030-fccb-a009-17317c574773",
    )

try:
    # Send Multichannel campaign
    api_response = api_instance.send_multichannel_campaign(send_multichannel_campaign_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling MultichannelApi->send_multichannel_campaign: %s\n" % e)