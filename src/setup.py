import config.options as options
from src.query import fetch_city_pair_data
from src.scraper import get_scraper_df
from src.create_tables import *
from data.airport_dicts import *

market_all_airports = options.market_airports + options.market_coterms


# Get data and update filepaths as necessary
def data_setup():
    # If no filepath specified, run the scraper, export to CSV, and update the filepath variable
    if options.scraper_filepath == "":
        scraper_df = get_scraper_df()
        options.scraper_filepath = export_csv(scraper_df, "table.csv", header_bool=True)

    # If no filepath specified, run the query, export to CSV, and update the filepath variable
    if options.query_filepath == "":
        markey_city_IDS = get_city_IDs(options.market_airports)
        city_pair_df = fetch_city_pair_data(markey_city_IDS[0], markey_city_IDS[1], limit=options.QUERY_LIMIT)
        options.query_filepath = export_csv(city_pair_df, "city_pair_data.csv", header_bool=True)


# Helper function to translate IATA codes to DOT City IDs (must be airport_dicts.py)
def get_city_IDs(airports):
    market_city_IDs = []

    for IATA_code in airports:
        for i in range(len(airports_list)):
            if IATA_code == airports_list[i]["IATA Code"]:
                market_city_IDs.append(airports_list[i]["City ID"])

    return market_city_IDs


def __main__():
    #data_setup()
    get_city_IDs(options.market_airports)


if __name__ == "__main__":
    __main__()