# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Move up one level in directory to allow imports
import sys
sys.path.insert(0, '..')

# Get average fare data as a cleaned df for market airports
def get_average_fare_df(all_market_airports, filepath):
    # Import average fare dataframe from table (static by default)
    average_city_fare_df = pd.read_csv(filepath)

    # Filter for market airports
    average_city_fare_df = average_city_fare_df[average_city_fare_df["Airport Code"].isin(all_market_airports)]

    # Drop inflation column
    average_city_fare_df.drop('Inflation Adjusted Average Fare ($) (Base Quarter:  Q2-2025)', axis=1, inplace=True)

    return average_city_fare_df

# Get query data as a cleaned df for market airports
def get_market_df(filepath):
    #Import market info dataframe from static tables
    df = pd.read_csv(filepath)

    # Combine year and quarter, insert at front, and sort
    period = df['year'].astype(str) + "Q" + df['quarter'].astype(str)
    df.insert(0, 'period', period)
    df.sort_values(by="period", ascending=True, inplace=True)

    # Drop extra columns
    df = df.drop(['quarter', 'city1', 'city2', 'nsmiles', 'citymarketid_1', 'citymarketid_2', 'table_1_flag', 'location_1', 'location_2', 'location_1_city', 'location_2_city'], axis=1)

    # Calculate OA market share
    df['OA_ms'] = np.where (
        df['carrier_lg'] == df['carrier_low'],
        1 - (df['large_ms']),
        1 - (df['large_ms'] + df["lf_ms"])
    )

    return df



# Plot market share of largest carrier, lowest fare carrier (if different), and other airlines (OA) over a given time period
def plot_market_share(filepath, starting_period="", periods_per_label=4, route_name=""):
    # Get dataframe for market
    dataframe = get_market_df(filepath)

    # Create helper column for plotting when largest carrier and lowest fare carrier are the same to prevent 2x graphing
    dataframe['lf_ms_plot'] = np.where(
        dataframe['carrier_lg'] == dataframe['carrier_low'],
        0,
        dataframe['lf_ms']
    )

    # Default to earliest period if not specified
    min_quarter = min(dataframe['period'])

    if starting_period == "":
        starting_period = min_quarter


    # Stacked bar chart of main carrier, lowest fare carrier, and OA carriers
    ax = dataframe[dataframe['period'] > starting_period].set_index('period')[['large_ms', 'lf_ms_plot', 'OA_ms']].plot(
        kind='bar',
        stacked=True,
        figsize=(10, 6),
        color=['#1f77b4', '#aec7e8', '#bbbbbb'],
        width=1.0
    )

    # Create year labels every periods_per_label periods
    labels = []
    for i, row in dataframe[dataframe['period'] > starting_period].iterrows():
        if i % periods_per_label == 0:
            labels.append(row['year'])
        else:
            labels.append('')
    ax.set_xticklabels(labels, rotation=45)

    # Get date range for subtitle
    max_quarter = max(dataframe['period'])
    subtitle = str(starting_period[0:4]) + " (" + str(starting_period[4:]) + ") - " + str(max_quarter[0:4]) + " (" + str(max_quarter[4:]) + ")"

    # Formatting
    plt.title(f'Market Share Breakdown by Year - {route_name} \n {subtitle}')
    plt.ylabel('Market Share (%)')
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    plt.xlabel('Year')
    plt.legend(title='Carriers', bbox_to_anchor=(1.05, 1), loc='upper left', labels = ["Largest Carrier", "Lowest Fare Carrier (if different)", "OA",])
    plt.tight_layout()
    return plt