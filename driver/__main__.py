from .functions import request_func, selenium_func
from .parallel import serial, multithread, multiprocess
import json

N = 10

for func in (request_func, selenium_func):
  for par in (multiprocess, serial, multithread):
    for result in par(func, 10):
      print json.dumps(result)
