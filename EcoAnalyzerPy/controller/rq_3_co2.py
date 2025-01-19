#!/usr/bin/env python3

''' Reaserach Question 3: How have CO2 emissions changed  
    over time for different countries or regions? 
    This file handles passing over the prepared data to 
    the file that takes care of the plotting'''

from model import rq_3_co2 as model
from view import rq_3_co2 as view
from logger import log

def research_question_three(show=True):
    '''This controller first gets the data from the model and passes it 
    to the view for plotting.'''
    log.info("Called function 'research_question_three'")
    data = model.get_data()
    view.plot_data(data)
