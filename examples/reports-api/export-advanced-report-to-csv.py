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
period = "2021-07" # str | Period for the requested report in format **Y-M** or **Y**
start_date = "2021-03-01" # str | The start date of the report in format Y-M-D
end_date = "2021-04-30" # str | The end date of the report in format Y-M-D
channel = "sms" # str | Channel of the sent messages (optional)
source = "api" # str | Source of the sent messages (optional)
delivery_report = "delivered" # str |  (optional)
country_iso = "fr" # str | Two-letter country code defined in ISO-3166 alpha 2 standard (case insensitive) (optional)
limit = 100 # int | A limit on the number of objects to be returned (optional) if omitted the server will use the default value of 500

try:
    # Export advanced report to CSV
    api_response = api_instance.export_advanced_report_to_csv(period, start_date, end_date)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->export_advanced_report_to_csv: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Export advanced report to CSV
    api_response = api_instance.export_advanced_report_to_csv(period, start_date, end_date, channel=channel, source=source, delivery_report=delivery_report, country_iso=country_iso, limit=limit)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling ReportsApi->export_advanced_report_to_csv: %s\n" % e)