import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.errors import ParserError
import logging
import os
import sys

# firstly we wanna get our data:
def get_data():
    # when getting our data we could face many problems and exception. We handle them here
    try:
        current_dir = os.path.dirname(__file__)
        csv_file = os.path.join(current_dir, '..', '..', 'data', 'clean', 'Threatened-Species.csv')
        df = pd.read_csv(csv_file)
        return df
    except FileNotFoundError:
        print("The file couldn't be found. Please check if you have given the right path or try to write an r before the path or use two \ instead of one between the folders")
        raise FileNotFoundError
    except PermissionError:
        print("The permission has been denied. You maybe don't have sufficient privileges to access the file.")
        raise PermissionError
    except ParserError:
        print("We encounter an error while parsing the CSV file. Please check the file format.")
        raise ParserError('Please check the structure of the file and the data it countains for issues')
    except UnicodeDecodeError("We encounter an error while decoding the file contents. Unsupported characters or encoding."):
        raise UnicodeDecodeError
    except IOError("Input/output error. Failed to read the file."):
        raise Exception
    return df
    
def prepareData(df):
    df=clean_data(df)
    # we are just going to need this three columns so ill select them
    df = df[['Year', 'Type','Value']]
    return df
    
def clean_data(df):
    #replacing Values
    '''' i dont like the whole String written in Series and i think it could be shorter by defining the type of
    animal using just Vertebrates, Invertebrates, and Plants so i will remplace the values'''

    # i create a map
    replacements = {
        'Threatened Species: Vertebrates (number)': 'Vertebrates',
        'Threatened Species: Invertebrates (number)': 'Invertebrates',
        'Threatened Species: Plants (number)': 'Plants',
        'Threatened Species: Total (number)' : 'Total'
    }

    # now i replace the strings in the 'Series' column based on the defined mappings
    # in case we dont have the column name in our CSV we raise an exception
    try:
        df.loc[:, 'Series'] = df['Series'].replace(replacements)
    except KeyError:
        raise KeyError("Please make sure that you have the column named 'Series")

    # i also dont like the column name so i will change it from Series to Type
    df=df.rename(columns={'Series':'Type'})
    df.rename(columns={df.columns[1]: 'Country'}, inplace=True)

    # now we will find out the number of endangered animals in total each year

    # Now i will change the data type of values to a float
    # if we dont find these columns names, we raise an exception
    try:
        if df['Value'].dtype==object:
            df['Value'] = df['Value'].str.replace(',', '').astype(float)
        df = df[['Year', 'Country', 'Type', 'Value']].reset_index(drop=True)
    except KeyError:
        raise KeyError("Make sure you have columns named Year and Value")
    return df

