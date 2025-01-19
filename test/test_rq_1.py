'''Test the functions related to research question one.
Controller does not need to be tested, due to its simplicity.
View cannot be tested, as stated in the course, it is best to test
the correctness of the data provided to the view.'''

import sys
import pandas as pd
import pytest

sys.path.append("./EcoAnalyzerPy")

from controller import rq_1_land as controller
from model import rq_1_land as model
from view import rq_1_land as view

def test_model():
    '''Test the model of research question one.'''

    # Test if the function returns a pandas DataFrame
    result = model.get_data()
    assert isinstance(result, pd.DataFrame)

    # Test if the index of the dataframe is 'Land'
    assert result.index.name == 'Land'

    # Test if the DataFrame has the expected columns
    expected_columns = {2005, 2019, 'Difference'}
    assert set(result.columns.tolist()) >= expected_columns

    # Test if the DataFrame has the expected shape (Rows and columns)
    assert result.shape == (234, 5)

    # Test if the function raises an exception for an invalid file path
    with pytest.raises(FileNotFoundError):
        model.get_data(file="./some/random/file/taht/does/not/exist.csv")
