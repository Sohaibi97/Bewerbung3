'''The controller of EcoAnalyzerPy. It fetches the data from the model and
passes it to the view.'''


import sys
import os

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, '..'))
