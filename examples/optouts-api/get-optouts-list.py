import time
import smscx_client
from smscx_client.api import optouts_api
from pprint import pprint

configuration = smscx_client.Configuration(
   # Use authentication via API Key
   api_key = "YOUR_API_KEY",

   # Uncomment to use authentication via Access Token
   # access_token = "YOUR_ACCESS_TOKEN",
)

# Create an instance of the API class
api_instance = optouts_api.OptoutsApi(
    smscx_client.ApiClient(configuration)
)    
limit = 100 # int | A limit on the number of objects to be returned (optional) if omitted the server will use the default value of 500
next = "NTM2NTA" # str | The next token used to retrieve additional data (optional)
previous = "NTQxNTA" # str | The previous token used to retrieve additional data (optional)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get optouts list
    api_response = api_instance.get_optouts_list(limit=limit, next=next, previous=previous)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OptoutsApi->get_optouts_list: %s\n" % e)