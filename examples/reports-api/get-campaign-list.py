import time
import smscx_client
from smscx_client.api import reports_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = reports_api.ReportsApi(
    smscx_client.ApiClient(configuration)
)    
delivery_reports = True # bool | The response will contain an object **data.status** with delivery report summary for each campaign (optional) if omitted the server will use the default value of False
source = "api" # str | Source of the sent messages (optional)
limit = 100 # int | A limit on the number of objects to be returned (optional) if omitted the server will use the default value of 500
next = "NTM2NTA" # str | The next token used to retrieve additional data (optional)
previous = "NTQxNTA" # str | The previous token used to retrieve additional data (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get list of sent campaigns
    api_response = api_instance.get_campaigns_list(delivery_reports=delivery_reports, source=source, limit=limit, next=next, previous=previous)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->get_campaigns_list: %s\n" % e)