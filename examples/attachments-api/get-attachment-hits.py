import time
import smscx_client
from smscx_client.api import attachments_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = attachments_api.AttachmentsApi(
    smscx_client.ApiClient(configuration)
)    
attachment_id = "KgTX" # str | Identifier of the attachment
short_response = False # bool | If set to true, it will return the full `info` object and an empty `data` object (optional) if omitted the server will use the default value of False
limit = 100 # int | A limit on the number of objects to be returned (optional) if omitted the server will use the default value of 500
next = "NTM2NTA" # str | The next token used to retrieve additional data (optional)
previous = "NTQxNTA" # str | The previous token used to retrieve additional data (optional)

try:
    # Get attachment hits
    api_response = api_instance.get_attachment_hits(attachment_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling AttachmentsApi->get_attachment_hits: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get attachment hits
    api_response = api_instance.get_attachment_hits(attachment_id, short_response=short_response, limit=limit, next=next, previous=previous)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling AttachmentsApi->get_attachment_hits: %s\n" % e)