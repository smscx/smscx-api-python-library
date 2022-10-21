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
dimension = "source" # str | Dimension for wich the summary report is requested
period = "2021-07" # str | Period for the requested report in format **Y-M** or **Y**
start_date = "2021-03-01" # str | The start date of the report in format Y-M-D
end_date = "2021-04-30" # str | The end date of the report in format Y-M-D
limit = 100 # int | A limit on the number of objects to be returned (optional) if omitted the server will use the default value of 500

try:
    # Get summary reports for a dimension
    api_response = api_instance.get_summary_reports(dimension, period, start_date, end_date)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->get_summary_reports: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get summary reports for a dimension
    api_response = api_instance.get_summary_reports(dimension, period, start_date, end_date, limit=limit)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->get_summary_reports: %s\n" % e)