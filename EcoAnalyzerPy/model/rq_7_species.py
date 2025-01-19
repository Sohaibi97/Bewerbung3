import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.errors import ParserError
import logging
import os
import sys
from prepare_data_species import *

# what is the total of species endangered in those years
def calculate_total(df):
    df=prepareData(df)
    # we start by enclose the search for the total values
    total_df= df[df['Type']=='Total']
    # now we group the values having the same year and we sum the numbers
    Total_endangered=total_df.groupby('Year')['Value'].sum()
    return Total_endangered


