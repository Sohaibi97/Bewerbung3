'''This file directory functions that are shared between
the other model files.'''

import sys
import os

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, '..'))
