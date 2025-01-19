'''How has the forest cover developed from 2005 to
    2019 in different countries?
    This file contains functionality for answering the research
    question.'''

from model import rq_1_land as model
from view import rq_1_land as view
from logger import log


def research_question_one(show=True):
    '''This controller first gets the data from the model and passes it 
    to the view for plotting.'''
    log.info("Called function 'research_question_one' with parameter show=%s", show)
    data = model.get_data()
    view.plot_data(data, show)
