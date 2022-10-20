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
campaign_id = "4baf0298-0c21-4df1-a60a-6e3476e95e0b"

try:
    # Export campaign report to CSV
    api_response = api_instance.export_campaign_report_to_csv(campaign_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->export_campaign_report_to_csv: %s\n" % e)