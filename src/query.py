import pandas as pd
from sodapy import Socrata

from credentials import APP_TOKEN

# DOT City IDs
city_IDs = {
    "Seattle": 30559,
    "Everett": 34004,
    "LA Metro": 32575 # (includes SNA, LGB, LAX, BUR, ONT)
}

# DOT Airport IDs
airport_IDs = {
    "SEA": 14747,
    "PAE": 14004,
    "SNA": 14908,
    "LAX": 12892,
    "LGB": 12954,
    "BUR": 10800,
    "ONT": 13891
}

# Dataset identifier for querying DOT
TABLE1_DATASET_ID = "4f3n-jbg2"

# Client for querying DOT
client = Socrata("data.transportation.gov", APP_TOKEN)

# Capture all flight data between two cities as an ordered pair and return as df (helper function)
def run_city_pair_query(city1, city2, limit=500, dataset_id = TABLE1_DATASET_ID):
    # Try with city1 then city2
    results = client.get(TABLE1_DATASET_ID,
                         limit=limit,
                         citymarketid_1=city1,
                         citymarketid_2=city2)
    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)
    return results_df

# Capture all flight data between two cities as an unordered pair and return as df (best for usage)
def fetch_city_pair_data(city1, city2, limit=500, dataset_id = TABLE1_DATASET_ID):
    # Try with city1 then city2
    results_df = run_city_pair_query(city1, city2, limit, dataset_id)

    # If city pairs are backwards, switch as parameters (DOT only has one entry per pair)
    if results_df.shape[0] > 1:
        return results_df
    else:
        results_df = run_city_pair_query(city2, city1, limit, dataset_id)
        return results_df


# Capture all flights between LA Metro airports and Seattle (DOT data is bidirectional)
la_seattle_data = fetch_city_pair_data(city_IDs["Seattle"], city_IDs["LA Metro"], limit=100)