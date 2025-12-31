import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_scraper_df():
    # Get data from DOT site
    URL = "https://www.transtats.bts.gov/AverageFare/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    # Identify main table
    results = soup.find("table", class_ = "dataTD3")

    # Get table headers
    headers = results.find_all('th')
    header_array = []
    for row in headers:
        header_array.append(row.text)

    # Parse table into 2D array
    data = []

    rows = results.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values

    # Remove empty first list from data
    data.pop(0)

    # Convert to data frame with headers and export to csv
    df = pd.DataFrame(data)
    df.columns = header_array

    return df