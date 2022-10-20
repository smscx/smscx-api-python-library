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

# Identifier of the attachment
attachment_id = "KgTX" 

try:
    # Export attachment hits to XLSX
    api_response = api_instance.export_attachment_hits_to_xlsx(attachment_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling AttachmentsApi->export_attachment_hits_to_xlsx: %s\n" % e)