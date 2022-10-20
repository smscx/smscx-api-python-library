import time
import smscx_client
from smscx_client.api import templates_api
from smscx_client.model.templates_new_request import TemplatesNewRequest
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
templates_new_request = TemplatesNewRequest(
        name="My text template",
        text="This is my text template {{optoutLink}}",
        channel="sms",
    )

try:
    # Create template
    api_response = api_instance.create_template(templates_new_request)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling TemplatesApi->create_template: %s\n" % e)