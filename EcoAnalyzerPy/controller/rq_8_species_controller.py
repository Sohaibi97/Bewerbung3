import sys
import os
import pandas as pd
import numpy as np

# here we add the relative path of both model and view
current_path = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_path, r'..\model')
view_path = os.path.join(current_path, r'..\view')
sys.path.append(model_path)
sys.path.append(view_path)
from prepare_data_species import *
from rq_8_species import calculateSeperately
from rq_8_species_view import show_total_by_type

# now we import our functions from our module
df = get_data()
total_endangered_species = calculateSeperately(df)

def research_question_eight():
    show_total_by_type(total_endangered_species)  

