#!/usr/bin/env python3

''' How do CO2 emissions relate to land usage?
    This file contains functionality to prepare the data from the
    corresponding csv files for plotting.'''

import os
import pandas as pd
from model.utilities.common import open_csv
from logger import log

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, '..', '..', 'data', 'clean', 'land.csv')
file_path_2 = os.path.join(current_dir, '..', '..', 'data', 'raw',
                           'SYB65_310_202209_Carbon Dioxide Emission Estimates.csv')

def get_data(file = file_path):
    '''Opens the csv file needed for answering
    the fourth research question and prepares the data
    for plotting.'''

    log.info("Called function 'model.rq_5_land.get_data'")


    df1 = open_csv(file)
    df2 = open_csv(file = file_path_2)

    data = prepare_data(df1 , df2)

    return data

def prepare_data(dataframe1, dataframe2):
    '''Takes care of renaming columns and column values,
    changing datatypes and filtering out relevant data '''


    log.info("Called function 'model.rq_5_land.prepare_data'")

    df1 = dataframe1
    df2 = dataframe2

    # Renaming columns
    df1.columns = ["id", "Country", "Year", "Series", "Value", "Footnotes", "Source"]
    df2.columns = ["id", "Country", "Year", "Series", "Value", "Footnotes", "Source"]

    # Removing commas in value
    df1['Value'] = pd.to_numeric(df1['Value'].str.replace(',', ''))
    df2['Value'] = pd.to_numeric(df2['Value'].str.replace(',', ''))

    # filtering irrelevant data
    df1 = df1[df1["Series"] == "Permanent crops (thousand hectares)"]
    df2 = df2[df2["Series"] == "Emissions (thousand metric tons of carbon dioxide)"]

    # merging dataframes
    merged_df = pd.merge(df1, df2, on=["Year", "Country"], how="inner",
                         suffixes=("_Crops", "_Emission"))

    # calculating correlation
    correlation = merged_df["Value_Crops"].corr(merged_df["Value_Emission"])
    print(f"The correlation between Permanent crops and CO2 emissions is: {correlation}")

    # sorting merged data
    merged_df_sorted = merged_df.sort_values("Value_Crops", ascending=False)

    top_countries = []

    # Iterate over sorted data
    for _, row in merged_df_sorted.iterrows():
        # Check emission
        if row["Value_Emission"] > merged_df["Value_Emission"].median():
            top_countries.append(row)

        if len(top_countries) >= 10:
            break

    # Concat
    top_countries = pd.concat(top_countries, axis=1).transpose()

    return top_countries
