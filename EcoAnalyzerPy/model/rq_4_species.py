#!/usr/bin/env python3

''' What is the trend in number 
of threatened vertebrate species in 
different countires? 
This file contains 
functionality to prepare the data from the
corresponding csv files for plotting.'''

import os
from model.utilities.common import open_csv
from logger import log


current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, '..', '..', 'data', 'clean', 'species_cleaned.csv')

''' What is the trend in number of threatened vertebrate species in different countires? 
    This file contains functionality to prepare the data from the
    corresponding csv files for plotting.'''

def get_data(file = file_path):
    '''Opens the csv file needed for answering
    the fourth research question and prepares the data
    for plotting.'''

    log.info("Called function 'model.rq_4_species.get_data'")

    species = open_csv(file)
    data = prepare_data(species)

    return data

def prepare_data(dataframe):
    '''Takes care of renaming columns and column values,
    changing datatypes and filtering out relevant data '''

    log.info("Called function 'model.rq_4_species.prepare_data'")


    species = dataframe
    filtered_species = species[species['Series'] == 'Vertebrates']

    region_totals = filtered_species .groupby('Region')['Value'].sum()
    print(region_totals)

    top_ten = region_totals.nlargest(10)
    #leastTen = region_totals.nsmallest(10)

    #top ten countries
    filtered_species_regions = filtered_species[filtered_species['Region'].isin(top_ten.index)]

    return filtered_species_regions
