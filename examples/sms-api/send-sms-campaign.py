import time
import smscx_client
from smscx_client.api import sms_api
from smscx_client.model.model403_no_coverage import Model403NoCoverage
from smscx_client.model.send_sms_campaign_request import SendSmsCampaignRequest
from smscx_client.model.model400_invalid_param import Model400InvalidParam
from smscx_client.model.model500_server_error import Model500ServerError
from smscx_client.model.model401_unauthorized import Model401Unauthorized
from smscx_client.model.send_sms_campaign_response import SendSmsCampaignResponse
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
send_sms_campaign_request = SendSmsCampaignRequest(
        groups=[
            1,
        ],
        _from="_from_example",
        text="Hello {{firstName}} {{lastName}} This is example text {{optoutLink}}",
        #scheduled_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        #is_utc=True,
        dlr_callback_url="https://webhook/receive-sms-delivery-reports",
        #short_response=False,
        #no_text_details=False,
        #show_timezone=False,
        idempotency_id="bf325375-e030-fccb-a009-17317c574773",
        transliteration=Transliteration(
            alphabet="NONE",
            remove_emojis=False,
        ),
    ) # SendSmsCampaignRequest | 

try:
    # Send SMS campaign
    api_response = api_instance.send_sms_campaign(send_sms_campaign_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling SmsApi->send_sms_campaign: %s\n" % e)