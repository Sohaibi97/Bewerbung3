import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.errors import ParserError
import logging
import os
import sys
from prepare_data_species import *


# which type of species is endangered and how many of them each year
def calculateSeperately(df):
    df=prepareData(df)
    df_seperately=df[df['Type']!='Total']
    # we catch the case where the Value column contains another type of data other than integers or floats
    try:
        total_endangered_type=df_seperately.groupby(['Year','Type'])['Value'].sum()
    except ValueError:
        raise ValueError("Please check whether the column 'Value' contains data which isnt an integer or a float.")
    return total_endangered_type
