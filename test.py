from US_VISA.logger import logging
from US_VISA.exception import USvisaException
import sys




try:
    
    a = 1/'s'

except Exception as e:
    raise USvisaException(e , sys) from e
