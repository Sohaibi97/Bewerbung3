'''Set a global configuration for logging.'''

import logging
import sys
import os
import logging.config

current_dir = os.path.dirname(__file__)
logging_file = os.path.join(current_dir, '..', 'logs', 'logs_global.txt')


DEFAULT_LOGGING = {
    'version': 1,
    'formatters': { 
        'standard': {
            'format': '%(asctime)s %(levelname)s: %(message)s',
            'datefmt': '%Y-%m-%d - %H:%M:%S' },
    },
    'handlers': {
        'console':  {'class': 'logging.StreamHandler', 
                     'formatter': "standard", 
                     'level': 'DEBUG', 
                     'stream': sys.stdout},
        'file':     {'class': 'logging.FileHandler', 
                     'formatter': "standard", 
                     'level': 'DEBUG', 
                     'filename': logging_file,'mode': 'a'} 
    },
    'loggers': { 
        __name__:   {'level': 'INFO', 
                     'handlers': ['console', 'file'], 
                     'propagate': False },
    }
}

logging.config.dictConfig(DEFAULT_LOGGING)
log = logging.getLogger(__name__)
