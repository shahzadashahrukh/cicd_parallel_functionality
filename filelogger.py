#!/usr/bin/env python

import logging
import os
print os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(filename='example.txt',level=logging.DEBUG)
logging.debug('This message should go to the log file 1')
logging.info('So should this 1')
logging.warning('And this, too 1')

logging.basicConfig(filename='example.txt',level=logging.INFO)
logging.debug('This message should go to the log file 2')
logging.info('So should this 2')
logging.warning('And this, too 2')