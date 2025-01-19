import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.errors import ParserError
import logging
import os
import sys
from prepare_data_species import *


#now i calculate the increase precentage between 2004 und 2022
def calculatePercentageIncrease(df):
    df = prepareData(df)
    types=['Vertebrates','Invertebrates','Plants']
    precentage_evolution={}
    for type in types:
        df_separately = df[(df['Type'] == type) & (df['Type'] != 'Total')] 
    
        total_endangered_2004 = df_separately[df_separately['Year'] == 2004].groupby('Type')['Value'].sum()
        total_endangered_2022 = df_separately[df_separately['Year'] == 2022].groupby('Type')['Value'].sum()
        try:
            percentage_increase = ((total_endangered_2022 - total_endangered_2004) / total_endangered_2004) * 100
        except ZeroDivisionError:
            percentage_increase = 100 # for there were no animals in 2004 which were threatened we will just use a 100% increase
        percentage_increase = round(percentage_increase.fillna(0))  # Replace NaN with 0
        #now we know the index
        percentage_increase.index = pd.Index(['Value'], name='Type')
        precentage_evolution[type] = percentage_increase

        
    
    return precentage_evolution