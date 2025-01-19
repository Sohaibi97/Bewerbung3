import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.errors import ParserError
import logging
import os
import sys
from prepare_data_species import *

#now i get the total of threatened species in each country in 2022
def give_number_by_country(df):
    df=clean_data(df)
    df_world = df[(df['Type'] == 'Total') & (df['Year'] == 2022)]
    df_world = df_world[['Country', 'Year', 'Value']]
    return df_world

