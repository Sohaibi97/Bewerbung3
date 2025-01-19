#!/usr/bin/env python3

''' How have CO2 emissions changed over time
for different countries or regions? 
This file contains functionality 
to prepare the data from the
corresponding csv files for plotting.'''

import os
import pandas as pd
import numpy as np
from model.utilities.common import open_csv
from logger import log


current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, '..', '..', 'data', 'raw',
                         'SYB65_310_202209_Carbon Dioxide Emission Estimates.csv')



def get_data(file = file_path):
    '''Opens the csv file needed for answering
    the third research question and prepares the data
    for plotting.'''

    log.info("Called function 'model.rq3_co2.get_data'")

    carbon_data = open_csv(file)

    data = prepare_data(carbon_data)

    return data

def prepare_data (dataframe):
    '''Takes care of renaming columns and column values,
    changing datatypes and filtering out relevant data '''

    log.info("Called function 'model.rq_3_co2.prepare_data'")

    carbon_data = dataframe

    # ----------- Renaming and Dropping Columns----------
    #print(carbon_data.dtypes)
    carbon_data.rename(columns={"Region/Country/Area": "RegionID", "Unnamed: 1": "Region"}, 
                      inplace = True)

    #print(carbon_data.columns)
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.width', None)

    #print(carbon_data["Series"])
    #print(carbon_data.head(10))

    #simplify names of units
    series_units = {
        'Emissions (thousand metric tons of carbon dioxide)': 'Emissions (kt CO2)',
        'Emissions per capita (metric tons of carbon dioxide)': 'Emissions per capita (t CO2)'
    }
    carbon_data['Series'] = carbon_data['Series'].replace(series_units)

    # ----------- Changing datatypes ----------
    #print(carbon_data.isna().any())
    #print("Any \n", carbon_data.any())
    carbon_data['Year'] = carbon_data['Year'].astype(np.int64)
    carbon_data['Value'] = carbon_data['Value'].str.replace(',', '').astype(float)

    # ---------- Final filtering before plotting ----------
    emissions_df = carbon_data[carbon_data['Series'] == 'Emissions (kt CO2)']

    return emissions_df
