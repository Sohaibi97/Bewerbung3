''' Reaserach Question 6: Is there a correlation between CO2 emissions 
    and permanent crops for the top ten countries?
    This file handles passing over the prepared data to 
    the file that takes care of the plotting'''

from model import rq_6_land_co2 as model
from view import rq_6_land_co2 as view
from logger import log


def research_question_six(show=True):
    '''This controller first gets the data from the model and passes it 
    to the view for plotting.'''
    log.info("Called function 'research_question_six'")   
    data = model.get_data()
    view.plot_data(data)
