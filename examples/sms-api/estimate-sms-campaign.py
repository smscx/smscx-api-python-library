import time
import smscx_client
from smscx_client.api import sms_api
from smscx_client.model.send_sms_campaign_request_estimate import SendSmsCampaignRequestEstimate
from smscx_client.model.transliteration import Transliteration

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
send_sms_campaign_request_estimate = SendSmsCampaignRequestEstimate(
        groups=[
            1,
        ],
        _from="InfoText",
        text="This is example test {{optoutLink}}",
        #scheduled_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        #is_utc=True,
        dlr_callback_url="https://webhook/receive-sms-delivery-reports",
        #short_response=False,
        #no_text_details=False,
        #show_timezone=False,
        transliteration=Transliteration(
            alphabet="NON_GSM", # Will remove non-gsm characters
            remove_emojis=True,
        ),
    ) # SendSmsCampaignRequestEstimate | 

try:
    # Estimate SMS campaign
    api_response = api_instance.estimate_sms_campaign(send_sms_campaign_request_estimate)
    pprint(api_response)
except smscx_client.NoCoverageException as e:
    print("No coverage for this destination")
    # Your code for no coverage
except smscx_client.InvalidRequestException as e:
    print("Invalid request")
    # Your code for invalid request
except smscx_client.InvalidPhoneNumberException as e:
    print("Invalid phone number")
    # Your code for invalid phone number
except smscx_client.InsufficientBalanceException as e:
    print("Insufficient balance")
    # Your code for insufficient balance    
except smscx_client.ApiException as e:
    print("Exception when calling SmsApi->estimate_sms_campaign: %s\n" % e)