from config.options import *
from data import airport_dicts
from src.scraper import get_scraper_df
from create_tables import *
from data.airport_dicts import *

market_all_airports = market_airports + market_coterms

def data_setup():
    if scraper_file == "":
        scraper_df = get_scraper_df()
        export_csv(scraper_df, "table", header_bool=True)

def get_city_IDs():
    market_city_IDs = []

    for IATA_code in market_airports:
        for i in range(len(airports_list)):
            if IATA_code == airports_list[i]["IATA Code"]:
                market_city_IDs.append(airports_list[i]["City ID"])

    return market_city_IDs

def __main__():
    #data_setup()
    get_city_IDs()

if __name__ == "__main__":
    __main__()