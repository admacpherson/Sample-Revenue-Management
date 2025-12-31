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
DOT_DATASET_ID = "4f3n-jbg2"

# Client for querying DOT
client = Socrata("data.transportation.gov", APP_TOKEN)

# Capture all flights between LA Metro airports and Seattle (DOT data is bidirectional)
results = client.get(DOT_DATASET_ID,
                         limit=100,
                         citymarketid_1=city_IDs["LA Metro"],
                         citymarketid_2=city_IDs["Seattle"])

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

print(results_df)