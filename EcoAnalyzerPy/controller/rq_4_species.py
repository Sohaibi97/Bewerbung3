''' Reaserach Question 4: What is the trend in number 
    of threatened vertebrate species in different countires? 
    This file handles passing over the prepared data to 
    the file that takes care of the plotting'''

from model import rq_4_species as model
from view import rq_4_species as view
from logger import log



def research_question_four(show=True):
    '''This controller first gets the data from the model and passes it 
    to the view for plotting.'''
    log.info("Called function 'research_question_four'")
    data = model.get_data()
    view.plot_data(data)
