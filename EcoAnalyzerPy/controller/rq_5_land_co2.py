''' Reaserach Question 5: How do CO2 emissions relate to land usage?
    This file handles passing over the prepared data to 
    the file that takes care of the plotting'''

from model import rq_5_land_co2 as model
from view import rq_5_land_co2 as view
from logger import log



def research_question_five(show=True):
    '''This controller first gets the data from the model and passes it 
    to the view for plotting.'''
    log.info("Called function 'research_question_five'")
    data = model.get_data()
    view.plot_data(data)
