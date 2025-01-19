'''Tests behaviour of the plot_data function 
depending on varying dataframes for the research question 6'''

import pytest
import pandas as pd
import numpy as np
from view.rq_6_land_co2 import plot_data



def test_plot_without_data():
    #Test case: Dataframe with correct columns without data
    df = pd.DataFrame(columns=['Country', 'Value_Crops', 'Value_Emission'])
    try:
        plot_data(df)
        print('Success')
    except:
        pytest.fail("There is no error")

def test_plot_data():

    #Test case:Dataframe with data
    data = {
        'Country': ['Test_Country1', 'Test_Country2'],
        'Value_Crops':[1000, 2000],
        'Value_Emission': [3000, 4000]
    }
    df = pd.DataFrame(data)

    try:
        plot_data(df)

        print('Success')
    except:
        pytest.fail("There is no error")

def test_plot_incorrect_collumns():
    #Test case: Dataframe with incorrect columns

    df = pd.DataFrame(columns=['Incorrect_Name1', 'Incorrect_Name2', 'Incorrect_Name3'])
    with pytest.raises(Exception):
        plot_data(df)



