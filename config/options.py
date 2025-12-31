# Define airports to select
market_airports = ["SEA", "SNA"]
market_coterms = ["LAX", "LGB", "BUR", "ONT"]

# Provide file paths for static data or leave blank to scrape BTS and/or DOT for most recent data
QUERY_LIMIT = 100
scraper_filepath = "../data/2025Q2.csv"
query_filepath = "../data/la_to_seattle_t1_static.csv"
