import time
import smscx_client
from smscx_client.api import conversations_api
from smscx_client.model.conversation_reply_sms_request import ConversationReplySmsRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = conversations_api.ConversationsApi(
    smscx_client.ApiClient(configuration)
)    
conversation_id = "c38fa60d-ce8f-4918-8b9d-d991bc44cb73" 
conversation_reply_sms_request = ConversationReplySmsRequest(
        text="text_example",
    )

try:
    # Send conversation reply via SMS
    api_response = api_instance.send_conversation_reply_sms(conversation_id, conversation_reply_sms_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ConversationsApi->send_conversation_reply_sms: %s\n" % e)