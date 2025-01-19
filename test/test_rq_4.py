'''Tests behaviour of the plot_data function 
depending on varying dataframes for the research question 4'''

import pytest
import pandas as pd
from view.rq_4_species import plot_data

def test_single_region_year():
    '''Tests dataframe with only one region and one year'''
    data = {
        'Region': ['Test Region1'],
        'Value': [1000],
        'Year': [2021]
    }
    df = pd.DataFrame(data)
    try:
        plot_data(df)
        print('Success')
    except:
        pytest.fail('Expected no error with single region and year')


def test_multiple_regions_years():
    '''Tests dataframe with multiple regions and years'''

    data = {
        'Region': ['Test_Region1', 'Test_Region2', 'Test_Region1', 'Test_Region2'],
        'Value': [1000, 2000, 1500, 2500],
        'Year': [2021, 2021, 2022, 2022]
    }
    df = pd.DataFrame(data)
    try:
        plot_data(df)
        print('Success')
    except:
        pytest.fail('Expected no errors with multiple regions and years')


def test_incorrect_columns():
    '''Tests dataframe with incorrect columns'''
    df = pd.DataFrame(columns=['Incorrect_Name1', 'Incorrect_Name2', 'Incorrect_Name3'])
    try:
        plot_data(df)
        pytest.fail('Expected an error with incorrect dataframe')
    except KeyError:
        print("Success")
        pass
