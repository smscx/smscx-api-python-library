import time
import smscx_client
from smscx_client.api import templates_api
from smscx_client.model.templates_update_response import TemplatesUpdateResponse
from smscx_client.model.templates_update_request import TemplatesUpdateRequest
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = templates_api.TemplatesApi(
    smscx_client.ApiClient(configuration)
)    
template_id = 39774 # int | Identifier of the template
templates_update_request = TemplatesUpdateRequest(
        name="My edited template name",
        text="My edited template text",
        channel="sms",
    )

try:
    # Update template
    api_response = api_instance.update_template(template_id, templates_update_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling TemplatesApi->update_template: %s\n" % e)