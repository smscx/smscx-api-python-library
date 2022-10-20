import time
import smscx_client
from smscx_client.api import reports_api
from smscx_client.model.report_single_response import ReportSingleResponse
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
msg_id = "9eeed792-9c8c-463c-a8e2-43ebf4494c02"

try:
    # Get report for single SMS or Viber or Whatsapp or Multichannel
    api_response = api_instance.get_single_report(msg_id)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->get_single_report: %s\n" % e)