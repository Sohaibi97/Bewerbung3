#!/usr/bin/env python3

''' Reaserach Question 6: Is there a correlation between CO2 emissions 
    and permanent crops for the top ten countries?
    This file handles passing over the prepared data to 
    the file that takes care of the plotting'''

import os
import pandas as pd
from model.utilities.common import open_csv
from logger import log


current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, '..', '..', 'data', 'clean', 'land.csv')
file_path_2 = os.path.join(current_dir, '..', '..', 'data', 'raw', 
                           'SYB65_310_202209_Carbon Dioxide Emission Estimates.csv')


''' Is there a correlation between CO2 emissions and permanent crops for the top ten countries?
    This file contains functionality to prepare the data from the
    corresponding csv files for plotting.'''

def get_data(file = file_path):
    '''Opens the csv file needed for answering
    the six research question and prepares the data
    for plotting.'''

    log.info("Called function 'model.rq_6_land.get_data'")

    dataframe1 = open_csv(file)
    dataframe2 = open_csv(file = file_path_2)
    data = prepare_data(dataframe1, dataframe2)

    return data

def prepare_data(dataframe1, dataframe2):
    '''Takes care of renaming columns and column values,
    changing datatypes and filtering out relevant data '''

    log.info("Called function 'model.rq_6_land.prepare_data'")


    df1 = dataframe1
    df2 = dataframe2

    #Rename columns
    df1.columns = ["id", "Country", "Year", "Series", "Value", "Footnotes", "Source"]
    df2.columns = ["id", "Country", "Year", "Series", "Value", "Footnotes", "Source"]

    #Remove the comma
    df1['Value'] = pd.to_numeric(df1['Value'].str.replace(',', ''))
    df2['Value'] = pd.to_numeric(df2['Value'].str.replace(',', ''))

    #Filter data
    df1 = df1[df1["Series"] == "Permanent crops (thousand hectares)"]
    df2 = df2[df2["Series"] == "Emissions (thousand metric tons of carbon dioxide)"]

    #Merge dataframe
    merged_df = pd.merge(df1, df2, on=["Year", "Country"], how="inner",
                         suffixes=("_Crops", "_Emission"))

    #Find correlation
    correlation = merged_df["Value_Crops"].corr(merged_df["Value_Emission"])
    print(f"The correlation between Permanent crops and CO2 emissions is: {correlation}")

    #countries
    top_crop_countries = merged_df.sort_values("Value_Crops",
                                               ascending=False)["Country"].unique()[:20]
    top_emission_countries = merged_df.sort_values(
        "Value_Emission",
        ascending=False)["Country"].unique()[:20]

    # Find common countries
    common_countries = list(set(top_crop_countries) & set(top_emission_countries))

    # Filter data
    final_df = merged_df[merged_df["Country"].isin(common_countries)].sort_values("Value_Crops",
                                                                                  ascending=False)

    return final_df
