## ISS API Example Project
# [Source](https://wheretheiss.at/w/developer)

# Authentication
Currently there is no authentication required for accessing this API but there are rate limits

# Rate Limits
One request per second. It can be tracked through the X-Rate-Limit headers returned in the response

# Response Formats
All responses are in json by default. I've added an option to return a reponse in a dataframe. 

# Optional paramters from the source
* suppress_response_codes=true to supress non-2XX responses
* indent=4 - indent responses with 4 spaces
