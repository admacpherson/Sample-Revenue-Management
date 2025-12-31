# Sample-Revenue-Management
Simulating a revenue management case study based on publicly available data

## Features
<b>Data Pipeline</b>
- [x] BTS data scraper
- [x] Airfare Report endpoint access
- [ ] Conversion to static tables and dataframes

<b>Analysis</b>
- [ ] MRP market analysis
- [ ] Impact of (U)LCCs on market via Consumer Airfare Report T7

## Structure
* `data`
  * `scraper.py`: BeautifulSoup scraper that reads most current data from the [BTS website](https://www.transtats.bts.gov/AverageFare/) for Average Domestic Airline Itinerary Fares By Origin City and exports it to table.csv 
  * `table.csv`: CSV-formatted data from BTS
  * `2025Q2.csv`: Static table with 2025 Q2 data 
* `.gitignore`
* `README.md`

## Data
The United States Bureau of Transportation Statistics (BTS), a part of the Department of Transportation (DOT) maintains various data relating to air transport. This project uses the following:

### Average Domestic Airline Itinerary Fares By Origin City

A database of average domestic airline itinerary fares by origin and by year and quarter. Per the BTS:
> Average Fares are based on domestic itinerary fares. Itinerary fares consist of round-trip fares unless the customer does not purchase a return trip. In that case, the one-way fare is included. Fares are based on the total ticket value which consists of the price charged by the airlines plus any additional taxes and fees levied by an outside entity at the time of purchase. Fares include only the price paid at the time of the ticket purchase and do not include fees for optional services, such as baggage fees. Averages do not include frequent-flyer or “zero fares.” The inflation adjustment is calculated using dollars for the most recent year of air fare data.

<i>(Quote sourced from site update on November 17, 2025)</i>

The data are available in web format or for download. For the purposes of this project, I have constructed a scraper, implemented in BeautifulSoup, to automatically pull the most recent version of the table and save it to the repository as a CSV. For analysis, I have created a copy to provide a static version.



### Domestic Airline Consumer Airfare Report: Table 1 - Top 1,000 Contiguous State City-Pair Markets (Fares by City Pairings)
The DOT also publishes a report related to domestic airfare that contains several tables. This project uses Table 1, which contains information about fares by city pairing and airline:
>For each of the 1,000 largest city-pair markets, Table 1 lists the number of one-way passenger trips per day, the nonstop distance, the average market fare, and identifies the airlines with the largest market share and the lowest average fare; market share and average fares are provided for both airlines. Average fares are average prices paid by all fare paying passengers. They therefore cover first class fares paid to carriers offering such service but do not cover free tickets, such as those awarded by carriers offering frequent flyer programs.

Since these data are significantly larger, the DOT provides an API endpoint for accessing the data. 
The API can be accessed through `query.py`, provided an app token credential is provided. App tokens are free to sign up for using [DOT Developer Tools](https://data.transportation.gov/profile/edit/developer_settings).

A data dictionary for relevant fields is provided on the [DOT Website](https://data.transportation.gov/Aviation/Consumer-Airfare-Report-Table-1-Top-1-000-Contiguo/4f3n-jbg2/about_data)