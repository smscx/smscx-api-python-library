import time
import smscx_client
from smscx_client.api import viber_api
from smscx_client.model.send_viber_message_request import SendViberMessageRequest
from smscx_client.model.model403_no_coverage import Model403NoCoverage
from smscx_client.model.model400_invalid_param import Model400InvalidParam
from smscx_client.model.model500_server_error import Model500ServerError
from smscx_client.model.model401_unauthorized import Model401Unauthorized
from smscx_client.model.send_viber_message_response import SendViberMessageResponse
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
send_viber_message_request = SendViberMessageRequest(
        to=[
            "+4474006003xx",
            "+417813350xx",
            "+3584129058xx",
            "+3931238638xx",
            "+316122393xx",
            "+3519121547xx",
            "+336125151xx",
            "+791236471xx",
            "+3069121512xx",
        ],
        _from="InfoText",
        template_id=2561,
        #scheduled_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        #is_utc=True,
        dlr_callback_url="https://webhook/receive-delivery-reports",
        track_data="bf325375-e030-fccb-a009-17317c574773",
        #short_response=False,
        #no_text_details=False,
        #show_timezone=False,
        idempotency_id="bf325375-e030-fccb-a009-17317c574773",
    )

try:
    # Send Viber message
    api_response = api_instance.send_viber_message(send_viber_message_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ViberApi->send_viber_message: %s\n" % e)