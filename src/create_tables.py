from scraper import get_scraper_df
from query import *

def export_csv(df, filename, index_bool=False, header_bool=False):
    filepath = "../data/" + filename + ".csv"
    df.to_csv(filepath, index=index_bool, header=header_bool)

scraper_df = get_scraper_df()

la_seattle_df = fetch_city_pair_data(
    city1=city_IDs["LA Metro"],
    city2=city_IDs["Seattle"],
    limit=500
)

export_csv(scraper_df, "table", header_bool=True)
export_csv(la_seattle_df, "la_to_seattle_t1", header_bool=True)