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
campaign_id = "4baf0298-0c21-4df1-a60a-6e3476e95e0b" # str | Identifier of a sent campaign
short_response = False # bool | If set to true, it will return the full `info` object and an empty `data` object (optional) if omitted the server will use the default value of False
limit = 100 # int | A limit on the number of objects to be returned (optional) if omitted the server will use the default value of 500
next = "NTM2NTA" # str | The next token used to retrieve additional data (optional)
previous = "NTQxNTA" # str | The previous token used to retrieve additional data (optional)

try:
    # Get campaign report
    api_response = api_instance.get_campaign_report(campaign_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->get_campaign_report: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get campaign report
    api_response = api_instance.get_campaign_report(campaign_id, short_response=short_response, limit=limit, next=next, previous=previous)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->get_campaign_report: %s\n" % e)