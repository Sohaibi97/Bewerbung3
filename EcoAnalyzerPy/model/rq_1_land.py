#!/usr/bin/env python3

'''How has the forest cover developed from 2005 to 
    2019 in different countries?
    This file contains functionality to prepare the data from the
    corresponding csv files for plotting.'''

import os
from model.utilities.common import open_csv
from logger import log


current_dir = os.path.dirname(__file__)
csv_file = os.path.join(current_dir, '..', '..', 'data', 'clean', 'land.csv')


def get_data(file=csv_file):
    '''Opens the csv file needed for answering
    the first research question and prepares the data
    for plotting.'''

    log.info("Called function 'model.rq_1_land.get_data' with parameter file=%s", file)

    df = open_csv(file)
    # Remove irrelevant data
    df_forest = df[df['Series'] == 'Forest cover (pct of total land area)']
    pivot_df = df_forest.pivot(index='Land', columns='Year', values='Value').dropna(subset=[2019])
    # Calculate the change from 2005 to 2019
    pivot_df['Difference'] = pivot_df[2019].astype(float) - pivot_df[2005].astype(float)

    return pivot_df
