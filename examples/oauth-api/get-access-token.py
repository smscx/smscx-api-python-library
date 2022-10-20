import time
import smscx_client
from smscx_client.api import oauth_api
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = smscx_client.Configuration(
    username = "YOUR_APPLICATION_ID",
    password = "YOUR_APPLICATION_SECRET"
)

# Create an instance of the API class
api_instance = oauth_api.OauthApi(
    smscx_client.ApiClient(configuration)
)    

# A list of space-delimited, case-sensitive strings. If left empty or ommited, the issued access token will be granted with all scopes (full privileges) (optional)
scope = "sms groups templates originators numbers reports templates shortlinks"

try:
    # Get access token
    api_response = api_instance.get_access_token()
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OauthApi->get_access_token: %s\n" % e)

# example passing only required values which don't have defaults set
# and optional values
try:
    # Get access token
    api_response = api_instance.get_access_token(scope=scope)
    pprint(api_response)
except smscx_client.ApiException as e:
    print("Exception when calling OauthApi->get_access_token: %s\n" % e)