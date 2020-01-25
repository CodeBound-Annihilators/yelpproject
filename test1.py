import requests
import get_my_key
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize


Client_ID = '8686c761d3182d6d8499bf7ef711556921f22a2b'
api_key = get_my_key.api_key()
endpoint = 'https://api.yelp.com/v3/businesses/search'
headers = {'Authorization' : 'Bearer %s' % api_key}

def search_restaurants(set_num): 
# This function launches the request for all restaurants in San Antonio, Tx.

    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {
        'Authorization': 'Bearer %s'% api_key,
    }
    url_params = { #parameters passed to the API
    "location":"San Antonio",
    "state": "Texas",
    'offset': offset_num, # We are going to iterate the offset
     "limit":50 # Maximum return of results per request (ref: API documentation).
     }

    response = requests.get(url, headers=headers, params=url_params)
    return response.json() # Returns a JSON.


if __name__ == "__main__":
    for offset_num in np.arange(0,3200,50) : 
# Desire 3200 results, in steps of 50 results per request.
        try:
            output_json = search_restaurants(offset_num) # Executing the function defined above.
            print(offset_num) # Making sure each offset iteration is running
            print(output_json) # If you wanna check the JSON for each iteration
            if offset_num == 50:
                df_first = pd.DataFrame.from_dict(output_json['businesses'])
# 'businesses' because that's the primary key of the JSON (i.e. pull all attribute data by calling 
# that one key). This is something you can figure out reading the API documentation or visually
# parsing the JSON. 
            else:
                df2 = pd.DataFrame.from_dict(output_json['businesses'])
                df_first = df_first.append(df2)
# The conditional statement above is so that I can append my results into a single dataframe, to 
# save into a single csv document.
        except AttributeError:
            print("error at ", offset_num) # Helpful for debugging purposes
            
    df_first.to_csv("yelp_data/output_data.csv", index = False)